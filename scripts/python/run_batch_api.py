import argparse
from db_utils.sentiment_db import CommentDbConnection, CommentSentimentDbConnection
from api_utils.sentiment_api import TextProcessingAPI, ViveknAPI


def run_sentiment_api_batch(api=None, select_where_clause="", db_name="sentiment_db"):
    # Open database connections
    # we need two: one for fetch records and another for update records)
    db = CommentDbConnection(db=db_name)
    db.connect()

    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    print ('\nUsing %s ' % api)
    print (50 * "-")
    results = db.fetch_all(where=select_where_clause)

    for row in results:
        comment_id = row[0]
        content = row[1]

        print ("Comment_id: %s" % comment_id)
        print ("Content: %s" % content)

        api.set_data(content)
        api.post()

        if api.is_request_successful():
            print ("Predicted sentiment: %s" % api.get_sentiment())
            db_sentiment.update(
                comment_id=comment_id,
                sentiment=api.get_sentiment(),
                sentiment_api_column=api.sentiment_api_column)
        else:
            print("API request was NOT successful: returned %d status code" % api.get_status_code())
            break
        print (29 * "-")

    db.close()
    db_sentiment.close()


def main():
    API_choices = {ViveknAPI.__name__: ViveknAPI,
                   TextProcessingAPI.__name__: TextProcessingAPI}

    parser = argparse.ArgumentParser(
        description='Script for making api calls to determine the sentiment of comment and store it in a database')
    parser.add_argument('-api',
                        required=True,
                        choices=API_choices.keys(),
                        help='Choose from the listed api options')

    parser.add_argument('-ideq',
                        type=int,
                        required=False,
                        help='Update a specific comment by specifying it\'s id')
    parser.add_argument('-idlt',
                        type=int,
                        required=False,
                        help='Update all comments with id less than the specified id')
    parser.add_argument('-idgt',
                        type=int,
                        required=False,
                        help='Update all comments with id greater than the specified id')

    args = parser.parse_args()

    where_clause = ''
    if args.ideq is not None:
        where_clause = 'id=%d' % args.ideq
    else:
        if args.idlt is not None:
            where_clause = 'id < %d' % args.idlt
        if args.idgt is not None:
            where_clause += ' AND ' if where_clause != '' else ''
            where_clause += 'id > %d' % args.idgt

    run_sentiment_api_batch(api=API_choices.get(args.api)(), select_where_clause=where_clause)


if __name__ == '__main__':
    main()
