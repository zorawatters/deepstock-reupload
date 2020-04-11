import keras_model
import argparse
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.saved_model import tag_constants
import mlflow.tensorflow
from builtins import int
from time import time
import os
import subprocess
from googleapiclient import discovery
from google.oauth2 import service_account

#mlflow.tensorflow.autolog()

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--ticker', default='')
	parser.add_argument('--num-epochs', type=int, default='10')
	parser.add_argument('--batch-size', type=int, default='64')
	parser.add_argument('--deploy', action='store_true', default=False)
	args, _ = parser.parse_known_args()
	return args

def _mlflow_log_metrics(metrics, metric_name):
  for epoch, metric in enumerate(metrics[metric_name], 1): 
  	mlflow.log_metric(metric_name, metric, step=epoch)

def train_and_evaluate(args):
	start_time = time()

	df = pd.read_csv('https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv')

	df['PrevClose'] = df['close'].shift(1)

	df['Return'] = (df['close'] - df['PrevClose']) / df['PrevClose']

	input_data = df[['open', 'high', 'low', 'close', 'volume']].values
	targets = df['Return'].values

	T = 10
	D = input_data.shape[1]
	N = len(input_data) - T

	Ntrain = len(input_data) * 2 // 3
	scaler = StandardScaler()
	scaler.fit(input_data[:Ntrain + T - 1])
	input_data = scaler.transform(input_data)

	x_train = np.zeros((Ntrain, T, D))
	y_train = np.zeros(Ntrain)

	for t in range(Ntrain):
		x_train[t, :, :] = input_data[t:t+T]
		y_train[t] = (targets[t+T] > 0)

	x_test = np.zeros((N - Ntrain, T, D))
	y_test = np.zeros(N - Ntrain)

	for u in range(N - Ntrain):
	  # u counts from 0...(N - Ntrain)
	  # t counts from Ntrain...N
	  t = u + Ntrain
	  x_test[u, :, :] = input_data[t:t+T]
	  y_test[u] = (targets[t+T] > 0)

	model = keras_model.build_model(T, D)
	print(model.summary())
	
	with mlflow.start_run(run_name=args.ticker) as active_run:
		run_id = active_run.info.run_id
		mlflow.set_tag('runName', args.ticker + '-' + run_id)

		r = model.fit(x_train, y_train, batch_size=args.batch_size, epochs=args.num_epochs, validation_data=(x_test, y_test))
		metrics = r.history
		mlflow.log_param('num_layers', len(model.layers))
		mlflow.log_param('optimizer_name', type(model.optimizer).__name__)
		mlflow.log_param('num_epochs', args.num_epochs)
		mlflow.log_param('batch_size', args.batch_size)

		_mlflow_log_metrics(metrics, 'loss')
		_mlflow_log_metrics(metrics, 'accuracy')
		_mlflow_log_metrics(metrics, 'val_loss')
		_mlflow_log_metrics(metrics, 'val_accuracy')

		os.mkdir('mlflow/'+ run_id)
		model_local_path = os.path.join('mlflow', run_id, 'model')
		tf.saved_model.save(model, model_local_path)
		mlflow.tensorflow.log_model(tf_saved_model_dir=model_local_path,
																tf_meta_graph_tags=[tag_constants.SERVING],
																tf_signature_def_key='serving_default',
																artifact_path='model')
		duration = time() - start_time
		mlflow.log_metric('duration', duration)
		mlflow.end_run()

	if args.deploy:
		service = discovery.build('ml', 'v1')
		project_id = 'deep-stock-268818'
		bucket_name = 'deep-stock-ml-bucket'
		model_name = args.ticker
		model_version = 'mlflow_{}'.format(run_id)
		model_gcs_path = os.path.join('gs://', bucket_name, run_id, 'model')
		
		subprocess.call(
        "gsutil -m cp -r {} {}".format(model_local_path, model_gcs_path),
        shell=True)
		try:
			create_body = {
				'name': model_name,
				'regions': 'us-central1',
				'description': 'MLflow model'
			}
			parent = 'projects/{}'.format(project_id)
			service_projects = service.projects()
			print('p', service_projects)
			service_models = service_projects.models()
			print('m', service_models)
			service_request = service_models.create(parent=parent, body=create_body)
			print('r', service_request.to_json())
			service_request.execute()
		except:
			print("create model failure")
		
		#try:
		deploy_body = {
			'name': model_version,
			'deploymentUri': 'gs://{}/{}/model'.format(bucket_name, run_id),
			'framework': 'TENSORFLOW',
			'runtimeVersion': '1.14',
			'pythonVersion': '3.5'
		}
		parent = 'projects/{}/models/{}'.format(project_id, model_name)
		print(parent)
		service_version = service.projects().models().versions().create(
				parent=parent, body=deploy_body)
		print('v', service_version.to_json())
		response = service_version.execute()
		#except:
		#	print('deploy model failure')
		"""
		#test predict
		""" 
		#gcloud ai-platform local predict --model-dir mlflow/eb7746fb07084d43892873db2a100f5b/model/ --json-instances local-predict.json --framework tensorflow"""
if __name__ == '__main__':
	args = get_args()
	train_and_evaluate(args)