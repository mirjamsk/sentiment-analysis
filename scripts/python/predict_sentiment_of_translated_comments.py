from utils.print_utils.helpers import print_horizontal_rule
from utils.db_utils.base_db import Database
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.api_utils.sentiment_api import TextProcessingAPI, ViveknAPI, IndicoAPI, IndicoHqAPI
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser


def run_sentiment_api_batch(api=None, id_selection="", db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment records
        - another to update comment_sentiment records
    """
    db = Database(db=db_name)
    db.connect()

    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    print ('\nUsing %s ' % api)

    if id_selection != '':
        id_selection = id_selection.replace('id', 'c.id') + ' AND '

    results = db.fetch_all(
        select='c.id, c.content, s.english_translation',
        from_clause=
        'im_commento AS c JOIN   \
        im_commento_sentiment AS s\
        ON c.id = s.idcommento',
        where=id_selection + "s.english_translation != ''",
        order_by='c.id ASC')

    for row in results:
        print_horizontal_rule()
        comment_id = row[0]
        content = row[1]
        english_translation = row[2]

        print ("Comment_id: %s" % comment_id)
        print ("Content: %s" % content)
        print ("Translation: %s" % english_translation)

        api.set_data(english_translation)
        api.post()

        if api.is_request_successful():
            print ("Predicted sentiment: %s" % api.get_sentiment())
            db_sentiment.update(
                comment_id=comment_id,
                sentiment=api.get_sentiment(),
                sentiment_api_column=api.sentiment_api_column)
        else:
            print ("API request was NOT successful: returned %d status code" % api.get_status_code())
            break

    print_horizontal_rule()
    db.close()
    db_sentiment.close()


def main():
    API_choices = {
        ViveknAPI.__name__: ViveknAPI,
        IndicoAPI.__name__: IndicoAPI,
        IndicoHqAPI.__name__: IndicoHqAPI,
        TextProcessingAPI.__name__: TextProcessingAPI}

    parser = IdSelectionArgumentParser(
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
