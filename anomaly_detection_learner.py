import numpy as np


class AnomalyDetectionLearner:

    def __init__(self, z_score_anomaly_threshold=3):
        self.means = None
        self.covariance_matrix = None
        self.z_score_anomaly_threshold = z_score_anomaly_threshold
        self.train_records_probabilities_mean = None
        self.train_records_probabilities_st_dev = None
        self.train_records_min_z_score = None

    def train(self, feature_data):
        self.means = np.mean(feature_data, axis=0)
        self.covariance_matrix = np.cov(feature_data.T)

        probabilities_of_records = self.calculate_probability_of_data(feature_data)

        # fit a normal distribution of probabilities for the training records
        self.train_records_probabilities_mean = np.mean(probabilities_of_records)
        self.train_records_probabilities_st_dev = np.std(probabilities_of_records)
        z_scores = (probabilities_of_records - self.train_records_probabilities_mean) / \
                   self.train_records_probabilities_st_dev
        self.train_records_min_z_score = np.min(z_scores)

    def calculate_probability_of_data(self, feature_data):
        part1 = 1.0 / (((2 * np.pi) ** (feature_data.shape[1] / 2.0)) * np.linalg.det(self.covariance_matrix) ** 0.5)
        record_minus_means = feature_data - self.means
        part2 = np.exp(-0.5 * np.dot(np.dot(record_minus_means, np.linalg.inv(self.covariance_matrix)),
                                     record_minus_means.T))

        return (part1 * part2).diagonal()

    def is_anomaly(self, data):
        probability_of_data = self.calculate_probability_of_data(data)

        z_score = (probability_of_data - self.train_records_probabilities_mean) / \
                  self.train_records_probabilities_st_dev

        return z_score < self.train_records_min_z_score
