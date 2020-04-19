import keras_model
import model_deployment
import argparse
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import requests
import tensorflow as tf
from tensorflow.python.saved_model import tag_constants
import mlflow.tensorflow
from builtins import int
from time import time
import os
import subprocess
import logging
from googleapiclient import discovery
from google.oauth2 import service_account

#mlflow.tensorflow.autolog()

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--ticker', default='')
	parser.add_argument('--num-epochs', type=int, default='20')
	parser.add_argument('--batch-size', type=int, default='8')
	parser.add_argument('--deploy', action='store_true', default=False)
	parser.add_argument('--create', action='store_true', default=False)
	args, _ = parser.parse_known_args()
	return args

def _mlflow_log_metrics(metrics, metric_name):
  for epoch, metric in enumerate(metrics[metric_name], 1): 
  	mlflow.log_metric(metric_name, metric, step=epoch)

def train_and_evaluate(args):
	start_time = time()
	url = 'http://35.222.54.209:5000/' + args.ticker + '/historicaldata'
	try:
		hist_data = requests.get(url)
	except requests.exceptions.RequestException as e:
		raise SystemExit(e)
	df = pd.DataFrame(hist_data.json())
	df.sort_values('date')
	#df = pd.read_json('{'+hist_data.json()+'}')
	#df = pd.read_csv('https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv')
	df['PrevClose'] = df['Close'].shift(1)

	df['Return'] = (df['Close'] - df['PrevClose']) / df['PrevClose']
	print(df.head())
	input_data = df[['Open', 'High', 'Low', 'Close', 'Volume']].values
	targets = df['Return'].values
	print(input_data.shape)
	T = 10
	D = input_data.shape[1]
	N = len(input_data) - T

	Ntrain = len(input_data) * 5 // 6
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
		try:
			os.mkdir('mlflow/'+ run_id)
		except:
			os.mkdir('mlflow')
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

	if args.create or args.deploy:
		service = discovery.build('ml', 'v1')
		project_id = 'deep-stock-268818'
		bucket_name = 'deep-stock-ml-bucket'
		model_name = args.ticker
		model_version = 'mlflow_{}'.format(run_id)
		model_gcs_path = os.path.join('gs://', bucket_name, run_id, 'model')
		model_helper = model_deployment.AIPlatformModel(project_id)
		
		model_helper.upload_to_bucket(model_local_path, model_gcs_path)
		model_helper.create_model(model_name)
		
		if args.deploy:
			model_helper.deploy_model(model_gcs_path, model_name, run_id)
			logging.info('Model Deployment complete')

		#gcloud ai-platform local predict --model-dir mlflow/eb7746fb07084d43892873db2a100f5b/model/ --json-instances local-predict.json --framework tensorflow"""
if __name__ == '__main__':
	args = get_args()
	train_and_evaluate(args)