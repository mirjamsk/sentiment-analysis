import json
import argparse
from utils.metric_utils.facade_metric import Metric
from utils.metric_utils.specific_metrics import AccuracyMetric, RecallMetric, PrecisionMetric
from utils.db_utils.sentiment_api_stats_db import SentimentApiStatsDbConnection
from utils.print_utils.helpers import print_horizontal_rule, print_sparse_horizontal_rule
from utils.db_utils.sentiment_db import CommentSentimentDbConnection, CommentEmojiSentimentDbConnection


def main():
    sentiment_api_columns = (
        'sentiment_api1',
        'sentiment_api1_en',
        'sentiment_api2',
        'sentiment_api2_en',
        'sentiment_api3',
        'sentiment_api4'
    )
    metrics = (
        PrecisionMetric.metric_name(),
        AccuracyMetric.metric_name(),
        RecallMetric.metric_name(),
    )
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
        required=False,
        choices=metrics,
        help='Choose from the listed metric options')

    spam = parser.add_mutually_exclusive_group(required=False)
    spam.add_argument('--spam', dest='spam', action='store_true')
    spam.add_argument('--no-spam', dest='spam', action='store_false')

    emoji = parser.add_mutually_exclusive_group(required=False)
    emoji.add_argument('--emoji', dest='emoji', action='store_true')
    emoji.add_argument('--no-emoji', dest='emoji', action='store_false')

    parser.set_defaults(spam=None)
    parser.set_defaults(emoji=None)

    args = parser.parse_args()
    if args.api is not None:
        sentiment_api_columns = (args.api,)

    spam = (args.spam,) if args.spam is not None else (True, False,)
    emoji = (args.emoji,) if args.emoji is not None else (True, False,)

    if args.metric is not None:
        metrics = (args.metric,)

    calculate_accuracy(
        spam=spam,
        emoji=emoji,
        metrics=metrics,
        sentiment_api_columns=sentiment_api_columns)


def calculate_accuracy(emoji='', metrics=None, spam=None, sentiment_api_columns=None, db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment sentiment
        - one to store accuracy in sentiment api stats table
    """
    db = CommentSentimentDbConnection(db=db_name)
    db.connect()

    db_emoji = CommentEmojiSentimentDbConnection(db=db_name)
    db_emoji.connect()

    db_update = SentimentApiStatsDbConnection(db=db_name)
    db_update.connect()

    for sentiment_api_column in sentiment_api_columns:
        for consider_spam in spam:
            for consider_emoji in emoji:
                update_single_performance(db, db_emoji, db_update, consider_spam, consider_emoji, metrics, sentiment_api_column)

    print_horizontal_rule()
    db_update.close()
    db_emoji.close()
    db.close()


def update_single_performance(db, db_emoji, db_update, consider_spam, consider_emoji, metrics, sentiment_api_column):
    print_horizontal_rule()
    print_horizontal_rule()

    print("Calculations for api: %s %s spam" % (
        sentiment_api_column + ('_emoji' if consider_emoji else ''),
        'with' if consider_spam else 'without'))

    where_clause = '(real_sentiment is not null OR real_sentiment != "") AND %s !="{}" ' % sentiment_api_column
    where_clause = where_clause if consider_spam else where_clause + ' AND spam REGEXP "false"'

    metric = Metric(metrics)
    results = db.fetch_all(
        select='idcommento, real_sentiment, %s' % sentiment_api_column,
        where=where_clause)

    for row in results:
        comment_id = row[0]
        try:
            real_sentiment = json.loads(row[1])
            api_sentiment = json.loads(row[2])
        except ValueError:
            continue
        if not real_sentiment or not api_sentiment:
            continue

        if consider_emoji:
            try:
               api_sentiment = json.loads(db_emoji.fetch_sentiment_by_comment_id(
                    comment_id=comment_id,
                    sentiment=sentiment_api_column)[0][0])
            except IndexError:
                continue
         
        metric.update_stats(
            real_sentiment=real_sentiment,
            predicted_sentiment=api_sentiment)

        # print_each_step(metric, comment_id, sentiment_api_column + '_emoji' if emoji else '', api_sentiment, real_sentiment)
        # print_horizontal_rule()

    metric.print_real_sentiment_distribution()
    metric.calculate_stats()
    metric.print_stats()

    for metric_name in metrics:
        print_sparse_horizontal_rule()
        db_update.update(
            column=metric.get_db_column(metric_name, consider_spam),
            value=metric.get_db_safe_stats(metric_name),
            api_id=sentiment_api_column + ('_emoji' if consider_emoji else ''))


def print_each_step(metric, comment_id, sentiment_api_column, api_sentiment, real_sentiment):
    print ("Comment id: %d" % comment_id)
    print ("%s: %s vs %s" % (sentiment_api_column, real_sentiment['sentiment_label'], api_sentiment['sentiment_label']))
    metric.print_stats()


if __name__ == '__main__':
    main()
