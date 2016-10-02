import re
from utils.print_utils.helpers import print_horizontal_rule
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser
from utils.emoji_utils.emoji_stats import EmojiStats


def main():

    parser = IdSelectionArgumentParser(
        description='Calcuates the comment sentiment taking emojis into account')

    parser.parse_args()
    mark_if_comment_has_emojis(id_selection=parser.id_selection)


def mark_if_comment_has_emojis(id_selection="", db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment sentiment
        - another to update comment_sentiment_emoji records
    """
    emoji_stats = EmojiStats()

    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    id_selection = id_selection.replace('id', 'idcommento')

    results = db_sentiment.fetch_all(
        select='idcommento, english_translation',
        where=id_selection)

    for row in results:
        print_horizontal_rule()
        comment_id = row[0]
        english_translation = row[1]

        print ("Comment_id: %s" % comment_id)
        print ("Translation: %s" % english_translation)

        if emoji_stats.contains_emoji(english_translation):
            emoji_stats.update_db(
                value=1,
                column='has_emoji',
                comment_id=comment_id)

        else:
            print ("Didn't detect any emojis... Not updating db")

    print_horizontal_rule()
    db_sentiment.close()
    emoji_stats.close_db_connection()


if __name__ == '__main__':
    main()
