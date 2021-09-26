# CS379 –Machine Learning
# Unit 4 – Individual Project 1
# Christopher Lakey
# Colorado Technical University

# This file generates the weights we will be using in our text generator
# to create new sentences from Alice in Wonderland.

# First we start with importing our libraries.
# We are using numpy to create multidimensional arrays in which we are storing data.
# The multidimensional array will store our data for the LSTM model to learn sequences
# of text from Alice in Wonderland. Keras is a neural network model package that we will
# be using to feed our data into. Keras is a part of Tensorflow which is a Python
# Machine learning package used for data science.

import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# Loading in the Alice in Wonderland file
filename = "alice_in_wonderland.txt"

# Read the data file
raw_text = open(filename, 'r', encoding='utf-8').read()

#Convert the text to lowercase.
raw_text = raw_text.lower()

# Convert the text to numbers to be used in our Neural Network Model
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

# Here we are getting lengths of the characters and vocabulary to describe the data
# We then print this data to the console
n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

# Here we are preparing the input of the data to take in the data and
# output pairs of encoded integers.
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)

# Here we are transforming our data into vectors, which is an array of 47 integers
# Representing the lowercase characters in ASCII text so each word in the text
# can be run through the model to make future predictions about the structure of
# the sentences we will be outputting.
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
X = X / float(n_vocab)
y = np_utils.to_categorical(dataY)


# Here we are creating our LTSM model using Keras. I don't toally understand all of it but
# from what I gather we are using a sing hidden LSTM layer with 256 memory units and a dropout of 20.
# using this we create an output layer the returns a prediction for the next word in the generation
# that uses our 47 character array and returns a score between 0 and one to determine how probable
# the next word will be when generating the text. This file is going to create multiple iterations
# of predictions and train itself to get better and better at generating new words and these
# predictions will be stored in weight file we will use in our predictions file to generate the text.
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Here we are defining the generation of checkpoint files to remember older predictions and improve on the model with
# each Epoch. This will generate the Epoch checkpoint files used later for our predictions and eventual
# text generation.
filepath = "weights-improvement-bigger-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

# Here we are fitting the model by specifying the amount of Epochs and the batch size.
# This is a delicate balance of getting the righ amount of Epochs to create an accurate model
# and having a small enough batch size to make our predictions more accurate.
# I have set this to 200 epochs and a size of 64 because around here is when the generated
# sentences start to make sense in our output.
model.fit(X, y, epochs=50, batch_size=64, callbacks=callbacks_list)
