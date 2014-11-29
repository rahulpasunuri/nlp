import logging
import cPickle as pickle
import re


def main():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	
	listOfReviews = []
	rawFile = open('someReviews.txt')
	for line in rawFile:
		line = line.lower()
		'''Removed all punctuation, 
		yet kept count of the number of numberOfExclamations
		as it may indicate positive sentiment. May or may not work as feature.
		Lets Try
		'''
		punctuationRemoved = processLine(line)
		punctuationRemoved = [word for word in punctuationRemoved if word != ' ']
		punctuationRemoved = removeStopWords(punctuationRemoved)
		listOfReviews.append(punctuationRemoved)
	
	for review in listOfReviews:
		for word in review:
			print type(word)

	writeObject = open('listOfListDump.pickle','wb')
	pickle.dump(listOfReviews,writeObject)

	writeObject.close()

def processForAnotherFile(line):
	line = line.lower()
	'''
	With this method, I will process lines coming from other files
	'''
	punctuationRemoved = processLine(line)
	punctuationRemoved = [word for word in punctuationRemoved if word != ' ']
	punctuationRemoved = removeStopWords(punctuationRemoved)

	return punctuationRemoved

def removeStopWords(splittedCleaned):
	fl = open("stopwordslist.txt")
	stoplist = []
	fullyCleaned = []
	for stopword in fl:
		temp = stopword
		if temp != " ": stoplist.append(temp[0:len(temp)-1])  
	for word in splittedCleaned:
		if word not in stoplist:
			fullyCleaned.append(word)		
	return fullyCleaned

def specialNot(word):
	regEx = ".*n't.*"
	regExObject = re.compile(regEx)
	if regExObject.match(word) != None:
		return True
	else:
		return False	

def splitOnSpaces(line):
	return line.split()

def processLine(line):
	punctuation = ". , ? ( ) \' \" : ; ! > < & @ #".split()
	splittedLine = splitOnSpaces(line)
	processedLine = []
	for word in splittedLine:
		if specialNot(word):
			processedLine.append(word)
			continue

		else:
			for char in punctuation:
				word = word.replace(char, '')
			processedLine.append(word)	
	return processedLine
		
def countNoOfExclamations(line):
	numberOfExclamations = 0
	for char in line:
		if char == '!':
			numberOfExclamations =+ 1
	return numberOfExclamations		

def countNoOfSentences(line):
	numberOfSentences = 0
	tokenizedWords = nltk.word_tokenize(line)
	return tokenizedWords

if __name__ == "__main__": main()