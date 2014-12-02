import os, re 
import Recipe, cleaning
from Recipe import Recipe
import cPickle as pickle

'''
This was the program I wrote to extract ratings and reviews as a list 
Each individual review and overall rating(From filename) is captured.
For each recipe , allReviewsDict will store a review as key and rating as value
This entire allReviewsDict will be used in the Recipe Datastrucutre to store 
allReviewsDict for all recipes.
'''

def main():

	#Change this to your br2 path
	baseDir = ""

	#Change to reviews/ for entire dataset
	reviewDirectory = baseDir+"temp/"
	
	#This dataset will be a list of recipe objects
	Dataset = []

	fileList = os.listdir(reviewDirectory)

	counter = 0
	for f in fileList:

		counter = 0
		currentFile = open(reviewDirectory+f)
		allReviewsListOfTuples = []
		ratingList = []
		reviewList = []	
		recipeName = getRecipeName(f)
		totalRating = getTotalRating(f)
		
		for line in currentFile:
			if line=="\n":
				continue
			if "Rating" in line:
				counter = counter+1
				rating = getReviewRating(line)
				ratingList.append(rating)
			else : 
				review = cleaning.processForAnotherFile(line)
				if review != []:
					reviewList.append(review)

		
		#Representing each review and its rating as a tuple
		for i in range(0,len(reviewList)):
			allReviewsListOfTuples.append((reviewList[i],ratingList[i]))
		RecipeObj = Recipe(name=recipeName, rating=totalRating, allReviews=allReviewsListOfTuples,numOfReviews= counter)
		Dataset.append(RecipeObj)

	print "Now opening pickle file dumping data"	
	pickleFile = open(baseDir+"ReviewsDataStructureDump.pickle", "wb")
	pickle.dump(Dataset, pickleFile)
	pickleFile.close()	
	print "Finished dumping pickle file"				

def getRecipeName(rawRecipeName):
	startIndex = rawRecipeName.rfind('_');
	endIndex = rawRecipeName.rfind('-');
	semiProcessed = rawRecipeName[startIndex+1:endIndex]
	processedName = semiProcessed.replace('-',' ')
	return processedName

def getReviewRating(line):
	regEx = "\d+"
	regExObj = re.compile(regEx)
	numberList = regExObj.findall(line)
	if len(numberList) == 1:
		return numberList[0]
	else:
		return ".".join(numberList)

def getTotalRating(fileName):
	regEx = "\d+"
	regExObj = re.compile(regEx)
	numberList = regExObj.findall(fileName)
	if len(numberList) == 3:
		rating = '.'.join(numberList[0:2])
	else:
		rating = '.'.join(numberList[0:1])	
	return rating

if __name__=="__main__": main()