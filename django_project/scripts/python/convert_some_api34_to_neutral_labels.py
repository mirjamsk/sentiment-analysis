import json
from copy import deepcopy
import operator
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.print_utils.helpers import print_horizontal_rule
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser
from utils.api_utils.sentiment_default_stats import SENTIMENT_DEFAULT_STATS


def main():
    sentiment_api_columns = (
        'sentiment_api3',
        'sentiment_api4'
    )

    parser = IdSelectionArgumentParser(
        description=
        'Converts some sentiment_api3&4 labels to neutral')

    parser.add_argument_with_choices(
        '-api',
        required=True,
        choices=sentiment_api_columns,
        help='Choose from the listed api column options')

    parser.parse_args()
    convert_sentiment_api_labels(
        id_selection=parser.id_selection,
        sentiment_api_column=parser.args.api)


def convert_sentiment_api_labels(sentiment_api_column='', id_selection='', db_name="sentiment_db"):
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
        sentiment = json.loads(row[1])

        print ("Comment id: %d" % comment_id)
        print ("%s: %s" % (sentiment_api_column, json.dumps(sentiment, indent=2)))

        if not sentiment:
            continue
        if 'sentiment_stats' not in sentiment:
            sentiment_stats = deepcopy(sentiment)
            sentiment = deepcopy(SENTIMENT_DEFAULT_STATS)
            sentiment['sentiment_stats'] = sentiment_stats
            sentiment['sentiment_label'] = get_most_frequent_label(deepcopy(sentiment['sentiment_stats']))
            raw_input()

        sentiment['sentiment_label'] = get_most_frequent_label(deepcopy(sentiment['sentiment_stats']))
        if is_neutral(sentiment['sentiment_stats']):
            sentiment['sentiment_label'] = 'neutral'
        print ("Converting to...")
        print ("%s: %s" % (sentiment_api_column, json.dumps(sentiment, indent=2)))

        db.update(
            column=sentiment_api_column,
            value=json.dumps(sentiment),
            comment_id=comment_id)

        print_horizontal_rule()

    db.close()


def get_most_frequent_label(stats={}):
    stats.pop('total', None)
    return max(stats.items(), key=operator.itemgetter(1))[0]


def is_neutral(stats={}):
    if 0.35 <= stats['positive'] < 0.65:
        return True
    return False


if __name__ == '__main__':
    main()
