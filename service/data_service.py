import numpy as np


class DataService:

    def __init__(self):
        pass

    @staticmethod
    def generate_random_gaussian_data(dimension_means=[0], num_records=1):

        st_dev = 1.0
        data = np.empty(shape=(num_records, len(dimension_means)), dtype=np.float64)

        for index, dimension_mean in enumerate(dimension_means):
            this_feature_data = np.random.normal(dimension_mean, st_dev, num_records)
            data[:, index] = this_feature_data

        return data
