import json
from utils.db_utils.sentiment_db import CommentSentimentDbConnection
from utils.print_utils.helpers import print_horizontal_rule
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser

URL_QUERY = {
    'url': '(\
        english_translation REGEXP "(https?:[[:space:]]*\/\/|www\.)[\.A-Za-z0-9\-]+\.[a-zA-Z]{2,4}" OR \
        english_translation REGEXP "[\.]{1}[A-Za-z0-9\-]+[\.]{1}[a-zA-Z]{2,4}[\.]?([[:space:]]|[[.slash.]]|$)" \
        OR ( english_translation NOT REGEXP "[[.commercial-at.]]{1}" AND \
        english_translation REGEXP "[[:alnum:]]+[\.]{1}(com|net|org|gov)([[:space:]]|[[.slash.]]|$)" \
        ))',
    'blank': '(english_translation is null or english_translation="")'
}


def main():
    parser = IdSelectionArgumentParser(
        description=
        'Marks comments that \
         contain a url as spam \
         and updates the database')

    parser.add_argument_with_choices(
        '-type',
        required=True,
        choices=URL_QUERY.keys(),
        help='Choose from the listed spam type options')

    parser.parse_args()
    spam_json = {
        'is_spam': True,
        'type': parser.args.type
    }
    mark_url_comments_spam(
        spam_json=spam_json,
        url_query=URL_QUERY[parser.args.type],
        id_selection=parser.id_selection)


def mark_url_comments_spam(id_selection='*', spam_json={}, url_query='', db_name="sentiment_db"):
    """
    Open one database connections:
        - to find the comment_sentiment records containing a url
        - and to update comment_sentiment records spam/not spam
    """
    db = CommentSentimentDbConnection(db=db_name)
    db.connect()

    id_selection = id_selection.replace('id', 'idcommento')
    where_clause = '' if id_selection == '' else id_selection + ' AND '
    results = db.fetch_all(
        where=where_clause + url_query)

    if len(results) != 0:
        print('Found %d %s comments' % (len(results), spam_json.get('type', '')))
        mark_comments_as_spam(
            db=db,
            rows=results,
            spam_json=spam_json)
    else:
        print ("No comments match the required conditions")

    db.close()


def mark_comments_as_spam(spam_json, rows, db):
    for row in rows:
        print_horizontal_rule()
        comment_id = row[1]
        english_translation = row[2]

        print ("Comment id: %s" % comment_id)
        print ("Translation: %s" % english_translation)
        print (json.dumps(spam_json))

        db.update(
            column='spam',
            value=json.dumps(spam_json),
            comment_id=comment_id)

        print_horizontal_rule()


if __name__ == '__main__':
    main()
