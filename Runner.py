from service.data_service import DataService
from anomaly_detection_learner import AnomalyDetectionLearner


class Runner:

    def __init__(self):
        self.dimensions = 3
        self.num_records = 100
        self.anomaly_detection_learner = AnomalyDetectionLearner(z_score_anomaly_threshold=3)

    def run(self):

        normal_data = DataService\
            .generate_random_gaussian_data(dimension_means=[0, 1, 2], num_records=self.num_records)
        # train with non-anomalous data
        self.anomaly_detection_learner.train(normal_data)

        # none of the training data should be anomalous
        anomalies_in_normal_data = self.anomaly_detection_learner.is_anomaly(normal_data)

        if not any(anomalies_in_normal_data):
            print("All training data checked out as normal.")
        else:
            print("Some training records registered as anomalous. Perhaps, adjust the z_score_anomaly_threshold.")

        anomalous_data = DataService\
            .generate_random_gaussian_data(dimension_means=[7, 3, 5], num_records=20)

        anomalies_in_anomalous_data = self.anomaly_detection_learner.is_anomaly(anomalous_data)

        if all(anomalies_in_anomalous_data):
            print("All anomalous data checked out as anomalous.")
        else:
            print("Some anomalous records did not check out as anomalous.")


if __name__ == "__main__":

    Runner().run()