import numpy as np


class DataService:

    def __init__(self):
        pass

    @staticmethod
    def generate_random_gaussian_data(dimension_means=[0], cov_matrix=[[1]], num_records=1):

        norm_distr_data = np.random.multivariate_normal(dimension_means, cov_matrix, 100)

        return norm_distr_data
    
    @staticmethod
    def generate_random_uniform_data(means):
        
        rand_data_dim1 = np.random.uniform(low=means[0] - 3, high=means[0] + 3, size=30)
        rand_data_dim2 = np.random.uniform(low=means[1] - 3, high=means[1] + 3, size=30)
        rand_data_dim3 = np.random.uniform(low=means[2] - 3, high=means[2] + 3, size=30)
        rand_data = np.array([
            rand_data_dim1, rand_data_dim2, rand_data_dim3
        ]).T

        sure_anomalies = np.array([
                [4, 2, 5],
                [4.5, 2.5, 4.75],
                [3, 2.5, 5.25],
                [4.5, 9, 10.5],
                [4.5, 9.5, 10],
                [-1, 9, 10],
                [-1, 8.5, 10.5],
                [0, 8, 10.25],
            ])

        rand_data = np.vstack((rand_data, sure_anomalies))

        return rand_data
