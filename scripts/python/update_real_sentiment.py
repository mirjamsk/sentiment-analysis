import argparse
from db_utils.sentiment_db import CommentDbConnection, CommentSentimentDbConnection


def get_input_label():
    return raw_input("pos/neg/neu? ").strip()


def update_real_sentiment_batch(select_where_clause="", db_name="sentiment_db"):
    # Open database connections
    # we need two: one for fetch records and another for update records)

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
        comment_id = row[0]
        content = row[1]

        print ("Comment_id: %s" % comment_id)
        print ("Content: %s" % content)
        print ("Determine the real_sentiment:")

        real_sentiment = get_input_label()
        while real_sentiment not in label_choices:
            print("%s not in %s" %(real_sentiment, label_choices))
            real_sentiment = get_input_label()

        db_sentiment.update(
            comment_id=comment_id,
            sentiment=SENTIMENT_LABELS[real_sentiment],
            sentiment_api_column='real_sentiment')

        print ("Updated real_sentiment: %s" %SENTIMENT_LABELS[real_sentiment])

        print (35 * "-")

    db.close()
    db_sentiment.close()


def main():

    parser = argparse.ArgumentParser(
        description='Script for manually updating real_sentiment of comments')
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

    print (35 * "-")
    update_real_sentiment_batch(select_where_clause=where_clause)


if __name__ == '__main__':
    main()
