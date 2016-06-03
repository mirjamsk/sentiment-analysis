import json
from copy import deepcopy
from utils.spam_utils.akismet_spam import AkismetSpam
from utils.spam_utils.blog_spam import BlogSpam
from utils.print_utils.helpers import print_horizontal_rule
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser
from utils.db_utils.sentiment_db import CommentSpamDbConnection, CommentSentimentDbConnection, CommentDbConnection


def main():
    API_choices = {
        AkismetSpam.__name__: AkismetSpam,
        BlogSpam.__name__: BlogSpam}

    parser = IdSelectionArgumentParser(
        description =
        'Uses Akismet lib to determine whether \
         the english translation or the comments\
         in original language are spam or not, & \
         it stores the results in the database')

    parser.add_argument_with_choices(
        '-api',
        required=True,
        choices=API_choices.keys(),
        help='Choose from the listed api options')

    spam = parser.add_mutually_exclusive_group(required=True)
    spam.add_argument('--en', dest='use_en', action='store_true')
    spam.add_argument('--ol', dest='use_en', action='store_false')

    parser.parse_args()
    detect_spam(
        use_en=parser.args.use_en,
        id_selection=parser.id_selection,
        api=API_choices.get(parser.args.api)())


def detect_spam(api=None, id_selection="", use_en="", db_name="sentiment_db"):
    """
    Open three database connections:
        - one to fetch comment records
        - one to fetch the english translation
        - another to update comment_spam records
    """
    db_spam = CommentSpamDbConnection(db=db_name)
    db_spam.connect()

    db_comment = CommentDbConnection(db=db_name)
    db_comment.connect()

    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    results = db_comment.fetch_all(where=id_selection)

    spam_json = {
        'is_spam': False,
        'type': 'other'
    }

    for row in results:
        print_horizontal_rule()
        comment_id = row[0]
        comment = row[1]
        post_id = row[2]
        comment_author = row[3]
        english_translation = db_sentiment.fetch_by_comment_id(comment_id)[0][2]
        content = english_translation if use_en else comment

        content_description = 'English translation' if use_en else 'Original content'
        print ("Comment_id: %s" % comment_id)
        print ("%s: %s" % (content_description, content))
        if not use_en:
            print ("English translation: %s" % english_translation)

        spam = deepcopy(spam_json)
        spam['is_spam'] = api.is_spam(
            content=content,
            post_id=post_id,
            comment_author=comment_author)

        print ("%s  detected as: %s spam" % (content_description, '' if spam['is_spam'] else 'NOT'))

        db_spam.update(
            comment_id=comment_id,
            column=api.get_db_column(use_en),
            value=json.dumps(spam))

    print_horizontal_rule()
    db_comment.close()
    db_spam.close()


if __name__ == '__main__':
    main()
