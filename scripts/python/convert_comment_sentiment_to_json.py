import json
import operator
from copy import deepcopy
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.print_utils.helpers import print_horizontal_rule
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser

SENTIMENT_DEFAULT_STATS = {
    'positive': 0,
    'negative': 0,
    'neutral': 0
}


def main():
    sentiment_api_columns = (
        'real_sentiment',
        'sentiment_api1',
        'sentiment_api1_en',
        'sentiment_api2',
        'sentiment_api2_en',
        'sentiment_api3',
        'sentiment_api4'
    )
    parser = IdSelectionArgumentParser(
        description=
        'Converts comments\' sentiment \
        string values (labels) to json  \
        stores the results in a database')

    parser.add_argument_with_choices(
        '-api',
        required=True,
        choices=sentiment_api_columns,
        help='Choose from the listed api column options')

    parser.parse_args()
    convert_comment_sentiment_to_json(
        id_selection=parser.id_selection,
        sentiment_api_column=parser.args.api)


def convert_comment_sentiment_to_json(sentiment_api_column='', id_selection='', db_name="sentiment_db"):
    """
    Open one database connections:
        - to fetch comment sentiment
        - and to convert it to a json form
    """

    db = CommentSentimentDbConnection(db=db_name)
    db.connect()

    results = db.fetch_all(
        select='idcommento, %s' % sentiment_api_column,
        where=id_selection.replace('id', 'idcommento'))

    for row in results:
        print_horizontal_rule()
        comment_id = row[0]
        api_sentiment = row[1]

        print ("Comment id: %d" % comment_id)
        print ("%s: %s" % (sentiment_api_column, api_sentiment))

        if api_sentiment is None or api_sentiment == '':
            print('No record (nothing to convert)')
            print_horizontal_rule()
            continue
        elif is_json(api_sentiment):
            print('Already in json format')
            print_horizontal_rule()
            continue

        sentiment_stats = deepcopy(SENTIMENT_DEFAULT_STATS)
        sentiment_stats[api_sentiment] = 1.0
        print ("Converting to...")
        print ("%s: %s" % (sentiment_api_column, json.dumps(sentiment_stats)))

        db.update(
            column=sentiment_api_column,
            value=json.dumps(sentiment_stats),
            comment_id=comment_id)

        print_horizontal_rule()

    db.close()


def is_json(json_str):
    try:
        json.loads(json_str)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    main()
