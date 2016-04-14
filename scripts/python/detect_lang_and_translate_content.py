from utils.db_utils.base_db import Database
from utils.db_utils.sentiment_db import CommentDbConnection
from utils.print_utils.helpers import print_horizontal_rule
from utils.api_utils.google_translate_api import GoogleTranslateAPI
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser


def detect_lang_and_translate_content(id_selection="", db_name="sentiment_db"):
    # Open database connections
    # we need two: one for fetch records and another for update records)
    db_comment = CommentDbConnection(db=db_name)
    db_comment.connect()

    db_language = Database(db=db_name)
    db_language.connect()

    api = GoogleTranslateAPI()
    print ('\nUsing GoogleTranslateAPI')
    
    results = db_comment.fetch_all(where=id_selection)

    for row in results:
        print_horizontal_rule()
        comment_id = row[0]
        content = row[1]

        print ("Comment_id: %s" % comment_id)
        print ("Content: %s" % content)

        api.set_text(content)
        api.get()

        if api.is_request_successful():
            print ("Detected language: %s" % api.get_detected_language())
            print ("English translation: %s" % api.get_translation())
            db_language.update(
                table="im_commento_sentiment",
                where="idcommento = %d" % comment_id,
                set={
                    api.language_column: api.get_detected_language(),
                    api.english_translation_column: api.get_translation().replace("'", "\\'")})
        else:
            print("API request was NOT successful: returned %d status code" % api.get_status_code())
            break

    print_horizontal_rule()
    db_comment.close()
    db_language.close()


def main():
    parser = IdSelectionArgumentParser(
        description=
        'Makes api calls to Google to \
        determine the language and the \
        english translation of comments \
        and store the results in a database')

    parser.parse_args()
    detect_lang_and_translate_content(id_selection=parser.id_selection)


if __name__ == '__main__':
    main()
