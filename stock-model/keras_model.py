import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


def build_model(T, D):	
	i = Input(shape=(T, D))
<<<<<<< HEAD
	x = LSTM(50)(i)
<<<<<<< HEAD
=======
	x = LSTM(50)(x)
	x = LSTM(25)(x)
>>>>>>> 044d9f51a6268fd5ae0448ba04f61c7c8b3c79d2
=======
	x = LSTM(60, return_sequences=True)(i)
	x = LSTM(30, return_sequences=True)(x)
	x = LSTM(15)(x)
>>>>>>> ec1f921d7719bbfdd816dfb3c91c1ac57973159c
	x = Dense(1, activation='sigmoid')(x)
	model = Model(i, x)
	model.compile(loss='mean_squared_error', optimizer=Adam(lr=.001), metrics=['accuracy'])

	return model

def build_dataset(features, labels, shuffle, num_epochs, batch_size):
	dataset = tf.data.Dataset.from_tensor_slices((features, labels))
	dataset = dataset.shuffle(buffer_size=len(features))
	dataset = dataset.repeat(num_epochs).batch(batch_size)
	return dataset