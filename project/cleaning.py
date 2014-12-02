import logging
import cPickle as pickle
import re

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

	#Change this to your br2 path
	baseDir = ""

	fl = open(baseDir+"stopwords.stop")
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