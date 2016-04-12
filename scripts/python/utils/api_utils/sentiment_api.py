from abc import ABCMeta as _ABCMeta, abstractmethod
from base_api import BaseAPI


class _SentimentAPI(BaseAPI):
    __metaclass__ = _ABCMeta

    def __init__(self, url='', data={}, params={},  sentiment_api_column=''):
        BaseAPI.__init__(
            self,
            url=url,
            data=data,
            params=params)

        self.sentiment_api_column = sentiment_api_column

    @abstractmethod
    def set_data(self, text):
        pass

    @abstractmethod
    def get_sentiment(self):
        pass


class ViveknAPI(_SentimentAPI):
    def __init__(self):
        self.SENTIMENT_LABELS = {
            'Positive': 'positive',
            'Negative': 'negative',
            'Neutral' : 'neutral'
        }
        _SentimentAPI.__init__(
            self,
            url='http://sentiment.vivekn.com/api/text/',
            data={'txt': ''},
            sentiment_api_column='sentiment_api1')

    def set_data(self, text):
        self.data['txt'] = text

    def get_sentiment(self):
        sentiment = self.response.json()['result']['sentiment']
        return self.SENTIMENT_LABELS[sentiment]

    def __str__(self):
        return 'Vivek API: ' + self.url


class TextProcessingAPI(_SentimentAPI):
    def __init__(self):
        self.SENTIMENT_LABELS = {
          'pos': 'positive',
          'neg': 'negative',
          'neutral': 'neutral'}

        _SentimentAPI.__init__(
            self,
            url='http://text-processing.com/api/sentiment/',
            data={'text': ''},
            sentiment_api_column='sentiment_api2')

    def set_data(self, text):
        self.data['text'] = text

    def get_sentiment(self):
        sentiment = self.response.json()['label']
        return self.SENTIMENT_LABELS[sentiment]

    def __str__(self):
        return 'Text-processing API: ' + self.url

