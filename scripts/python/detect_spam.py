from utils.db_utils.base_db import Database
from utils.db_utils.sentiment_db import CommentSpamDbConnection, PostDbConnection, CommentDbConnection
from utils.print_utils.helpers import print_horizontal_rule
from utils.api_utils.akismet_spam_api import AkismetSpamAPI
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser


def detect_spam(id_selection="", db_name1="spam_db", db_name2="sentiment_db"):
    # Open database connections
    # we need two: one for fetch records and another for update records)
    db_comment_spam = CommentSpamDbConnection(db=db_name1)
    db_comment_spam.connect()

    db_comment = CommentDbConnection(db=db_name2)
    db_comment.connect()

    #db_language = Database(db=db_name1)
    #db_language.connect()

    db_post = PostDbConnection(db=db_name2)
    db_post.connect()

    api = AkismetSpamAPI()
    print ('\nUsing AkismetSpamAPI')

    results = db_comment_spam.fetch_all(where=id_selection)

    for row in results:
        print_horizontal_rule()
        comment_id = row[1]
        content = row[2]

        print ("Comment_id: %s" % comment_id)
        print ("Content: %s" % content)


        result_comment = db_comment.fetch_by_id(comment_id)
        #print (result_comment[0][2])
        result_post = db_post.fetch_by_id(result_comment[0][2])

        post_url = result_post[0][2]

        print ("Comment: " + content + ", api result spam is: " + str(api.spam_check(content, post_url)))

        # api.set_text(content)
        # api.get()

        # if api.is_request_successful():
        #     print ("Detected language: %s" % api.get_detected_language())
        #     print ("English translation: %s" % api.get_translation())
        #     db_language.update(
        #         table="im_commento_sentiment",
        #         where="idcommento = %d" % comment_id,
        #         set={
        #             api.language_column: api.get_detected_language(),
        #             api.english_translation_column: api.get_translation().replace("'", "\\'")})
        # else:
        #     print("API request was NOT successful: returned %d status code" % api.get_status_code())
        #     break

    print_horizontal_rule()
    db_comment.close()
    db_post.close()
    db_comment_spam.close()
    #db_language.close()


def main():
    parser = IdSelectionArgumentParser(
        description=
        'Makes api calls to Akismet to \
        determine the language and the \
        english translation of comments \
        and store the results in a database')

    parser.parse_args()
    detect_spam(id_selection=parser.id_selection)


if __name__ == '__main__':
    main()
