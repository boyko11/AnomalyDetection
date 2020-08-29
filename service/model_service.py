from service.data_service import DataService
from anomaly_detection_learner import AnomalyDetectionLearner
import numpy as np


class ModelService:

    def __init__(self):
        self.params = {}
        self.model_trained = False
        self.means = [2, 5, 8]
        self.cov_matrix = [
            [1, .75, .25],
            [.75, 2, .5],
            [.25, .5, 1.5]
        ]
        self.learner = AnomalyDetectionLearner()
        self.train_display_indices = None
        self.train_data = None

    def train_model(self):

        three_d_norm_distr_data = DataService \
            .generate_random_gaussian_data(dimension_means=self.means, cov_matrix=self.cov_matrix, num_records=200)
        self.train_data = three_d_norm_distr_data
        self.learner.train(three_d_norm_distr_data)
        self.model_trained = True

        probabilities_of_records = self.learner.calculate_probability_of_data(three_d_norm_distr_data)
        self.train_display_indices = np.argwhere(
            probabilities_of_records > self.learner.train_records_twentieth_smallest_probability).flatten()

    def get_train_display_data(self, num_records=35):

        train_display_indices = np.random.choice(self.train_display_indices, num_records)

        train_data = self.train_data[train_display_indices, :]

        train_data_to_plot = {
            'x': train_data[:, 0].tolist(),
            'y': train_data[:, 1].tolist(),
            'z': train_data[:, 2].tolist()
        }

        data_to_return = {
            'train_data': train_data_to_plot
        }

        return data_to_return
