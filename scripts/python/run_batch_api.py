from db_utils import CommentDbConnection, CommentSentimentDbConnection
from api_utils import TextProcessingApi, ViveknApi


def run_sentiment_api_batch(api=None, select_where_clause=""):
    # Open database connections
    # we need two: one for fetch records and another for update records)
    db = CommentDbConnection(db="test_db")
    db.connect()

    db_sentiment = CommentSentimentDbConnection(db="test_db")
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

        if api.is_request_successful:
            print ("Predicted sentiment: %s" % api.get_sentiment())
            db_sentiment.update(
                comment_id=comment_id,
                sentiment=api.get_sentiment(),
                sentiment_api_column=api.sentiment_api_column)

        print (29 * "-")

    db.close()
    db_sentiment.close()


#run_sentiment_api_batch(api=TextProcessingApi(), select_where_clause='id<5')
run_sentiment_api_batch(api=ViveknApi(), select_where_clause='id<5')
