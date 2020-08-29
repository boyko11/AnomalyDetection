var App = App || {};
App.service = App.service || {};
App.service.PlotService = (function() {

	var plot_3D_scatter = function( data ) {

		//credit - https://plotly.com/javascript/3d-scatter-plots/

		console.log("Data:")
		console.log(data)

		let train_data = {
			x: data.train_data.x,
			y: data.train_data.y,
			z: data.train_data.z,
			mode: 'markers',
			marker: {
				size: 12,
				line: {
					color: 'rgba(217, 217, 217, 0.14)',
					width: 0.5
				},
				opacity: 0.8
			},
			type: 'scatter3d'
		};

		let test_data_anomaly = {
			x: data.test_data_anomaly.x,
			y: data.test_data_anomaly.y,
			z: data.test_data_anomaly.z,
			mode: 'markers',
			marker: {
				size: 12,
				line: {
					color: 'rgba(255, 66, 66, 0.14)',
					width: 0.5
				},
				opacity: 0.8
			},
			type: 'scatter3d'
		};

		let test_data_non_anomaly = {
			x: data.test_data_non_anomaly.x,
			y: data.test_data_non_anomaly.y,
			z: data.test_data_non_anomaly.z,
			mode: 'markers',
			marker: {
				size: 12,
				line: {
					color: 'rgba(152, 231, 126, 0.14)',
					width: 0.5
				},
				opacity: 0.8
			},
			type: 'scatter3d'
		};

		let plotly_data = [train_data, test_data_anomaly, test_data_non_anomaly];
		let layout = {
			margin: {
				l: 0,
				r: 0,
				b: 0,
				t: 0
			  }
		};

		Plotly.newPlot('chart_container', plotly_data, layout);
	};


	return {
		plot_3D_scatter: plot_3D_scatter
	}

})();

