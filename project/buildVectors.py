#!/usr/bin/python
import cPickle as pickle

def main():
	#ldaPicklePath = "LDAProcessed.pickle"
	ldaPicklePath = "ldaPickles/LDAProcessed5.pickle"
	#ldaPicklePath = "ldaPickles/LDAProcessed10.pickle"
	
	trainf = open("liTrainingFiles.pickle","rb")	
	testf = open("liTestFiles.pickle","rb")
	trainingFile = open("trainVectors5.txt","w")
	testFile = open("testVectors5.txt","w")
	
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
	
	oneRating = []
	twoRating = []
	threeRating = []
	fourRating = []
	
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
	errors = 0
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
		else:
			errors+=1		
			continue
			
		#normalize the data vector now..
		sum1 = 0
		
		for i in range(len(liTopics)):
			sum1+= v[i+1]

		if sum1 == 0:
			continue

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


		if r.rating == "1":
			oneRating.append(s)
		elif r.rating == "2":
			twoRating.append(s)
		elif r.rating == "3":
			threeRating.append(s)
		elif r.rating == "4":
			fourRating.append(s)
	
	lenOne = len(oneRating)
	lenTwo = len(twoRating)
	lenThree = len(threeRating)
	lenFour = len(fourRating)
			
	for i in range(lenOne):
		if i < 	(4*lenOne)/5:
			trainingFile.write(oneRating[i])
		else:
			testFile.write(oneRating[i])									

	for i in range(lenTwo):
		if i < 	(4*lenTwo)/5:
			trainingFile.write(twoRating[i])
		else:
			testFile.write(twoRating[i])									
						
	for i in range(lenThree):
		if i < 	(4*lenThree)/5:
			trainingFile.write(threeRating[i])
		else:
			testFile.write(threeRating[i])									
			
	for i in range(lenFour):
		if i < 	(4*lenFour)/5:
			trainingFile.write(fourRating[i])
		else:
			testFile.write(fourRating[i])												

	print "Errors are ", errors
	
	trainingFile.close()
	testFile.close()

if __name__=="__main__": main()
