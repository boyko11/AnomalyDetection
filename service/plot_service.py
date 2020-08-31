from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d


class PlotService:

    def __init__(self):
        pass

    @staticmethod
    def plot3d_scatter(data, labels, marker='o', title=''):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], marker=marker)

        ax.set_xlabel(labels[0])
        ax.set_ylabel(labels[1])
        ax.set_zlabel(labels[2])

        plt.title(title)

        plt.show()

    @staticmethod
    def plot3d_scatter_normal_and_anomalous(normal_data, rand_anomalous_data, rand_non_anomalous_data,
                                            labels=['x', 'y', 'z'], marker1='o',
                                            marker2='o', marker3='o', color1='#0099ff', color2='r', color3='g',
                                            title='Normal And Anomalous'):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(normal_data[:, 0], normal_data[:, 1], normal_data[:, 2], marker=marker1, label="Normal", c=color1)
        ax.scatter(rand_anomalous_data[:, 0], rand_anomalous_data[:, 1], rand_anomalous_data[:, 2], marker=marker2,
                   label="Rand Anomalous", c=color2)
        ax.scatter(rand_non_anomalous_data[:, 0], rand_non_anomalous_data[:, 1], rand_non_anomalous_data[:, 2],
                   marker=marker3, label="Rand Non-Anomalous", c=color3)

        ax.set_xlabel(labels[0])
        ax.set_ylabel(labels[1])
        ax.set_zlabel(labels[2])

        ax.legend()

        plt.title(title)

        plt.show()