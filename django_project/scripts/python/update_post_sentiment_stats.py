import json
import operator
from copy import deepcopy
from utils.db_utils.base_db import Database
from utils.print_utils.helpers import print_horizontal_rule
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser

SENTIMENT_DEFAULT_STATS = {
    'total_comments': 0,
    'sentiment_label': '',
    'sentiment_stats': {
        'total': 0
    }
}
SENTIMENT_API_COLUMNS = (
    'real_sentiment',
    'sentiment_api1',
    'sentiment_api1_en',
    'sentiment_api2',
    'sentiment_api2_en',
    'sentiment_api3',
    'sentiment_api4'
)

def main():

    parser = IdSelectionArgumentParser(
        description=
        'Calculates posts\' sentiment \
        stats using comment labels and \
        stores the results in a database')

    parser.add_argument_with_choices(
        '-api_column',
        required=False,
        choices=SENTIMENT_API_COLUMNS,
        help=
        'Choose from the listed api column \
        options. If argument not specified, \
        algorithm runs for all listed columns')

    parser.parse_args()
    if parser.args.api_column is not None:
        sentiment_api_columns = (parser.args.api_column,)
    else:
        sentiment_api_columns = SENTIMENT_API_COLUMNS

    update_post_sentiment_stats(
        id_selection=parser.id_selection,
        sentiment_api_columns=sentiment_api_columns)


def update_post_sentiment_stats(sentiment_api_columns=SENTIMENT_API_COLUMNS, id_selection='', db_name="sentiment_db"):
    """
    Open one database connection:
        - to fetch post records and calculate sentiment stats
        - to update post_sentiment records
    """

    db = Database(db=db_name)
    db.connect()

    # there is ~200k posts, but only ~300 have comments
    # run the algorithm only for the posts with comments
    # and update the rest with zero total count in one go
    subquery = "(SELECT DISTINCT idpost FROM im_commento)"
    where_clause = '' if id_selection == '' else id_selection + ' AND '

    results = db.fetch_all(
        select='id',
        from_clause='im_post',
        where=where_clause + 'id in ' + subquery,
        order_by='id')

    if len(results) != 0:
        determine_and_update_post_sentiment(
            rows=results,
            db=db,
            sentiment_api_columns=sentiment_api_columns)

    # set default post sentient
    set_default_post_sentiment(
        subquery=subquery,
        db=db,
        where_clause=where_clause,
        sentiment_api_columns=sentiment_api_columns)

    db.close()


def set_default_post_sentiment(subquery, where_clause, db, sentiment_api_columns):
    print_horizontal_rule()
    print('Setting columns %s of commentless posts to default to JSON:' % '\n '.join(sentiment_api_columns))
    print(json.dumps(SENTIMENT_DEFAULT_STATS, indent=2))

    set_clause = {api_column: json.dumps(SENTIMENT_DEFAULT_STATS) for api_column in sentiment_api_columns}
    db.update(
        table='im_post_sentiment',
        set=set_clause,
        where=where_clause.replace('id', 'idpost') + 'idpost not in ' + subquery)
    print_horizontal_rule()


def determine_and_update_post_sentiment(rows, db, sentiment_api_columns):
    for row in rows:
        print_horizontal_rule()
        post_id = row[0]

        for api_column in sentiment_api_columns:
            sentiment_stats = count_comment_sentiment_labels(
                db=db,
                post_id=post_id,
                api_column=api_column)

            print ("Post id: %s" % post_id)
            print ("Api column: %s" % api_column)
            print (json.dumps(sentiment_stats, indent=2))

            db.update(
                table='im_post_sentiment',
                set={api_column: json.dumps(sentiment_stats)},
                where='idpost=%d' % post_id)

            print_horizontal_rule()


def count_comment_sentiment_labels(post_id, api_column, db):
    sentiment_stats = deepcopy(SENTIMENT_DEFAULT_STATS)
    results = db.fetch_all(
        select=api_column,
        from_clause=
        "im_commento AS c JOIN   \
        im_commento_sentiment AS s ON c.id = s.idcommento",
        where=
        "c.idpost = {0} AND (s.spam like '%is_spam%false%' or s.spam like '{1}')".format(post_id, '{}'))
    for row in results:
        comment_sentiment = row[0]
        if comment_sentiment is None or comment_sentiment == '' or  comment_sentiment == '{}':
            continue
        comment_sentiment = json.loads(comment_sentiment)
        #print(comment_sentiment)

        stats = sentiment_stats['sentiment_stats']

        # adds up all sentiment probabilities
        # for sentiment in ['neutral', 'positive', 'negative']:
        #    stats[sentiment] = stats.get(sentiment, 0.0) + float(comment_sentiment[sentiment])
        #    stats['total'] += float(comment_sentiment[sentiment])

        # adds up only the labeled sentiment
        sentiment = comment_sentiment['sentiment_label']
        stats[sentiment] = stats.get(sentiment, 0) + 1
        stats['total'] += 1

        sentiment_stats['total_comments'] += 1
        sentiment_stats['sentiment_label'] = get_most_frequent_label(deepcopy(sentiment_stats['sentiment_stats']))

    return sentiment_stats


def get_most_frequent_label(stats={}):
    stats.pop('total', None)
    return max(stats.items(), key=operator.itemgetter(1))[0]


if __name__ == '__main__':
    main()
