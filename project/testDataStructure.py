import pickle

def main():
	pickleFile = open("LDAProcessed.pickle","rb")
	allReviews = pickle.load(pickleFile)

	for obj in allReviews:
		print obj.name+" --> "+str(obj.rating)+ " Number of Reviews --> "+ str(obj.numOfReviews)
		print obj.topicProbabilities
		print obj.reviewRatings

if __name__ == "__main__": main()	
