from service.data_service import DataService
from anomaly_detection_learner import AnomalyDetectionLearner
import numpy as np
from service.plot_service import PlotService


class Runner:

    def __init__(self):

        self.dimensions = 3
        self.num_records = 100
        self.anomaly_detection_learner = AnomalyDetectionLearner()

    def run(self):

        means = [2, 5, 8]
        cov_matrix = [
            [  1, .75, .25],
            [.75,   2,  .5],
            [.25,  .5, 1.5]
        ]

        three_d_norm_distr_data = DataService\
            .generate_random_gaussian_data(dimension_means=means, cov_matrix=cov_matrix, num_records=self.num_records)

        self.anomaly_detection_learner.train(three_d_norm_distr_data)

        rand_data = DataService.generate_random_uniform_data(means)
        rand_data_anom_results = self.anomaly_detection_learner.is_anomaly(rand_data)

        rand_data_anom = rand_data[rand_data_anom_results, :]
        rand_data_non_anom = rand_data[np.logical_not(rand_data_anom_results), :]

        PlotService.plot3d_scatter_normal_and_anomalous(three_d_norm_distr_data, rand_data_anom, rand_data_non_anom)


if __name__ == "__main__":

    Runner().run()