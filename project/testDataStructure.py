import pickle

def main():
	pickleFile = open("LDAProcessed.pickle","rb")
	allReviews = pickle.load(pickleFile)

	for obj in allReviews:
		print obj.name+" --> "+str(obj.rating)+ " Number of Reviews --> "+ str(obj.numOfReviews)
		#print obj.topicProbabilities
		#print obj.reviewRatings
		print "Length of topic topicProbabilities : "+str(len(obj.topicProbabilities))
		print "Length of review rating: "+str(len(obj.reviewRatings))
		print "*"*40
		if len(obj.topicProbabilities) != obj.numOfReviews:
			print "Error"
		



if __name__ == "__main__": main()	
