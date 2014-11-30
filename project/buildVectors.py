#!/usr/bin/python
import cPickle as pickle

def main():
	ldaPicklePath = "ReviewsDataStructureDump.p"
	trainf = open("liTrainingFiles.pickle","rb")	
	testf = open("liTestFiles.pickle","rb")
	trainingFile = open("trainVectors.txt","w")
	testFile = open("testVectors.txt","w")
	
	#the list of files to be used as training and testing...
	liTrainingFiles = pickle.load(trainf)
	liTestFiles = pickle.load(testf)
		
	trainf.close()
	testf.close()			
	
	
	#open the results of lda..
	pickleFile = open(ldaPicklePath,"rb")
	recipes = pickle.load(pickleFile)
	pickleFile.close()

	if len(recipes)<0:
		print "No recipes found"
		exit()
	
	liTopics = []
	for r in recipes:
		liTopics =  [ k for k in r.topicProbabilities[0]] #get all keys of the first prob vector..
		liTopics.sort()
								
	for r in recipes:
		v = [] #this is the data vector
		v.append(r.rating) # first element of the vector is rating...
		v.extend([0 for a in liTopics]) #init values of feature topics as 0.
		
		for r in range(r.numReviews):
			rating = r.allReviews[r]
			topicDictionary = r.topicProbabilities[r]					
			
			sum1= 0
			#normalize the topic dict first..
			for key in topicDictionary:
				sum1 +=topicDictionary[key]
			
			for key in topicDictionary:
				topicDictionary[key] = topicDictionary[key]/sum1	
			
			for i in range(liTopics):
				v[i+1] += topicDictionary[liTopics[i]] * rating
		
		#normalize the data vector now..
		sum1 = 0
		for i in range(len(liTopics)):
			sum1+= v[i+1]

		for i in range(len(liTopics)):
			v[i+1] = v[i+1]/sum1		
		
			
		s = ""
		s+= str(v[0])
		
		for i in range(len(liTopics)):
			if v[i+1]!=0:
				s+=" "
				s+=str(i+1)
				s+=" "
				s+=str(v[i+1])			
						
		#if it is a recipe for training.
		if r.name in liTrainingFiles:			
			trainingFile.write(s)
		else:
			testFile.write(s)
			
	trainingFile.close()
	testFile.close()

if __name__=="__main__": main()
