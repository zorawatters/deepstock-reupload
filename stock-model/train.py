import build_model
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

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

model = build_model.build(T, D)
print(model.summary())

r = model.fit(x_train, y_train, batch_size=32, epochs=300, validation_data=(x_test, y_test))