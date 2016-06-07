import re
import json
from utils.print_utils.helpers import print_horizontal_rule
from utils.db_utils.base_db import Database
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.api_utils.sentiment_api import TextProcessingAPI, ViveknAPI, IndicoAPI, IndicoHqAPI
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser


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

    run_sentiment_api_batch(
        api=API_choices.get(parser.args.api)(),
        id_selection=parser.id_selection)


def run_sentiment_api_batch(api=None, id_selection="", db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment sentiment
        - another to update comment_sentiment_emoji records
    """
    db = Database(db=db_name)
    db.connect()

    emoji_regex = get_emoji_regex(db=db)

    try:
        # UCS-4
        emoji_check = re.compile(u'([\U00002600-\U000027BF]|(?![\U0001f3fb-\U0001f3ff])[\U0001f300-\U0001f64F]|[\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        emoji_check = re.compile(u'([\u2600-\u27BF]|[\uD83C][\uDF00-\uDFFF]|[\uD83D][\uDC00-\uDE4F]|[\uD83D][\uDE80-\uDEFF])')

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
        sentiment = json.loads(row[1])
        english_translation = row[2]

        print ("Comment_id: %s" % comment_id)
        print ("Translation: %s" % english_translation)

        #for match in emoji_regex.finditer(english_translation):
        #    print (match.group(0))

        if len(emoji_regex.findall(english_translation)):
            db.update(
                table="im_commento_sentiment_emoji",
                set={'has_emoji':1},
                where="idcommento=%d" %comment_id)


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
