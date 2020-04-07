import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


def build(T, D):	
	i = Input(shape=(T, D))
	x = LSTM(50)(i)
	x = Dense(1, activation='sigmoid')(x)
	model = Model(i, x)
	model.compile(loss='binary_crossentropy', optimizer=Adam(lr=.001), metrics=['accuracy'])

	return model
