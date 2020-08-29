from flask import Flask
from flask_cors import cross_origin
from service.data_service import DataService
from anomaly_detection_learner import AnomalyDetectionLearner
import numpy as np

app = Flask(__name__)

anomaly_learner = AnomalyDetectionLearner()
means = [2, 5, 8]
rand_data_points_count = 0
rand_data = DataService.generate_random_uniform_data(means)


@app.route('/')
@cross_origin()
def train_data():

	global means
	global anomaly_learner

	cov_matrix = [
		[1, .75, .25],
		[.75, 2, .5],
		[.25, .5, 1.5]
	]

	three_d_norm_distr_data = DataService \
		.generate_random_gaussian_data(dimension_means=means, cov_matrix=cov_matrix, num_records=100)
	anomaly_learner.train(three_d_norm_distr_data)

	probabilities_of_records = anomaly_learner.calculate_probability_of_data(three_d_norm_distr_data)
	train_display_indices = np.argwhere(probabilities_of_records > anomaly_learner.train_records_twentieth_smallest_probability).flatten()
	train_display_indices = np.random.choice(train_display_indices, 20)

	train_data = three_d_norm_distr_data[train_display_indices, :]

	train_data_to_plot = {
			'x': train_data[:, 0].tolist(),
			'y': train_data[:, 1].tolist(),
			'z': train_data[:, 2].tolist()
	}

	data_to_return = {
		'train_data': train_data_to_plot
	}


	return data_to_return

@app.route('/new_data_point')
@cross_origin()
def new_data_point():
	global rand_data_points_count
	global rand_data
	global anomaly_learner

	point_to_return = rand_data[rand_data_points_count, :].reshape(1, 3)
	rand_data_points_count += 1
	if rand_data_points_count == 30:
		rand_data_points_count = 0

	anomaly = anomaly_learner.is_anomaly(point_to_return)

	data_to_return = {
		'anomaly': bool(anomaly[0]),
		'x': point_to_return[0, 0],
		'y': point_to_return[0, 1],
		'z': point_to_return[0, 2]
	}

	return data_to_return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# nohup python anomaly_controller.py > log.txt 2>&1 &