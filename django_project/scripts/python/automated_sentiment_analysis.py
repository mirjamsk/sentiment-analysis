import sys
import time
import codecs
from utils.db_utils.base_db import Database
from predict_comment_sentiment import run_sentiment_api_batch
from translate_comments import detect_lang_and_translate_content
from mark_if_comment_has_emoji import mark_if_comment_has_emojis
from utils.db_utils.helpers import build_id_selection_condition
from utils.api_utils.sentiment_api import TextProcessingAPI, ViveknAPI, IndicoAPI, IndicoHqAPI
from update_sentiment_prediction_with_emojis import update_sentiment_emoji_stats

STDOUT = sys.stdout


def log(message='', indent=3):
    print >> STDOUT, '-' * indent, message


def main():
    original_and_english_APIs = (TextProcessingAPI, ViveknAPI)
    english_only_APIs = (IndicoAPI, IndicoHqAPI)
    db_name = "sentiment_db"

    db = Database(db=db_name)
    db.connect()

    results = db.fetch_all(
        select='id',
        from_clause='im_commento',
        where='id NOT IN ( \
             SELECT idcommento \
             FROM im_commento_sentiment)',
        order_by='id')

    comment_ids = [str(row[0]) for row in results]
    log('Found these comments without a sentiment record: %s' % comment_ids)

    if len(comment_ids) == 0:
        log('No new comments to analyze')
        db.close()
        return

    log(indent=3,
        message='For each of the comments with id in %s:' % comment_ids)
    log(indent=6,
        message='Inserting a record in im_commento_sentiment...')

    for id in comment_ids:
        db.insert(table='im_commento_sentiment', column_value={'idcommento': id})
        db.insert(table='im_commento_sentiment_emoji', column_value={'idcommento': id})
    db.close()

    log(indent=6,
        message='Translating the comments with Google API...')

    id_selection = build_id_selection_condition(id_equals=comment_ids)
    detect_lang_and_translate_content(
        db_name=db_name,
        id_selection=id_selection)

    log(indent=6,
        message='Marking if the comments have emojis...')
    mark_if_comment_has_emojis(
        db_name=db_name,
        id_selection=id_selection)

    for api in original_and_english_APIs:
        for original_language in (True, False):
            log(indent=6,
                message='For %s and %s language:' % (api.__name__, 'original' if original_language else 'english'))
            log(indent=9,
                message='Predicting sentiment and updating im_commento_sentiment table')

            run_sentiment_api_batch(
                db_name=db_name,
                api=api(original_language),
                id_selection=id_selection,
                original_language=original_language)

            log(indent=9,
                message='Detecting emojis and updating im_commento_sentiment_emoji table')

            update_sentiment_emoji_stats(
                api=api(original_language),
                id_selection=id_selection,
                db_name=db_name)

    for api in english_only_APIs:
        log(indent=6,
            message='For %s and %s language:' % (api.__name__, 'english'))

        log(indent=9,
            message='Predicting sentiment and updating im_commento_sentiment table')

        run_sentiment_api_batch(
            api=api(),
            db_name=db_name,
            id_selection=id_selection,
            original_language=False)

        log(indent=9,
            message='Detecting emojis and updating im_commento_sentiment_emoji table')

        update_sentiment_emoji_stats(
            api=api(),
            db_name=db_name,
            id_selection=id_selection)

    #invoke update post sentiment!!!!
    # evaluating accuracy should be done on real_sentiment input


if __name__ == '__main__':
    timestamp = int(time.time())
    sys.stderr = codecs.open('log/err/automated_sentiment_error_%d.log' % timestamp, 'w', 'utf8')
    sys.stdout = codecs.open('log/automated_sentiment_analysis_%d.log' % timestamp, 'w', 'utf8')
    log(indent=0,
        message='\n*** You can find a more detailed transcript of operations in the log/ directory ***\n')
    main()
