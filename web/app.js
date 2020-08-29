var App = (function() {

	let number_test_points_counter = 0

	let check_and_render_new_data = function(data) {

	if(number_test_points_counter > 20) {
		return;
	}

	let data_plus_new_data = data;
	fetch(`http://127.0.0.1:5000/new_data_point`)
	   .then(response => response.json())
	   .then(json => {
			let new_data_point = json;
			if (new_data_point.anomaly) {
				data_plus_new_data.test_data_anomaly.x.push(new_data_point.x);
				data_plus_new_data.test_data_anomaly.y.push(new_data_point.y);
				data_plus_new_data.test_data_anomaly.z.push(new_data_point.z);
			} else {
				data_plus_new_data.test_data_non_anomaly.x.push(new_data_point.x);
				data_plus_new_data.test_data_non_anomaly.y.push(new_data_point.y);
				data_plus_new_data.test_data_non_anomaly.z.push(new_data_point.z);
			}

			App.service.PlotService.plot_3D_scatter(data_plus_new_data);
			number_test_points_counter++;

			setTimeout(function() {
					check_and_render_new_data(data_plus_new_data)
					console.log('Initial Rendered.')
			}, 2000);
	   });


	};

	const start = function() {

		fetch(`http://127.0.0.1:5000`)
		   .then(response => response.json())
		   .then(json => {
				data = json;
				data.test_data_anomaly = { x: [], y: [], z: [] };
				data.test_data_non_anomaly = { x: [], y: [], z: [] };

				App.service.PlotService.plot_3D_scatter(data);

				setTimeout(function() {
					check_and_render_new_data(data)
					console.log('Initial Rendered.')
				}, 2000);

		   });
	};


	return {
		start: start
	}

})();

