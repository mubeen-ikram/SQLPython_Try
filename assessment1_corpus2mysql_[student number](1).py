import pymysql
import os

# Connect to the database
# connection = pymysql.connect(host='',
#                              user='',
#                              password='',
#                              db='',
#                              charset='')
connection = []


def load_imdb_data(data_folder):
    d = dict({})
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
        sentiment = []
        f = open(os.path.join(data_folder, infile), 'r', encoding="utf8")
        while True:
            line = f.readline()
            if not line:
                break
            word = []
            words = line.split(" ")
            for wrd in words:
                word.append(wrd)
            sentiment.append(word)
        d[infile] = sentiment
    # process the review file 'f' and populate the dictionary 'd'
    return d


def get_mostfreq_words(data_dict):
    freqdict = {}
    for data in data_dict['pos']:
        for wrd in data:
            if wrd not in freqdict.keys():
                freqdict[wrd] = 0
            freqdict[wrd] = freqdict[wrd] + 1
    for data in data_dict['neg']:
        for wrd in data:
            if wrd not in freqdict.keys():
                freqdict[wrd] = 0
            freqdict[wrd] = freqdict[wrd] + 1

    # your code for creating a frequency distribution of the words in the dataset
    # can be useful to pre-select a vocabulary
    return freqdict


def create_tables():
    # your code for creating the tables 'corpus', 'dictionary' and 'sentiment'
    with connection.cursor() as cur:
        q = """
			CREATE TABLE dictionary(
			  # some columns here and pk constraint here
			);
		"""
        cur.execute(q)
        connection.commit()

    with connection.cursor() as cur:
        q = """
			CREATE TABLE sentiment_corpus(
			# some columns and pk constraint here
			);
		"""
        cur.execute(q)
        connection.commit()

    with connection.cursor() as cur:
        q = """
			CREATE TABLE mentions(
			  # some columns and pk/fk constraints here
			);
		"""
        cur.execute(q)
        connection.commit()


def populate_dictionary(most_freq_words):
    # columns: wordId, word
    rows = []
    idx = 1
    for idx in most_freq_words:
        rows.append(idx)
    # your code for populating the 'rows' list and incrementing the counter goes here
    with connection.cursor() as cur:
        q = """
				YOUR INSERT STATEMENT HERE
		"""
        cur.executemany(q, rows)
        connection.commit()


def populate_sentiment_corpus(data_dictionary):
    #  columns: textID, sentimentValue
    rows = []
    text_idx = 1
    for label in data_dictionary:
        for document in data_dictionary[label]:
            rows.append(label)
    with connection.cursor() as cur:
        q = """
				# YOUR INSERT STATEMENT HERE
		"""
        cur.executemany(q, rows)
        connection.commit()


class Mentions(object):
    def __init__(self):
        self.hit_idx = 0
        self.text_idx = 0
        self.offset = 0


def populate_mentions(data_dictionary, most_freq_words):
    #  columns: textID, ID, wordID
    rows = []
    hit_idx = 1
    text_idx = 1
    for label in data_dictionary:
        for document in data_dictionary[label]:
            offset = 1
            for word in document:
                if word in most_freq_words:
                    mention = Mentions()
                    mention.hit_idx = hit_idx
                    mention.text_idx = text_idx
                    mention.offset = offset
                    rows.append(mention)
                    hit_idx += 1
                    text_idx += 1
                offset += 1

    print(rows)

    # your (big) chunk of code goes here to populate the rows list
    with connection.cursor() as cur:
        q = """
				YOUR INSERT STATEMENT HERE
		"""
        cur.executemany(q, rows)
        connection.commit()


def query_32():
    results = []
    # your code here
    return results


if __name__ == '__main__':

    data_folder = 'imdb/train'

    data = load_imdb_data(data_folder)
    freqdist = get_mostfreq_words(data)
    # we only keep the 100 most frequent words
    most_freq_words = [a for a, b in sorted(freqdist.items(), key=lambda x: x[1], reverse=True)][:100]

    try:
        # this is the workflow
        # create_tables()
        print('populating the dictionary table')
        # populate_dictionary(most_freq_words)
        print('populating the sentiment corpus table')
        # populate_sentiment_corpus(data)
        print('populating the mentions table')
        populate_mentions(data, most_freq_words)
    finally:
        connection.close()

    print('== Attempting query for question 3.2 ==')
    for r in query_32():
        print(r)
