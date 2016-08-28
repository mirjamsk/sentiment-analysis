import re
from utils.print_utils.helpers import print_horizontal_rule
from utils.db_utils.base_db import Database
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser


def main():

    parser = IdSelectionArgumentParser(
        description='Calcuates the comment sentiment taking emojis into account')

    parser.parse_args()
    check_if_comment_has_emojis(id_selection=parser.id_selection)


def check_if_comment_has_emojis(id_selection="", db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment sentiment
        - another to update comment_sentiment_emoji records
    """
    db = Database(db=db_name)
    db.connect()

    emoji_regex = get_emoji_regex(db=db)

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

        if len(emoji_regex.findall(english_translation)):
            db.update(
                table="im_commento_sentiment_emoji",
                set={'has_emoji': 1},
                where="idcommento=%d" % comment_id)

    print_horizontal_rule()
    db.close()
    db_sentiment.close()


def get_emoji_regex(db):
    emoji_regex = set([])
    results = db.fetch_all(select="`char`", from_clause="im_emoji_stats")
    for row in results:
        emoji_regex.add(
            row[0].replace('(', '\(')
                .replace(')','\)')
                .replace(':','\:')
                .replace('*','\*')
                .replace('-','\-')
                .replace('_','\_')
                .replace('.', '\.'))

    emoji_regex = '|'.join(emoji_regex)
    emoji_regex = u'(' + emoji_regex + ')'

    return re.compile(emoji_regex)

if __name__ == '__main__':
    main()
