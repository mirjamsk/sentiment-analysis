import re
import json
from utils.print_utils.helpers import print_horizontal_rule
from utils.db_utils.sentiment_db import CommentSentimentDbConnection, CommentEmojiSentimentDbConnection
from utils.api_utils.sentiment_api import TextProcessingAPI, ViveknAPI, IndicoAPI, IndicoHqAPI
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser
from utils.db_utils.base_db import Database


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
    db = Database(db=db_name)
    db.connect()

    emoji_stats = get_emoji_stats(db=db)
    emoji_regex = get_emoji_regex(emoji_stats)

    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    db_emoji_sentiment = CommentEmojiSentimentDbConnection(db=db_name)
    db_emoji_sentiment.connect()

    print ('\nUsing %s ' % api)
    id_selection = id_selection.replace('id', 'idcommento')

    results = db_sentiment.fetch_all(
        select='idcommento, %s , english_translation' % api.sentiment_api_column,
        where=id_selection)

    for row in results:
        print_horizontal_rule()
        comment_id = row[0]
        api.sentiment_stats = json.loads(row[1])
        english_translation = row[2]

        print ("Comment_id: %s" % comment_id)
        print ("Translation: %s" % english_translation)
        print ("Current sentiment: %s" % json.dumps(api.get_sentiment_stats(), indent=2))

        emojis = emoji_regex.findall(english_translation)
        if len(emojis):
            comment_emoji_stats = get_comment_emoji_stats(emoji_stats, emojis)
            api.update_emoji_sentiment_stats(comment_emoji_stats)
            print('Found emojis: %s' % (' '.join(emojis)))
            print ("Updated sentiment: %s" % json.dumps(api.get_sentiment_stats(), indent=2))

        db_emoji_sentiment.update(
            comment_id=comment_id,
            column=api.sentiment_api_column,
            value=json.dumps(api.get_sentiment_stats()))


    print_horizontal_rule()
    db.close()
    db_sentiment.close()


def get_emoji_stats(db):
    """
    emoji_stats = {
        ':)': {
            'neutral': 0.3,
            'positive': 0.3,
            'negative': 0.6,
            'sentiment_score': -0.2
        }
    }
    """
    emoji_stats = {}
    results = db.fetch_all(
        select="`char`,`neutral`,`positive`, `negative`,`sentiment_score`",
        from_clause="im_emoji_stats")

    for row in results:
        emoji = row[0]
        emoji_stats[emoji] = {
            'neutral': row[1],
            'positive': row[2],
            'negative': row[3],
            'sentiment_score': row[4]}
    return emoji_stats


def sanitize_emojis(emojis):
    return emojis\
            .replace('(', '\(')\
            .replace(')', '\)')\
            .replace(':', '\:')\
            .replace('*', '\*')\
            .replace('-', '\-')\
            .replace('_', '\_')\
            .replace('.', '\.')


def get_emoji_regex(emoji_stats):
    emoji_regex = sanitize_emojis('|'.join(emoji_stats.keys()))
    emoji_regex = u'(' + emoji_regex + ')'

    return re.compile(emoji_regex)


def get_comment_emoji_stats(emoji_stats, comment_emojis):
    comment_emoji_stats = []
    for emoji in comment_emojis:
        comment_emoji_stats.append(emoji_stats[emoji])
    return comment_emoji_stats

if __name__ == '__main__':
    main()
