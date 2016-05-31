import json
import argparse
from utils.print_utils.helpers import print_horizontal_rule
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.db_utils.sentiment_api_stats_db import SentimentApiStatsDbConnection
from utils.metric_utils.specific_metrics import AccuracyMetric, RecallMetric, PrecisionMetric


def main():
    sentiment_api_columns = (
        'sentiment_api1',
        'sentiment_api1_en',
        'sentiment_api2',
        'sentiment_api2_en',
        'sentiment_api3',
        'sentiment_api4'
    )
    metric = {
        'precision': PrecisionMetric,
        'accuracy': AccuracyMetric,
        'recall': RecallMetric
    }
    parser = argparse.ArgumentParser(
        description=
        'Evaluates API\'s performance \
        using defined metrics and then \
        stores the results in a database')

    parser.add_argument(
        '--api',
        required=False,
        choices=sentiment_api_columns,
        help='Choose from the listed api column options')

    parser.add_argument(
        '--metric',
        required=True,
        choices=metric.keys(),
        help='Choose from the listed metric options')

    spam = parser.add_mutually_exclusive_group(required=True)
    spam.add_argument('--spam', dest='spam', action='store_true')
    spam.add_argument('--no-spam', dest='spam', action='store_false')

    args = parser.parse_args()
    if args.api is not None:
        sentiment_api_columns = (args.api,)

    calculate_accuracy(
        metric=metric.get(args.metric)(),
        consider_spam=args.spam,
        sentiment_api_columns=sentiment_api_columns)


def calculate_accuracy(metric=None, consider_spam=False, sentiment_api_columns=None, db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment sentiment
        - one to store accuracy in sentiment api stats table
    """
    db = CommentSentimentDbConnection(db=db_name)
    db.connect()
    db_update = SentimentApiStatsDbConnection(db=db_name)
    db_update.connect()
    for sentiment_api_column in sentiment_api_columns:
        metric.clear_stats()
        print_horizontal_rule()
        print_horizontal_rule()
        print("Calculations for api: %s " % sentiment_api_column)

        where_clause = '(real_sentiment is not null OR real_sentiment != "") AND %s !="{}" ' % sentiment_api_column
        where_clause = where_clause if consider_spam else where_clause + ' AND spam REGEXP "false"'

        results = db.fetch_all(
            select='idcommento, real_sentiment, %s' % sentiment_api_column,
            where=where_clause)

        for row in results:
            comment_id = row[0]
            real_sentiment = json.loads(row[1])
            api_sentiment = json.loads(row[2])

            metric.update_stats(
                real_sentiment=real_sentiment,
                predicted_sentiment=api_sentiment)

            #print_each_step(metric, comment_id, sentiment_api_column, api_sentiment, real_sentiment)
            #print_horizontal_rule()

        metric.calculate_stats()
        metric.print_stats()
        print_horizontal_rule()

        db_update.update(
            column=metric.db_column if not consider_spam else metric.db_column_with_spam,
            value=metric.get_db_safe_stats(),
            api_id=sentiment_api_column)

    db.close()
    db_update.close()


def print_each_step( metric, comment_id, sentiment_api_column, api_sentiment, real_sentiment):
    print ("Comment id: %d" % comment_id)
    print ("%s: %s vs %s" % (sentiment_api_column, real_sentiment['sentiment_label'], api_sentiment['sentiment_label']))
    metric.print_stats()

if __name__ == '__main__':
    main()
