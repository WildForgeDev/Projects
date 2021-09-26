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

import sys
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
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

# Create the mappings of unique characters
# and we are getting lengths of the characters and vocabulary to describe the data
# We then print this data to the console
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

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


# Here we are preparing the input of the data to take in the data and
# output pairs of encoded integers.
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
X = X / float(n_vocab)
y = np_utils.to_categorical(dataY)



# Here we are transforming our data into vectors, which is an array of 47 integers
# Representing the lowercase characters in ASCII text so each word in the text
# can be run through the model to make future predictions about the structure of
# the sentences we will be outputting.
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))

# Here we our loading our network weigh checkpoint file to be used in generating text.
filename = "weights-improvement-bigger-153-0.8983.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')

# We are creating a random seed of text to use to generate text.
start = numpy.random.randint(0, len(dataX) - 1)
pattern = dataX[start]
print("Seed:")
print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")

# Here we are generating the characters based off of our network weights.
for i in range(1000):
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x / float(n_vocab)
    prediction = model.predict(x, verbose=0)
    index = numpy.argmax(prediction)
    result = int_to_char[index]
    seq_in = [int_to_char[value] for value in pattern]
    sys.stdout.write(result)
    pattern.append(index)
    pattern = pattern[1:len(pattern)]
print("\nDone.")
