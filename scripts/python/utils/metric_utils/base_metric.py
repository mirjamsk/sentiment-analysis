from abc import ABCMeta as _ABCMeta, abstractmethod


class _BaseMetric(object):
    __metaclass__ = _ABCMeta

    @abstractmethod
    def update_stats(self, real_sentiment, api_sentiment):
        pass

    @abstractmethod
    def calculate_stats(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def print_stats(self):
        pass
