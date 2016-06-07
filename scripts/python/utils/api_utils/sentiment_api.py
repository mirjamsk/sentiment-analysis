import operator
from copy import deepcopy
from abc import ABCMeta as _ABCMeta, abstractmethod
from base_api import BaseAPI
from .sentiment_default_stats import SENTIMENT_DEFAULT_STATS


class _SentimentAPI(BaseAPI):
    __metaclass__ = _ABCMeta

    def __init__(self, url='', data={}, params={},  sentiment_api_column=''):
        self.sentiment_stats = deepcopy(SENTIMENT_DEFAULT_STATS)
        BaseAPI.__init__(
            self,
            url=url,
            data=data,
            params=params)

        self.sentiment_api_column = sentiment_api_column

    def clear_sentiment_stats(self):
        self.sentiment_stats['sentiment_label'] = ''
        for sentiment in self.sentiment_stats['sentiment_stats'].keys():
            self.sentiment_stats['sentiment_stats'][sentiment] = 0

    def get_sentiment_stats(self):
        return self.sentiment_stats

    @abstractmethod
    def set_data(self, text):
        pass

    @abstractmethod
    def update_sentiment_stats(self):
        pass

    @abstractmethod
    def update_emoji_sentiment_stats(self, emoji_stats=[]):
        pass

    @staticmethod
    def get_most_frequent_label(stats):
        stats.pop('total', None)
        return max(stats.items(), key=operator.itemgetter(1))[0]


class ViveknAPI(_SentimentAPI):
    """
    ViveknAPI's response.json() returns: {
        "result": {
            "sentiment": "Positive",
            "confidence" : 73.22451
        }
    }
    """
    def __init__(self, lang='en'):
        self.SENTIMENT_LABELS = {
            'Positive': 'positive',
            'Negative': 'negative',
            'Neutral' : 'neutral'
        }
        _SentimentAPI.__init__(
            self,
            url='http://sentiment.vivekn.com/api/text/',
            data={'txt': ''},
            sentiment_api_column='sentiment_api1_en' if lang == 'en' else 'sentiment_api1')

    def set_data(self, text):
        self.data['txt'] = text

    def update_sentiment_stats(self):
        self.clear_sentiment_stats()
        sentiment = self.response.json()['result']['sentiment']
        sentiment = self.SENTIMENT_LABELS[sentiment]
        confidence = round(float(self.response.json()['result']['confidence']) * 0.01, 3)

        self.sentiment_stats['sentiment_label'] = sentiment
        self.sentiment_stats['sentiment_stats'][sentiment] = confidence

    def update_emoji_sentiment_stats(self, emoji_stats=[]):
        sentiment_stats = self.sentiment_stats['sentiment_stats']
        for emoji in emoji_stats:
            for label in self.SENTIMENT_LABELS.values():
                sentiment_stats[label] += emoji[label]

        norm = sum(sentiment_stats.values())
        for label in self.SENTIMENT_LABELS.values():
            sentiment_stats[label] = round(sentiment_stats[label]/norm, 3)

        self.sentiment_stats['sentiment_label'] = self.get_most_frequent_label(deepcopy(sentiment_stats))

    def __str__(self):
        return 'Vivek API: ' + self.url


class TextProcessingAPI(_SentimentAPI):
    """
    TextProcessingAPI's response.json() returns: {
        "label": "neg",
        "probability": {
            "pos": 0.31153694518214375,
            "neg": 0.68846305481785608,
            "neutral": 0.3863760999470,
        }
    }
    """
    def __init__(self, lang='en'):
        self.SENTIMENT_LABELS = {
          'pos': 'positive',
          'neg': 'negative',
          'neutral': 'neutral'}

        _SentimentAPI.__init__(
            self,
            url='http://text-processing.com/api/sentiment/',
            data={'text': ''},
            sentiment_api_column='sentiment_api2_en' if lang == 'en' else 'sentiment_api2')

    def set_data(self, text):
        self.data['text'] = text

    def update_sentiment_stats(self):
        sentiment = self.response.json()['label']
        sentiment = self.SENTIMENT_LABELS[sentiment]

        self.sentiment_stats['sentiment_label'] = sentiment
        self.sentiment_stats['sentiment_stats']['positive'] = round(float(self.response.json()['probability']['pos']), 3)
        self.sentiment_stats['sentiment_stats']['negative'] = round(float(self.response.json()['probability']['neg']), 3)
        self.sentiment_stats['sentiment_stats']['neutral'] = round(float(self.response.json()['probability']['neutral']), 3)

    def update_emoji_sentiment_stats(self, emoji_stats=[]):
        sentiment_stats = self.sentiment_stats['sentiment_stats']
        for emoji in emoji_stats:
            for label in self.SENTIMENT_LABELS.values():
                sentiment_stats[label] += emoji[label]

        norm = sum(sentiment_stats.values())
        for label in self.SENTIMENT_LABELS.values():
            sentiment_stats[label] = round(sentiment_stats[label] / norm, 3)

        self.sentiment_stats['sentiment_label'] = self.get_most_frequent_label(deepcopy(sentiment_stats))

    def __str__(self):
        return 'Text-processing API: ' + self.url


class _IndicoAPI(_SentimentAPI):
    """
    IndicoAPI's response.json() returns positivity probability: {
        "results": 0.3468102081511113
    }
    """
    def __init__(self, url, ApiKey, sentiment_api_column):
        _SentimentAPI.__init__(self,
            url=url + ApiKey,
            data={'language': 'english', 'data': ''},
            sentiment_api_column=sentiment_api_column)

    def set_data(self, text):
        self.data['data'] = text

    def update_sentiment_stats(self):
        self.clear_sentiment_stats()
        positive_probability = round(float(self.response.json()['results']), 3)
        self.sentiment_stats['sentiment_stats']['positive'] = positive_probability
        self.sentiment_stats['sentiment_stats']['negative'] = round(1.0 - positive_probability, 3)
        self.sentiment_stats['sentiment_label'] = self.get_sentiment(positive_probability)

    def get_sentiment(self, positive_probability):
        if positive_probability >= 0.5:
            return 'positive'
        else:
            return 'negative'

    def update_emoji_sentiment_stats(self, emoji_stats=[]):
        sentiment_stats = self.sentiment_stats['sentiment_stats']
        for emoji in emoji_stats:
            sentiment_stats['positive'] += emoji['sentiment_score']
            sentiment_stats['positive'] = min(sentiment_stats['positive'], 1.0)
            sentiment_stats['positive'] = max(sentiment_stats['positive'], 0)
        sentiment_stats['negative'] = 1.0 - sentiment_stats['positive']

        self.sentiment_stats['sentiment_label'] = self.get_most_frequent_label(deepcopy(sentiment_stats))

    def __str__(self):
        return 'Indico API: ' + self.url


class IndicoAPI(_IndicoAPI):
    def __init__(self):
        _IndicoAPI.__init__(
            self,
            url='http://apiv2.indico.io/sentiment?key=',
            ApiKey='fc1f6326eadb01b3f71b41295336516a',
            sentiment_api_column='sentiment_api3')


class IndicoHqAPI(_IndicoAPI):
    def __init__(self):
        _IndicoAPI.__init__(
            self,
            url='https://apiv2.indico.io/sentimenthq?key=',
            ApiKey='9b0d19c33f87ff807dfe344378d9a73d',
            sentiment_api_column='sentiment_api4')
