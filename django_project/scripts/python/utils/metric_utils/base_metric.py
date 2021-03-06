import json
from copy import deepcopy

_default_stats = {
    'positive': 0,
    'negative': 0,
    'neutral': 0
}


class BaseMetric(object):
    """
    Corresponding labels map to statistic terms:
     - TP: True Positives ( correctly predicted labels)
     - FN: False Negatives ( # of times it didn't predict the label when it should have )
     - FP: False Positive ( # of times it predicted the label when it shouldn't have )

    """
    def __init__(self):
        self.TP = deepcopy(_default_stats)
        self.FP = deepcopy(_default_stats)
        self.FN = deepcopy(_default_stats)

        self.total_sentiment_predictions = 0
        self.correct_sentiment_predictions = 0

    def update_stats(self, real_sentiment, predicted_sentiment):
        self.total_sentiment_predictions += 1
        if real_sentiment['sentiment_label'] == predicted_sentiment['sentiment_label']:
            self.TP[predicted_sentiment['sentiment_label']] += 1
        else:
            self.FN[real_sentiment['sentiment_label']] += 1
            self.FP[predicted_sentiment['sentiment_label']] += 1

    def clear_stats(self):
        self.TP = deepcopy(_default_stats)
        self.FP = deepcopy(_default_stats)
        self.FN = deepcopy(_default_stats)

        self.total_sentiment_predictions = 0
        self.correct_sentiment_predictions = 0

    def calculate_stats(self):
        pass

    def get_stats(self):
        pass

    def get_db_safe_stats(self):
        pass

    def print_stats(self):
        print("True positives: %s " % self.TP)
        print("False negatives: %s " % self.FN)
        print("False positives: %s " % self.FP)
        print("Total sentiment predictions: %d " % self.total_sentiment_predictions)

    def print_real_sentiment_distribution(self):
        distribution = deepcopy(_default_stats)
        for sentiment in distribution.keys():
            distribution[sentiment] = self.TP[sentiment] + self.FN[sentiment]
            distribution[sentiment] /= float(self.total_sentiment_predictions)
            distribution[sentiment] = 100 * round(distribution[sentiment], 4)
            distribution[sentiment] = str(distribution[sentiment]) + '%'

        print('Real sentiment distribution %s' % json.dumps(distribution, indent=2))
