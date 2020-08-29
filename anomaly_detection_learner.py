import numpy as np


class AnomalyDetectionLearner:

    def __init__(self):

        self.means = None
        self.covariance_matrix = None
        self.train_records_fifth_smallest_probability = None

    def train(self, feature_data):

        self.means = np.mean(feature_data, axis=0)
        self.covariance_matrix = np.cov(feature_data.T)
        probabilities_of_records = self.calculate_probability_of_data(feature_data)
        self.train_records_fifth_smallest_probability = np.partition(probabilities_of_records, 4)[4]

    def calculate_probability_of_data(self, feature_data):

        part1 = 1.0 / (((2 * np.pi) ** (feature_data.shape[1] / 2.0)) * np.linalg.det(self.covariance_matrix) ** 0.5)
        record_minus_means = feature_data - self.means
        part2 = np.exp(-0.5 * np.dot(np.dot(record_minus_means, np.linalg.inv(self.covariance_matrix)),
                                     record_minus_means.T))

        return (part1 * part2).diagonal()

    def is_anomaly(self, data):

        probability_of_data = self.calculate_probability_of_data(data)

        return probability_of_data < self.train_records_fifth_smallest_probability
