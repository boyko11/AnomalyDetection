from flask import Flask
from flask_cors import cross_origin
from service.model_service import ModelService
from service.data_service import DataService

app = Flask(__name__)
modelService = ModelService()


@app.route('/')
@cross_origin()
def get_display_train_data():

	if not modelService.model_trained:
		modelService.train_model()

	display_train_data = modelService.get_train_display_data(num_records=40)

	return display_train_data


@app.route('/new_data_point')
@cross_origin()
def new_data_point():

	rand_data = DataService.generate_test_data(modelService.means, modelService.cov_matrix)

	point_to_return = rand_data[0, :].reshape(1, 3)

	anomaly = modelService.learner.is_anomaly(point_to_return)

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