#!/usr/bin/python
import cPickle as pickle

def main():
	ldaPicklePath = "LDAProcessed.pickle"
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
	
	print "Total Recipes is ", len(recipes)
	
	
	if len(recipes)<0:
		print "No recipes found"
		exit()
	
	#get all the list of topics..
	liTopics = []
	numReviews = 0
	for r in recipes:
		numReviews += r.numOfReviews
		for tp in r.topicProbabilities:
			for key in tp:
				if key not in liTopics:
					liTopics.append(key)

	print "Total number of reviews is ", numReviews
	
	liTopics.sort()																		
	
	for r in recipes:
		if len(r.topicProbabilities) == r.numOfReviews:
			v = [] #this is the data vector
			v.append(float(r.rating)) # first element of the vector is rating...
			v.extend([0 for a in liTopics]) #init values of feature topics as 0.
			for j in range(r.numOfReviews):
			
				rating = r.reviewRatings[j]
				topicDictionary = r.topicProbabilities[j]					
			
				sum1= 0
				#normalize the topic dict first..
				for key in topicDictionary:
					sum1 +=topicDictionary[key]
			
				for key in topicDictionary:
					topicDictionary[key] = topicDictionary[key]/sum1	
			
				for i in range(len(liTopics)):
					if liTopics[i] in topicDictionary:
						v[i+1] += topicDictionary[liTopics[i]] * float(rating)
						
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
				s+=":"
				s+=str(v[i+1])			
				
		s+="\n"		
		#if it is a recipe for training.
		if r.name in liTrainingFiles:			
			trainingFile.write(s)
		else:
			testFile.write(s)
			
	trainingFile.close()
	testFile.close()

if __name__=="__main__": main()
