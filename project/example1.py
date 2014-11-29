try:
	import logging
	import numpy
	import scipy
	from gensim import corpora, models, similarities
	print "Success"
except:
	print "There was an error"
 
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
documents = ["Human machine interface for lab abc computer applications", "A survey of user opinion of computer system response time", "The EPS user interface management system", "System and human system engineering testing of EPS", "Relation of user perceived response time to error measurement", "The generation of random binary unordered trees", "The intersection graph of paths in trees", "Graph minors IV Widths of trees and well quasi ordering", "Graph minors A survey"]

print documents
print 
print

stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

print texts

print

# remove words that appear only once
all_tokens = sum(texts, [])
print all_tokens

tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once] for text in texts]

print
print
print texts

dictionary = corpora.Dictionary(texts)
print 
print "Dictionary object"
print
print dictionary.token2id
dictionary.save('mydict.dict')
print
for tempList in texts:
	new_vec = dictionary.doc2bow(tempList)
	print
	print"Bag of Words"
	print new_vec

