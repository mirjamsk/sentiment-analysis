from abc import ABCMeta as _ABCMeta, abstractmethod
from requests import post


class _API(object):
    __metaclass__ = _ABCMeta

    def __init__(self, url, data, sentiment_labels, sentiment_api_column):
        self.url = url
        self.data = data
        self.response = None
        self.SENTIMENT_LABELS = sentiment_labels
        self.sentiment_api_column = sentiment_api_column

    def post(self):
        self.response = post(url=self.url, data=self.data)

    def is_request_successful(self):
        return self.response.status_code == 200

    @abstractmethod
    def set_data(self, text):
        pass

    @abstractmethod
    def get_sentiment(self):
        pass


class ViveknApi(_API):
    def __init__(self):
        SENTIMENT_LABELS = {
            'Positive': 'positive',
            'Negative': 'negative',
            'Neutral' : 'neutral'
        }
        _API.__init__(
            self,
            url='http://sentiment.vivekn.com/api/text/',
            data={'txt': ''},
            sentiment_labels=SENTIMENT_LABELS,
            sentiment_api_column='sentiment_api1')

    def set_data(self, text):
        self.data['txt'] = text

    def get_sentiment(self):
        sentiment = self.response.json()['result']['sentiment']
        return self.SENTIMENT_LABELS[sentiment]

    def __str__(self):
        return 'Vivek API: ' + self.url


class TextProcessingApi(_API):
    def __init__(self):
        SENTIMENT_LABELS = {
          'pos': 'positive',
          'neg': 'negative',
          'neutral': 'neutral'}

        _API.__init__(
            self,
            url='http://text-processing.com/api/sentiment/',
            data={'text': ''},
            sentiment_labels=SENTIMENT_LABELS,
            sentiment_api_column='sentiment_api2')

    def set_data(self, text):
        self.data['text'] = text

    def get_sentiment(self):
        sentiment = self.response.json()['label']
        return self.SENTIMENT_LABELS[sentiment]

    def __str__(self):
        return 'Text-processing API: ' + self.url
