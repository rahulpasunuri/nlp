import pickle
def main():
	readObject = open("listOfListDump",'r')
	listOfLists = pickle.load(readObject)

	print listOfLists
if __name__=="__main__": main()	