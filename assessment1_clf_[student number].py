# suggested imports, feel free to try other things!
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import tree
from sklearn.metrics import classification_report
import os

def load_imdb_data(data_folder):
	#d = {}
	d = defaultdict(list)
	# your code here
	# the returned dictionary should be of the form:
	# {'pos': [
	#			['word1', 'word2', word3, ... ], # each of these nested lists of strings are imdb reviews
	#			['word1', 'word2', word3, ... ]
	# 			... }
	# {'neg': [
	#			['word1', 'word2', word3, ... ],
	#			['word1', 'word2', word3, ... ]
	# 			... }
	files = os.listdir(data_folder)
	for infile in files:
		f = open(os.path.join(data_folder,infile))
		# process the review file 'f' and populate the dictionary 'd'
	return d

if __name__ == '__main__':

	train_data_folder = 'imdb/train'
	test_data_folder = 'imdb/train'

	train_data = load_imdb_data(train_data_folder)
	test_data = load_imdb_data(test_data_folder)

	# your code here: populate the all_train_docs and all_test_docs variables such that it contains a list of strings, 
	# where each string is one document
	# list of strings is the format required by scikit-learn's vectorizer
	all_train_docs = []
	all_test_docs = []
	all_docs = all_train_docs+all_test_docs
	vectorizer = CountVectorizer()
	vectorizer.fit(all_docs)

	# you must ensure that the indices in X_train and y_train correspond, i.e., 
	# the first element in X_train has a corresponding label in the first element of y_train, etc.
	X_train = vectorizer.transform(all_train_docs)
	y_train = [1 for x in train_data['pos']]+[0 for x in train_data['neg']]

	# same with the test split
	X_test = vectorizer.transform(all_test_docs)
	y_test = [1 for x in test_data['pos']]+[0 for x in test_data['neg']]
	
	# your code here for instantiating, training, obtaining predictions and evaluating your model
