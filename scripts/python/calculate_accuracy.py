import json
import argparse
from utils.db_utils.sentiment_api_stats_db import SentimentApiStatsDbConnection
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.print_utils.helpers import print_horizontal_rule


def main():
    sentiment_api_columns = (
        'sentiment_api1',
        'sentiment_api1_en',
        'sentiment_api2',
        'sentiment_api2_en',
        'sentiment_api3',
        'sentiment_api4'
    )
    metric = (
        'accuracy',
    )
    parser = argparse.ArgumentParser(description='Calc accuracy')

    parser.add_argument(
        '--api',
        required=True,
        choices=sentiment_api_columns,
        help='Choose from the listed api column options')
    parser.add_argument(
        '--metric',
        required=True,
        choices=metric,
        help='Choose from the listed metric options')

    spam = parser.add_mutually_exclusive_group(required=True)
    spam.add_argument('--spam', dest='spam', action='store_true')
    spam.add_argument('--no-spam', dest='spam', action='store_false')

    args = parser.parse_args()
    print(args.spam)
    calculate_accuracy(
        metric=args.metric,
        consider_spam=args.spam,
        sentiment_api_column=args.api)


def calculate_accuracy(metric='', consider_spam=False, sentiment_api_column='', db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment sentiment
        - one to store accuracy in sentiment api stats table
    """

    db = CommentSentimentDbConnection(db=db_name)
    db.connect()
    db_update = SentimentApiStatsDbConnection(db=db_name)
    db_update.connect()

    where_clause = '(real_sentiment is not null OR real_sentiment != "") AND %s !="{}" ' % sentiment_api_column
    where_clause = where_clause if  consider_spam else where_clause + ' AND spam REGEXP "false"'

    results = db.fetch_all(
        select='idcommento, real_sentiment, %s' % sentiment_api_column,
        where=where_clause)

    print_horizontal_rule()
    total_sentiment_predictions = 0
    correct_sentiment_predictions = 0
    for row in results:
        comment_id = row[0]
        real_sentiment = json.loads(row[1])
        api_sentiment = json.loads(row[2])

        total_sentiment_predictions += 1
        if real_sentiment['sentiment_label'] == api_sentiment['sentiment_label']:
            correct_sentiment_predictions +=1

        #print_each_step(
        #    comment_id,
        #    api_sentiment,
        #    real_sentiment,
        #    sentiment_api_column,
        #    correct_sentiment_predictions,
        #    total_sentiment_predictions)
        #print_horizontal_rule()

    accuracy = round(correct_sentiment_predictions/float(total_sentiment_predictions), 4)
    print("Calculations for api: %s " % sentiment_api_column)
    print("Correct sentiment predictions: %d " % correct_sentiment_predictions)
    print("Total sentiment predictions: %d " % total_sentiment_predictions)
    print("Accuracy: %f " % accuracy)
    print_horizontal_rule()

    db_update.update(
        column=metric if not consider_spam else metric + '_with_spam',
        value=accuracy,
        api_id=sentiment_api_column)

    db.close()
    db_update.close()


def print_each_step(
        comment_id,
        api_sentiment,
        real_sentiment,
        sentiment_api_column,
        correct_sentiment_predictions,
        total_sentiment_predictions):

    print ("Comment id: %d" % comment_id)
    print ("%s: %s vs %s" % (sentiment_api_column, real_sentiment['sentiment_label'], api_sentiment['sentiment_label']))
    print('Correct predictions: %d' % correct_sentiment_predictions)
    print('Total predictions: %d' % total_sentiment_predictions)

if __name__ == '__main__':
    main()
