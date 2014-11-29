import pickle

def main():
	pickleFile = open("ReviewsDataStructureDump.txt","rb")
	allReviews = pickle.load(pickleFile)

	for obj in allReviews:
		print obj.name+" --> "+str(obj.rating)+ " Number of Reviews --> "+ str(obj.numOfReviews)
		print obj.allReviews

if __name__ == "__main__": main()	