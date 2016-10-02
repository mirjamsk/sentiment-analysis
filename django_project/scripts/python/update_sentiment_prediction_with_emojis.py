import json
from utils.print_utils.helpers import print_horizontal_rule
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.api_utils.sentiment_api import TextProcessingAPI, ViveknAPI, IndicoAPI, IndicoHqAPI
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser
from utils.emoji_utils.emoji_stats import EmojiStats


def main():
    API_choices = {
        ViveknAPI.__name__: ViveknAPI,
        IndicoAPI.__name__: IndicoAPI,
        IndicoHqAPI.__name__: IndicoHqAPI,
        TextProcessingAPI.__name__: TextProcessingAPI}

    parser = IdSelectionArgumentParser(
        description='Calcuates the comment sentiment taking emojis into account')

    parser.add_argument_with_choices(
        '-api',
        required=True,
        choices=API_choices.keys(),
        help='Choose from the listed api options')

    parser.parse_args()

    update_sentiment_emoji_stats(
        api=API_choices.get(parser.args.api)(),
        id_selection=parser.id_selection)


def update_sentiment_emoji_stats(api=None, id_selection="", db_name="sentiment_db"):
    """
    Open three database connections:
        - one to fetch comment sentiment
        - another to fetch emoji stats
        - another to update comment_sentiment_emoji records
    """

    emoji_stats = EmojiStats()
    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    print ('\nUsing %s ' % api)
    id_selection = id_selection.replace('id', 'idcommento')

    results = db_sentiment.fetch_all(
        select='idcommento, %s , english_translation' % api.sentiment_api_column,
        where=id_selection)

    for row in results:
        print_horizontal_rule()
        comment_id = row[0]
        english_translation = row[2]
        print ("Comment_id: %s" % comment_id)
        print ("Translation: %s" % english_translation)

        try:
            api.sentiment_stats = json.loads(row[1])
            print ("Current sentiment: %s" % json.dumps(api.get_sentiment_stats(), indent=2))
        except ValueError:
            print ("ValueError: Not a Json Object: %s" % row[1])
            continue

        if emoji_stats.contains_emoji(english_translation):
            comment_emoji_stats = emoji_stats.get_comment_emoji_stats(english_translation)
            api.update_emoji_sentiment_stats(comment_emoji_stats)
            print ("Updated sentiment: %s" % json.dumps(api.get_sentiment_stats(), indent=2))


        emoji_stats.update_db(
            comment_id=comment_id,
            column=api.sentiment_api_column,
            value=json.dumps(api.get_sentiment_stats()))

    print_horizontal_rule()
    db_sentiment.close()
    emoji_stats.close_db_connection()


if __name__ == '__main__':
    main()
