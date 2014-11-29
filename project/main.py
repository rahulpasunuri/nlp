from gensim import corpora, models, similarities
import logging
import gensim
import cleaning
import Recipe
import cPickle as pickle

'''
In this program we do the actual LDA, and give a certain output.
The datastucture used will be a list of Recipe Object which will be read 
from a pickle file, which has been already created
This has been done to increase modularity and reduce points of failures'''

def main(): 
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	print "Starting to load the pickle file ... "
	pickleFile = open("ReviewsDataStructureDump.pickle","rb")
	ReviewObjList = pickle.load(pickleFile)
	pickleFile.close()
	#This bigListOfReviews contains all the reviews
	#I don't know if keeping this big of a list in memory is a good idea. 
	#This is a very naive approach.

	bigListOfReviews = []

	print "Starting to load files ... "
	for obj in ReviewObjList:
		allReviews = obj.allReviews
		for i in range(0,len(allReviews)):
			#print allReviews[i][0]
			temp = []
			for word in allReviews[i][0]:
				#print "Type = "+ str(type(unicode(allReviews[i][0][0],errors='ignore')))
				word = unicode(word,errors='ignore')
				temp.append(word)
			print "Working on it ... "+str(len(bigListOfReviews))	
			bigListOfReviews.append(temp)
	
	print "Successfully loaded data in memory"		
	#print bigListOfReviews	
	print "Total length of reviews : "+str(len(bigListOfReviews))
	#print bigListOfReviews

	dictionary = corpora.Dictionary(bigListOfReviews)
	print dictionary
	dictionary.save_as_text("myDict.dict",sort_by_word=True)
	corpus = [dictionary.doc2bow(review) for review in bigListOfReviews]
	corpora.MmCorpus.serialize('reviewsCorpus.mm',corpus)
	id2word = corpora.Dictionary.load_from_text("myDict.dict")
	#lda = gensim.models.ldamodel.LdaModel(corpus=corpus,id2word=id2word,num_topics=10,passes=1,update_every=1)
	#Added multicore lda model to help with efficiency
	lda = gensim.models.ldamulticore.LdaMulticore(corpus=corpus,id2word=id2word,num_topics=10,passes=1)
	lda.print_topics(10)

	print "Naming Topics : "
	print lda.show_topic(1, topn=2)
	for obj in ReviewObjList:
		listOfTopicProbabilities = []
		for i in range(0,len(allReviews)):
			tempReview = allReviews[i][0]
			result = lda[dictionary.doc2bow(tempReview)]
			listOfTopicProbabilities.append(result)
		obj.topicProbabilities = listOfTopicProbabilities	

	pickleFile = open("LDAProcessed.pickle","wb")
	pickle.dump(ReviewObjList, pickleFile)
	pickleFile.close()

	'''for obj in ReviewObjList:
		print "*"*20
		print obj.name+" --> "+"TotalRating : "+obj.rating+"  Total Reviews: "+str(obj.numOfReviews)
		print " "
		for i in range(len(obj.allReviews)):
			print obj.allReviews[i][0]
			print obj.topicProbabilities[i]
		print "*"*20
		raw_input("Proceed ?")		
	'''
if __name__=="__main__": main()	
