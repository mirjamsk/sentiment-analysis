import json
import operator
from copy import deepcopy
from utils.api_utils.sentiment_default_stats import SENTIMENT_DEFAULT_STATS
from utils.parser_utils.id_selection_argument_parser import IdSelectionArgumentParser
from utils.db_utils.sentiment_db import CommentDbConnection, CommentSentimentDbConnection
from utils.print_utils.helpers import print_horizontal_rule, print_sparse_horizontal_rule


def main():
    parser = IdSelectionArgumentParser(description='Script for manually updating real_sentiment of comments')
    parser.parse_args()
    update_real_sentiment_batch(id_selection=parser.id_selection)


def update_real_sentiment_batch(id_selection="", db_name="sentiment_db"):
    """
    Open two database connections:
        - one to fetch comment records
        - another to update comment_sentiment records
    """
    db_comment = CommentDbConnection(db=db_name)
    db_comment.connect()

    db_sentiment = CommentSentimentDbConnection(db=db_name)
    db_sentiment.connect()

    results = db_comment.fetch_all(where=id_selection)
    for row in results:
        print_horizontal_rule()
        print_horizontal_rule()
        comment_id = row[0]
        content = row[1]
        comment_sentiment_row = db_sentiment.fetch_by_comment_id(comment_id)[0]
        english_translation = comment_sentiment_row[2]
        real_sentiment = comment_sentiment_row[3]

        print ("Comment_id: %s" % comment_id)
        print ("Content: %s" % content.encode('utf-8'))
        print ("English translation: %s" % english_translation.encode('utf-8'))

        print_sparse_horizontal_rule()
        determine_and_store_is_mention(
            db=db_sentiment,
            comment_id=comment_id)

        print_sparse_horizontal_rule()
        spam = determine_and_store_spam(
            db=db_sentiment,
            comment_id=comment_id)

        print_sparse_horizontal_rule()
        if spam['is_spam']:
            store_default_real_sentiment(
                db=db_sentiment,
                comment_id=comment_id)
        else:
            determine_and_store_real_sentiment(
                db=db_sentiment,
                comment_id=comment_id,
                real_sentiment=real_sentiment)

    print_horizontal_rule()
    db_sentiment.close()
    db_comment.close()


def determine_and_store_is_mention(comment_id, db):
    is_mention = get_is_mention()
    db.update(
        comment_id=comment_id,
        value=is_mention,
        column='is_mention')
    print ("Updated mention: %s" % ('True' if is_mention else 'False'))


def get_is_mention():
    is_mention = raw_input('Is this comment ONLY a mention? (y/n): ')
    while is_mention.lower() not in ('y', 'n'):
        print("Input needs to be either 'y' or 'n'")
        is_mention = raw_input('Is this comment ONLY a mention? (y/n): ')
    is_mention = 1 if is_mention.lower() == 'y' else 0
    return is_mention


def determine_and_store_spam(comment_id, db):
    spam = get_is_spam()
    db.update(
        comment_id=comment_id,
        value=json.dumps(spam),
        column='spam')
    print ("Updated spam: %s" % json.dumps(spam, indent=2))
    return spam


def get_is_spam():
    spam_json = {'is_spam': True, 'type': ''}
    is_spam = raw_input('Is this comment spam? (y/n): ')
    while is_spam.lower() not in ('y', 'n'):
        print("Input needs to be either 'y' or 'n'")
        is_spam = raw_input('Is this comment spam? (y/n): ')

    spam_json['is_spam'] = True if is_spam.lower() == 'y' else False
    if spam_json['is_spam']:
        spam_json['type'] = raw_input('Enter type? (e.g. url, blank, email, chain, other...): ')

    return spam_json


def store_real_sentiment(comment_id, db_sentiment, real_sentiment):
    db_sentiment.update(
        comment_id=comment_id,
        value=json.dumps(real_sentiment),
        column='real_sentiment')
    print ("Updated real_sentiment: %s" % json.dumps(real_sentiment, indent=2))


def store_default_real_sentiment(db, comment_id):
    real_sentiment = deepcopy(SENTIMENT_DEFAULT_STATS)
    real_sentiment['sentiment_label'] = 'neutral'
    real_sentiment['sentiment_stats']['neutral'] = 1
    store_real_sentiment(
        db_sentiment=db,
        comment_id=comment_id,
        real_sentiment=real_sentiment)


def determine_and_store_real_sentiment(comment_id, db, real_sentiment):
    if 0 and is_json(real_sentiment) and 'sentiment_label' in json.loads(real_sentiment):
        sentiment = json.loads(real_sentiment)['sentiment_label']
        print('Real sentiment already determined: %s' % sentiment)
    else:
        real_sentiment = get_real_sentiment()
        store_real_sentiment(
            db_sentiment=db,
            comment_id=comment_id,
            real_sentiment=real_sentiment)


def get_real_sentiment():
    SENTIMENT_LABELS = {
        'pos': 'positive',
        'neg': 'negative',
        'neu': 'neutral',
        'mix': 'mixed'
    }
    label_choices = set(SENTIMENT_LABELS.keys())
    print ("Determine the real_sentiment:")
    input_sentiment = get_input_label()

    while input_sentiment not in label_choices:
        print("%s not in %s" % (input_sentiment, label_choices))
        input_sentiment = get_input_label()

    if input_sentiment == 'mix':
        real_sentiment = get_mixed_sentiment()
    else:
        real_sentiment = set_single_sentiment(sentiment=SENTIMENT_LABELS[input_sentiment])

    return real_sentiment


def set_single_sentiment(sentiment):
    real_sentiment = deepcopy(SENTIMENT_DEFAULT_STATS)
    real_sentiment['sentiment_label'] = sentiment
    for label in real_sentiment['sentiment_stats'].keys():
        if real_sentiment['sentiment_label'] == label:
            real_sentiment['sentiment_stats'][label] = 1
        else:
            real_sentiment['sentiment_stats'][label] = 0
    return real_sentiment


def get_mixed_sentiment():
    real_sentiment = deepcopy(SENTIMENT_DEFAULT_STATS)

    print('Enter the probabilities for each label (they should sum to 1):')
    get_sentiment_probabilities(real_sentiment)
    print(real_sentiment['sentiment_stats'])
    while sum(real_sentiment['sentiment_stats'].values()) != 1:
        print('The probabilities do not sum up to 1. Try again:')
        get_sentiment_probabilities(real_sentiment)

    real_sentiment['sentiment_label'] = get_most_frequent_label(real_sentiment['sentiment_stats'])
    return real_sentiment


def get_sentiment_probabilities(real_sentiment):
    sentiment_stats = real_sentiment['sentiment_stats']
    for sentiment in sentiment_stats.keys():
        while True:
            try:
                probability = round(float(raw_input(sentiment + ': ')), 4)
                if probability < 0 or probability > 1:
                    raise ValueError
            except ValueError:
                print("The input should be positive decimal number in the range [0,1]")
                print("Please, try again.")
                continue
            else:
                sentiment_stats[sentiment] = probability
                break


def get_input_label():
    return raw_input("pos/neg/neu/mix? ").strip()


def get_most_frequent_label(stats={}):
    stats.pop('total', None)
    return max(stats.items(), key=operator.itemgetter(1))[0]


def is_json(json_str):
    if json_str is None or json_str == '':
        return False
    try:
        json.loads(json_str)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    main()
