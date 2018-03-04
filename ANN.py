import tensorflow as tf
import tflearn
import numpy as np
import math
import time
import sys
import pdb
import pickle


# Custom method to prevent printing of tflearn messages
# 1 1 1 1 1 1
try:
	from tflearn.dh_hack import set_suppress_output as dh_hack_suppress_output
except:
	def dh_hack_suppress_output(a):
		pass

global num

dataFile = "./insurance"

input = 15

trData = np.loadtxt(dataFile + 'Train.csv', delimiter=',')
trX = trData[:,1:(input+1)] # TODO Changeme
trY = trData[:,(input+1):]

valData = np.loadtxt(dataFile + 'Validation.csv', delimiter=',')
valX = valData[:,1:(input+1)] # TODO Changeme
valY = valData[:,(input+1):]


testData = np.loadtxt(dataFile + 'Test.csv', delimiter=',')
testX = testData[:,1:(input+1)] # TODO Changeme
testY = testData[:,(input+1):]

class ANN(object):

	# Model parameters
	num_epoch = 100 #TODO change back to 100
	input_nodes = input  # TODO change
	h1_nodes = 128
	h2_nodes = 256
	h3_nodes = 256
	h4_nodes = 128
	output_nodes = 5
	batch_size = 128 # Change back to 128

	learning_rate = 10.0
	decay_rate = 0.9
	momentum = 1.0
	dropout_value = 0.5

	# Preprocessing
	preprocessing = True

	# Regularization - [None, L2]
	doRegularization = False
	regularization = "L2"

	# Dropout -
	dropout = False

	# Activation - [Sigmoid, ReLu6]
	activation = "sigmoid"

	# Loss - [mean-squared error, softmax cross entropy]
	loss = "mean-square"

	# Optimization
	optimization = "momentum"

	model = None

	targets = None

	'''
		settings
			- Preprocessing - True, False
			- Regularization - None, L2
			- Dropout - True, False
			- Activation - Sigmoid, ReLu6
			- Loss - Mean-Square, Softmax
			- Optimization - AdaDelta, Momentum
	'''

	def __init__(self, learning_rate, decay_rate, momentum, settings):

		tf.reset_default_graph()

		self.learning_rate = learning_rate
		self.decay_rate = decay_rate
		self.momentum = momentum

		if settings[0] == "1":
			self.preprocessing = True
		else:
			self.preprocessing = False

		if settings[1] == "1":
			self.doRegularizer = True
		else:
			self.doRegularizer = False

		if settings[2] == "1":
			self.dropout = True
		else:
			self.dropout = False

		if settings[3] == "1":
			self.activation = "sigmoid"
		else:
			self.activation = "relu6"

		if settings[4] == "1":
			self.loss = "mean_square"
		else:
			self.loss = "softmax_categorical_crossentropy"

		if settings[5] == "1":
			self.optimization = "adaDelta"
		else:
			self.optimization = "momentum"

		# Reading in data



		self.targets = tf.placeholder(tf.float32, [None, self.output_nodes])


		input_layer = None

		if self.preprocessing:
			data_processing = tflearn.data_preprocessing.DataPreprocessing()
			data_processing.add_featurewise_stdnorm(std=74.09373752913417)
			data_processing.add_featurewise_zero_center(mean=18.856167177006782)
			input_layer = tflearn.input_data(shape=[None, self.input_nodes], data_preprocessing=data_processing)

		else:
			input_layer = tflearn.input_data(shape=[None, self.input_nodes])

		h1 = None
		h2 = None
		h3 = None
		h4 = None
		output_layer = None

		if self.doRegularizer:
			# 1st Hidden Layer
			h1 = tflearn.fully_connected(input_layer, self.h1_nodes, activation=self.activation, regularizer=self.regularization, weight_decay=1/(8 * self.batch_size * self.input_nodes*self.h1_nodes))

			if self.dropout:
				h1 = tflearn.dropout(h1, self.dropout_value)

			# 2nd Hidden Layer
			h2 = tflearn.fully_connected(h1, self.h2_nodes, activation=self.activation, regularizer=self.regularization, weight_decay=1/(8 * self.batch_size * self.h1_nodes*self.h2_nodes))

			if self.dropout:
				h2 = tflearn.dropout(h2, self.dropout_value)

			'''
			h3 = tflearn.fully_connected(h2, self.h3_nodes, activation=self.activation, regularizer=self.regularization, weight_decay=1/(8 * self.batch_size * self.h2_nodes*self.h3_nodes))

			if self.dropout:
				h3 = tflearn.dropout(h3, self.dropout_value)

			# 2nd Hidden Layer
			h4 = tflearn.fully_connected(h3, self.h4_nodes, activation=self.activation, regularizer=self.regularization, weight_decay=1/(8 * self.batch_size * self.h3_nodes*self.h4_nodes))

			if self.dropout:
				h4 = tflearn.dropout(h4, self.dropout_value)
			'''
			# Output Layer
			output_layer = tflearn.fully_connected(h2, self.output_nodes, activation=self.activation, regularizer=self.regularization, weight_decay=1/(8 * self.batch_size * self.h2_nodes*self.output_nodes))
		else:
			# 1st Hidden Layer
			h1 = tflearn.fully_connected(input_layer, self.h1_nodes, activation=self.activation)

			if self.dropout:
				h1 = tflearn.dropout(h1, self.dropout_value)

			# 2nd Hidden Layer
			h2 = tflearn.fully_connected(h1, self.h2_nodes, activation=self.activation)

			'''
			if self.dropout:
				h2 = tflearn.dropout(h2, self.dropout_value)

			h3 = tflearn.fully_connected(h2, self.h3_nodes, activation=self.activation)

			if self.dropout:
				h3 = tflearn.dropout(h3, self.dropout_value)

			# 2nd Hidden Layer
			h4 = tflearn.fully_connected(h3, self.h4_nodes, activation=self.activation)

			if self.dropout:
				h4 = tflearn.dropout(h4, self.dropout_value)
			'''
			# Output Layer
			output_layer = tflearn.fully_connected(h2, self.output_nodes, activation=self.activation)

		# Learning
		# Optimizer
		opt = None
		if self.optimization == "momentum":
			opt = tflearn.Momentum(learning_rate=self.learning_rate, lr_decay=self.decay_rate, momentum=self.momentum)
		else:
			opt = tflearn.AdaDelta(learning_rate=self.learning_rate, rho=self.decay_rate)

		r = tflearn.regression(output_layer, placeholder=self.targets, optimizer=opt, loss=self.loss)
		self.model = tflearn.DNN(r)



	def fit(self):
		self.model.fit(trX, {self.targets:trY}, n_epoch=self.num_epoch, show_metric=True, batch_size=self.batch_size)

	def validate(self):
		self.fit()
		return self.model.evaluate(valX, {self.targets:valY})[0]

	def test(self):
		self.model.fit(np.concatenate((trX, valX), axis=0), {self.targets:np.concatenate((trY, valY), axis=0)}, n_epoch=self.num_epoch, show_metric=True, batch_size=self.batch_size)
		return self.model.evaluate(testX, {self.targets:testY})[0]
		
	def predict(self, inputs):
	    return self.model.predict(inputs)
	    

phi = (1+math.sqrt(5)) / 2.0
aArray = [0.0, 0.0, 0.0]
bArray = [0.01, 1.0, 1.0]

learning_rate = 0.0
decay_rate = 0.0
momentum = 0.0

values = [[], [], []]

def goldenSectionSearch_learningRate(settings, epsilon=1e-6):
	global a
	global b
	global learning_rate

	print(epsilon)

	# Optimizing learning rate
	a = aArray[0]
	b = bArray[0]
	c = b - ((b - a) / phi)
	d = a + ((b - a) / phi)

	counter = 1

	while abs(c - d) > epsilon:
		ann1 = ANN(c, 0.99, 0.99, settings)
		c_out = ann1.validate()
		del ann1

		ann2 = ANN(d, 0.99, 0.99, settings)
		d_out = ann2.validate()
		del ann2

		if c_out > d_out:
			b = d
		else:
			a = c

		values[0].append((c, c_out))
		values[0].append((d, d_out))


		c = b - ((b - a) / phi)
		d = a + ((b - a) / phi)
		print("Iteration: %d, A: %1.6f B: %1.6f Epsilon: %1.6f" % (counter, a, b, abs(c-d)))
		counter += 1

	max_point = (b + a) / 2.0
	ann = ANN(max_point, 0.5, 0.5, settings)
	ab_out = ann.validate()

	values[0].append((max_point, ab_out))
	learning_rate = max_point

def goldenSectionSearch_decayRate(settings, epsilon=1e-5):
	global a
	global b
	global decay_rate

	# Optimizing learning rate
	a = aArray[1]
	b = bArray[1]
	c = b - ((b - a) / phi)
	d = a + ((b - a) / phi)

	counter = 1

	while abs(a - b) > epsilon:
		ann1 = ANN(learning_rate, c, 0.99, settings)
		c_out = ann1.validate()
		del ann1

		ann2 = ANN(learning_rate, d, 0.99, settings)
		d_out = ann2.validate()
		del ann2

		if c_out > d_out:
			b = d
		else:
			a = c

		values[1].append((c, c_out))
		values[1].append((d, d_out))


		c = b - ((b - a) / phi)
		d = a + ((b - a) / phi)
		print("Iteration: %d, A: %1.6f B: %1.6f Epsilon: %1.6f" % (counter, a, b, abs(c-d)))
		counter += 1

	max_point = (b + a) / 2.0
	ann = ANN(learning_rate, max_point, 0.5, settings)
	ab_out = ann.validate()

	values[1].append((max_point, ab_out))
	decay_rate = max_point

def goldenSectionSearch_momentum(settings, epsilon=1e-5):
	global a
	global b
	global momentum

	# Optimizing learning rate
	a = aArray[2]
	b = bArray[2]
	c = b - ((b - a) / phi)
	d = a + ((b - a) / phi)

	counter = 1

	while abs(a - b) > epsilon:
		ann1 = ANN(learning_rate, decay_rate, c, settings)
		c_out = ann1.validate()
		del ann1

		ann2 = ANN(learning_rate, decay_rate, d, settings)
		d_out = ann2.validate()
		del ann2

		if c_out > d_out:
			b = d
		else:
			a = c

		values[2].append((c, c_out))
		values[2].append((d, d_out))


		c = b - ((b - a) / phi)
		d = a + ((b - a) / phi)
		print("Iteration: %d, A: %1.6f B: %1.6f Epsilon: %1.6f" % (counter, a, b, abs(c-d)))
		counter += 1

	max_point = (b + a) / 2.0
	ann = ANN(learning_rate, decay_rate, max_point, settings)
	ab_out = ann.validate()

	values[2].append((max_point, ab_out))
	momentum = max_point

def binaryToDecimal(settings):
	sum = 0
	for x in range(6):
		sum += (2**x) * int(settings[6 - x - 1])
	return sum

def decimalToBinary(num):
	binaryString = bin(num)[2:]
	if (len(binaryString) < 6):
		for x in range(6 - len(binaryString)):
			binaryString = '0' + binaryString
	return binaryString

def train():
    try:
        dh_hack_suppress_output(True)
        '''
        ann = ANN(0.01, 0.9, 0.0, '111111')
        print(ann.fit())
        print(ann.test())
        '''
        num = int(sys.argv[1]) if (len(sys.argv) >= 2) else 0
        settings = decimalToBinary(num)
        start = time.time()
        print(num)

        goldenSectionSearch_learningRate(settings)
        print("Finished with Learning Rate")
        goldenSectionSearch_decayRate(settings)
        print("Finished with Decay Rate")
        if settings[5] == "0":
            goldenSectionSearch_momentum(settings)
            print("Finished with Momentum Rate")


        # file = open("out"+ str(num) + "_" + str(learning_rate) + "_" + str(decay_rate)+ "_" + str(momentum)+ ".txt", 'w')
        file = open("out"+ str(num) + ".txt", 'w')
        file.write("Settings: " + str(settings) + "\n")
        file.write("Preprocesssing: %s \nRegularization: %s \nDropout: %s \nActivation: %s \nLoss: %s \nOptimization: %s\n" %
                    (("None", "STD/Mean")        [settings[0] == "1"],
                    ("None", "L2")              [settings[1] == "1"],
                    ("None", "On Hidden")       [settings[2] == "1"],
                    ("ReLu6", "Sigmoid")        [settings[3] == "1"],
                    ("softmax", "mean_square")  [settings[4] == "1"],
                    ("Momentum", "AdaDelta")    [settings[5] == "1"])

                    )
        # file.write("Learning rate: %s, Decay Rate: %s, Momentum: %s\n" %
        #            (settings[6], settings[7], settings[8]))

        startBest = time.time()
        ann = ANN(learning_rate, decay_rate, momentum, settings)
        accuracy = ann.test()
        end = time.time()
        print("Testing accuracy: %s%% with LR: %1.6f, DR: %1.6f, momentum: %1.6f" % (accuracy*100, learning_rate, decay_rate, momentum))
        file.write("Testing accuracy: %s%% with LR: %1.6f, DR: %1.6f, momentum: %1.6f\n" % (accuracy*100, learning_rate, decay_rate, momentum))


        file.write("\n\nValues: \n")
        for x in values:
            for y in x:
                file.write(str(y) + "\n")
            file.write("\n\n")


        file.write("\n\nSeconds: ")
        file.write("Total training: " + str(end-start) + "\n")
        file.write("Best Settings Time: " + str(end-startBest) + "\n")
        file.close()

    except:
        # file = open("out"+ str(num) + "_" + str(learning_rate) + "_" + str(decay_rate)+ "_" + str(momentum)+ ".txt", 'w')
        file = open("out"+ str(num) + ".txt", 'w')
        file.write("Settings: " + str(settings) + "\n")
        file.write("Preprocesssing: %s \nRegularization: %s \nDropout: %s \nActivation: %s \nLoss: %s \nOptimization: %s\n" %
                    (("None", "STD/Mean")        [settings[0] == "1"],
                    ("None", "L2")              [settings[1] == "1"],
                    ("None", "On Hidden")       [settings[2] == "1"],
                    ("ReLu6", "Sigmoid")        [settings[3] == "1"],
                    ("softmax", "mean_square")  [settings[4] == "1"],
                    ("Momentum", "AdaDelta")    [settings[5] == "1"])

                    )
                
        file.write("\n\nValues: \n")
        for x in values:
            for y in x:
                file.write(str(y) + "\n")
            file.write("\n\n")

        file.close()

def run(lr=0.009, dr=0.0004, momentum=1.0, settings="111111"):
    ann = ANN(lr, dr, momentum, settings)
    "Training data"
    ann.fit()
    
    "Testing data"
    print("Accuracy: {0:.12f}".format(ann.test()))
    
    return ann

def predict(input):
    ann = ANN(0.008090, 0.969623, 0.000000, "111111")
    ann.fit()
    
    '''
        Age
        Sex
        Employment
        Preconditions
            0 none
            1 low
            2 medium
            3 high
        Annual Income
        BMI
        Tobacco
        Bronze Price
        Silver Price
        Gold Price
        Platinum Price
        Purchased Plan
            0 - Bronze
            1 - Silver
            2 - Gold
            3 - Platinum
    '''
    return ann.predict(input)
    
'''
    Designed to allow writing of model to file.
    Taken from : https://stackoverflow.com/a/47952913
    
    Doesn't actually allow writing. 
    Still gives error TypeError: can't pickle _thread.lock objects on 
    line 484 - pickle.dump(model, open("model.tflearn", "wb"))
'''
setattr(tf.contrib.rnn.GRUCell, '__deepcopy__', lambda self, _: self)
setattr(tf.contrib.rnn.BasicLSTMCell, '__deepcopy__', lambda self, _: self)
setattr(tf.contrib.rnn.MultiRNNCell, '__deepcopy__', lambda self, _: self)

#model = run(0.008090, 0.969623, 0.000000, "111111")
#pickle.dump(model, open("model.tflearn", "wb"))
print(predict([[27, 1, 2, 2, 1, 1, 1, 1, 1, 2, 3, 1, 200, 40.1616210938, 1]]))
