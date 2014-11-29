import gensim
import cleaning
import Recipe
import pickle

'''
In this program we do the actual LDA, and give a certain output.
The datastucture used will be a list of Recipe Object which will be read 
from a pickle file, which has been already created
This has been done to increase modularity and reduce points of failures'''

def main(): 
	pickleFile = open("ReviewsDataStructureDump.txt","rb")
	ReviewObjList = pickle.load(pickleFile)
	#This bigListOfReviews contains all the reviews
	bigListOfREviews = []

	for obj in ReviewObjList:
		

if __name__=="__main__": main()	
