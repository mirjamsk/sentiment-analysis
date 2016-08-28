from base_metric import BaseMetric
from specific_metrics import AccuracyMetric, RecallMetric, PrecisionMetric

class Metric(object):
    def __init__(self, metrics):
        self.base_metric = BaseMetric()
        _metric = {
            PrecisionMetric.metric_name(): PrecisionMetric,
            AccuracyMetric.metric_name(): AccuracyMetric,
            RecallMetric.metric_name(): RecallMetric
        }
        self.metric = {}
        for metric_name in metrics:
            self.metric[metric_name] = _metric[metric_name]()

    def update_stats(self, real_sentiment, predicted_sentiment):
        self.base_metric.update_stats(real_sentiment, predicted_sentiment)
        for metric in self.metric.values():
            metric.TP = self.base_metric.TP
            metric.FP = self.base_metric.FP
            metric.FN = self.base_metric.FN
            metric.total_sentiment_predictions = self.base_metric.total_sentiment_predictions
            metric.correct_sentiment_predictions = self.base_metric.correct_sentiment_predictions

    def clear_stats(self):
        self.base_metric.clear_stats()
        for metric in self.metric.values():
            metric.clear_stats()

    def calculate_stats(self):
        for metric in self.metric.values():
            metric.calculate_stats()

    def get_stats(self, metric_name):
        self.metric[metric_name].get_stats()

    def get_db_safe_stats(self, metric_name):
        return self.metric[metric_name].get_db_safe_stats()

    def print_stats(self):
        self.base_metric.print_stats()
        for metric in self.metric.values():
            metric.print_stats()

    def print_real_sentiment_distribution(self):
        self.base_metric.print_real_sentiment_distribution()

    def get_db_column(self, metric_name, consider_spam):
        return self.metric[metric_name].get_db_column(consider_spam)
