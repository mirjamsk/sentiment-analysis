from utils.api_utils.sentiment_api import TextProcessingAPI, ViveknAPI
from utils.db_utils.sentiment_db import CommentDbConnection, CommentSentimentDbConnection
from utils.parser_utils.comment_argument_parser import CommentArgumentParser


def run_sentiment_api_batch(api=None,id_selection="", db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment records
        - another to update comment_sentiment records
    """
    db = CommentDbConnection(db=db_name)
    db.connect()

    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    print ('\nUsing %s ' % api)
    print (50 * "-")
    results = db.fetch_all(where=id_selection)

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
    API_choices = {
        ViveknAPI.__name__: ViveknAPI,
        TextProcessingAPI.__name__: TextProcessingAPI}

    parser = CommentArgumentParser(
        description=
        'Makes api calls to determine \
        the sentiment of a comment and \
        store the results in a database')

    parser.add_argument_with_choices(
        '-api',
        required=True,
        choices=API_choices.keys(),
        help='Choose from the listed api options')

    parser.parse_args()

    run_sentiment_api_batch(
        api=API_choices.get(parser.args.api)(),
       id_selection=parser.id_selection)


if __name__ == '__main__':
    main()
