import keras_model
import argparse
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import tensorflow as tf
import mlflow.tensorflow
from builtins import int
mlflow.tensorflow.autolog()

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--ticker', default='')
	parser.add_argument('--num-epochs', type=int, default='10')
	parser.add_argument('--batch-size', type=int, default='64')
	args, _ = parser.parse_known_args()
	return args

def train_and_evaluate(args):
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

	r = model.fit(x_train, y_train, batch_size=args.batch_size, epochs=args.num_epochs, validation_data=(x_test, y_test))

if __name__ == '__main__':
	args = get_args()
	tf.compat.v1.logging.set_verbosity('DEBUG')
	train_and_evaluate(args)