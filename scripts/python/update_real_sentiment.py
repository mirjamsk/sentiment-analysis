from utils.db_utils.sentiment_db import CommentDbConnection, CommentSentimentDbConnection
from utils.parser_utils.comment_argument_parser import CommentArgumentParser


def get_input_label():
    return raw_input("pos/neg/neu? ").strip()


def update_real_sentiment_batch(select_where_clause="", db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment records
        - another to update comment_sentiment records
    """
    SENTIMENT_LABELS = {
        'pos': 'positive',
        'neg': 'negative',
        'neu': 'neutral'}
    label_choices = set(SENTIMENT_LABELS.keys())

    db = CommentDbConnection(db=db_name)
    db.connect()

    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    results = db.fetch_all(where=select_where_clause)

    for row in results:
        print (35 * "-")

        comment_id = row[0]
        content = row[1]

        print ("Comment_id: %s" % comment_id)
        print ("Content: %s" % content)
        print ("Determine the real_sentiment:")

        real_sentiment = get_input_label()
        while real_sentiment not in label_choices:
            print("%s not in %s" % (real_sentiment, label_choices))
            real_sentiment = get_input_label()

        db_sentiment.update(
            comment_id=comment_id,
            sentiment=SENTIMENT_LABELS[real_sentiment],
            sentiment_api_column='real_sentiment')

        print ("Updated real_sentiment: %s" % SENTIMENT_LABELS[real_sentiment])

    db.close()
    db_sentiment.close()


def main():
    parser = CommentArgumentParser(description='Script for manually updating  real_sentiment of comments')
    parser.parse_args()
    update_real_sentiment_batch(select_where_clause=parser.where_clause)


if __name__ == '__main__':
    main()
