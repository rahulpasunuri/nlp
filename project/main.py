from gensim import corpora, models, similarities
import logging
import gensim
import cleaning
import Recipe
from Recipe2 import Recipe2
import cPickle as pickle

'''
In this program we do the actual LDA, and give a certain output.
The datastucture used will be a list of Recipe Object which will be read 
from a pickle file, which has been already created
This has been done to increase modularity and reduce points of failures'''

def main(): 
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	
	#Change this to your br2 path
	baseDir = ""

	print "Starting to load the pickle file ... "
	pickleFile = open(baseDir+"ReviewsDataStructureDump.pickle","rb")
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
			temp = []
			for word in allReviews[i][0]:
				word = unicode(word,errors='ignore')
				temp.append(word)
			print "Working on it ... "+str(len(bigListOfReviews))	
			bigListOfReviews.append(temp)
	
	print "Successfully loaded data in memory"		
	print "Total length of reviews : "+str(len(bigListOfReviews))

	dictionary = corpora.Dictionary(bigListOfReviews)
	print dictionary
	dictionary.save_as_text(baseDir+"myDict.dict")
	corpus = [dictionary.doc2bow(review) for review in bigListOfReviews]
	corpora.MmCorpus.serialize(baseDir+'reviewsCorpus.mm',corpus)
	id2word = corpora.Dictionary.load_from_text(baseDir+"myDict.dict")
	lda = gensim.models.ldamodel.LdaModel(corpus=corpus,id2word=id2word,num_topics=10,passes=1,update_every=1)
	
	#Added multicore lda model to help with efficiency
	#lda = gensim.models.ldamulticore.LdaMulticore(corpus=corpus,id2word=id2word,num_topics=10,passes=1)
	
	lda.print_topics(10)

	Review2ObjList = []
	for obj in ReviewObjList:
		
		listOfTopicProbDict= []
		for i in range(0,len(obj.allReviews)):
			tempReview = obj.allReviews[i][0]
			temp = []
			for word in tempReview:
				word = unicode(word,errors='ignore')
				temp.append(word)
			result = tuple2dictionary(lda[dictionary.doc2bow(temp)])
			listOfTopicProbDict.append(result)
			
		listOfRecipeRatings = []	
		for tempTuple in obj.allReviews:
			listOfRecipeRatings.append(tempTuple[1])

		Review2ObjList.append(Recipe2(name=obj.name,rating=obj.rating,reviewRatings=listOfRecipeRatings,numOfReviews=obj.numOfReviews, topicProbabilities=listOfTopicProbDict))	

	print "Writing to LDAProcessed.pickle file"	
	pickleFile = open(baseDir+"LDAProcessed.pickle","wb")
	pickle.dump(Review2ObjList, pickleFile)
	pickleFile.close()
	print "Finished Writing to pickle File"

def tuple2dictionary(listOfTuples):
	dictOfProbabilities = {}
	for tempTuple in listOfTuples:
		dictOfProbabilities[tempTuple[0]] = tempTuple[1]
	return dictOfProbabilities	
if __name__=="__main__": main()	
