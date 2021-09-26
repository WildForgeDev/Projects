# import our libraries to implement the algorithm.
# random seed is used to generate a random seed number to feed into the algorithm.
# randrange is used to create a range of random numbers for the algorithm to use.
# CSV is used to pull our data and put it into a format we can run through the model.

from random import seed
from random import randrange
from csv import reader
 
# Create function to read the data file we are using.
def load_csv(filename):
	file = open(filename, "rt")
	lines = reader(file)
	dataset = list(lines)
	return dataset
 
# Function that converts a column of strings to  float types
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
 
# create function for cross validation splits. This is taking the dataset's splits and copying those to another array
# The amount of folds is the length of the split values. 
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split
 
# Function that calculates the accuracy of the decision tree model. We pass in the actual data and the predicted data.
# from there we set the correct amount to 0. We then loop through the actual and predicted values and 
# Count how many of them match each other.
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0
 
# Function to run the data through the cross validation split function. We are passing the dataset and fold amounts into the 
# Cross validation function to add the calculations to one list and remove the evaluated folds from the first list.
# We then run this data through the accuaracy metric function to get a count of the correct predictions based on our indexed data.
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores
 
# Create an index of the attribute in the data we are looking at. We are using the attribute and splitting the data into two lists.
# The lists consist of the index for the attribute and the value of that index.
def test_split(index, value, dataset):
	left, right = list(), list()
	for row in dataset:
		if row[index] < value:
			left.append(row)
		else:
			right.append(row)
	return left, right
 
# Create a function to calculate the costs of splits based on the Gini Index. This function looks at our indexes and scores them based on how
# mixed the classes are. This ranges form 0 to .50. ) being a perfect split and .50 being the worst split possible.
def gini_index(groups, classes):
	# Get all indexes to score
	n_instances = float(sum([len(group) for group in groups]))
	# Calculate the sum for the gini index for each index.
	gini = 0.0
	for group in groups:
		size = float(len(group))
		# solving for division by 0.
		if size == 0:
			continue
		score = 0.0
		# Score each index based on each class.
		for class_val in classes:
			p = [row[-1] for row in group].count(class_val) / size
			score += p * p
		# Weigh the data based on the total relative weights in the dataset.
		gini += (1.0 - score) * (size / n_instances)
	return gini


# Create a function that evaluates the splits and deteerimes if the split is good or not. We use our gini index to score the split data
# and determine the cost of the split to make the best split determinations about the data. We pass in the dataset, set a class list to then
# be run through the gini index and return a dictionary of the b_index, b_value, and the b_groups.
def get_split(dataset):
	class_values = list(set(row[-1] for row in dataset))
	b_index, b_value, b_score, b_groups = 999, 999, 999, None
	for index in range(len(dataset[0])-1):
		for row in dataset:
			groups = test_split(index, row[index], dataset)
			gini = gini_index(groups, class_values)
			if gini < b_score:
				b_index, b_value, b_score, b_groups = index, row[index], gini, groups
	return {'index':b_index, 'value':b_value, 'groups':b_groups}
 
# Create a function the determines when to stop splitting and creating nodes of the decision tree. This function selects the class value for our row group
# and returns the most common output values for the row group list.
def to_terminal(group):
	outcomes = [row[-1] for row in group]
	return max(set(outcomes), key=outcomes.count)
 
# Create a function that repeatedly runs the to_terminal function and creates split groups. This has the effect of creating 
# multiple child nodes and traversing the nodes to create a tree structure.
def split(node, max_depth, min_size, depth):
	left, right = node['groups']
	del(node['groups'])
	# check for a no split
	if not left or not right:
		node['left'] = node['right'] = to_terminal(left + right)
		return
	# check for max depth
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		return
	# process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left)
	else:
		node['left'] = get_split(left)
		split(node['left'], max_depth, min_size, depth+1)
	# process right child
	if len(right) <= min_size:
		node['right'] = to_terminal(right)
	else:
		node['right'] = get_split(right)
		split(node['right'], max_depth, min_size, depth+1)
 
# Create a function that creates a root node and uses the split function recursivley to build out the entire tree.
def build_tree(train, max_depth, min_size):
	root = get_split(train)
	split(root, max_depth, min_size, 1)
	return root
 
# Create a function that takes the nodes and the row data and makes predictions based on the data and returns a prediction to be used to measure the accuaracy of the models.
def predict(node, row):
	if row[node['index']] < node['value']:
		if isinstance(node['left'], dict):
			return predict(node['left'], row)
		else:
			return node['left']
	else:
		if isinstance(node['right'], dict):
			return predict(node['right'], row)
		else:
			return node['right']
 
# Create a function the finalizes the decision tree by calling the build tree function, passing in the maximum depth, minimum size, and
# the training/test data and return the final predictions.
def decision_tree(train, test, max_depth, min_size):
	tree = build_tree(train, max_depth, min_size)
	predictions = list()
	for row in test:
		prediction = predict(tree, row)
		predictions.append(prediction)
	return(predictions)
 
# Create a test classification/Regression tree
seed(1)
# Load in the data to be run through the algorithm.
filename = 'data_banknote_authentication.txt'
dataset = load_csv(filename)
# Convert the strings in the data to integers.
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
# Evaluate the algorithm and return the prediction scores.
n_folds = 5
max_depth = 5
min_size = 10
scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))