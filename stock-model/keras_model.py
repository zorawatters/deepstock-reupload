import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


def build_model(T, D):	
	i = Input(shape=(T, D))
	x = LSTM(50)(i)
	x = Dense(1, activation='sigmoid')(x)
	model = Model(i, x)
	model.compile(loss='binary_crossentropy', optimizer=Adam(lr=.001), metrics=['accuracy'])

	return model

def build_dataset(features, labels, shuffle, num_epochs, batch_size):
	dataset = tf.data.Dataset.from_tensor_slices((features, labels))
	dataset = dataset.shuffle(buffer_size=len(features))
	dataset = dataset.repeat(num_epochs).batch(batch_size)
	return dataset