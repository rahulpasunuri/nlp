#!usr/bin/python
import sys
import WordsTagsProbability
import math

def calculate(sentence, tagSequence,wordsGivenTags, tagsGivenTags) :

	previousTag = None #Used to keep track of the preceding word 

	#just storing the logs separately for simplicity
	logTags = 0 
	logWord = 0

	log0Flag = False #This will be used to detect if a probability is 0

	#iterate over the entire given sequence
	for index, tag in enumerate(tagSequence):
		#Marks start of sentence
		if tag == "S":
			previousTag = tag
			continue
 	
		print "From state "+previousTag+" to state "+tag	
	
		for temp in tagsGivenTags:
			if temp.tag1==tag and temp.tag2 == previousTag:
				if temp.probability == 0: 
					log0Flag = True
					break
				else:
					print "Recording probability for the tag "+tag+ " given the probabaility of "+previousTag
					logTags = logTags + math.log10(temp.probability)

		for temp in wordsGivenTags:
			if tag == "E" : continue

			if temp.word == sentence[index] and temp.tag2 == tag:
				if temp.probability == 0: 
					log0Flag = True
					break
				else:
					print "Recording probability of word "+sentence[index]+" given the probability of "+tag
					logWord = logWord + math.log10(temp.probability)
		if log0Flag == True : break		
		previousTag = tag		
	
	if not log0Flag:	
		totalValues = logTags+logWord	
		print ""
		print ""
		print "Log values for logTags: " +str(logTags)
		print "Log values for logWord: "+str(logWord)
		print "Antilog values for tags: "+str(antilog(logTags))
		print "Antilog values for words : "+str(antilog(logWord))
		print "Total probability : "+str(antilog(totalValues))
	else: 
		print ""
		print ""
		print "Error : "
		print "One or more of the probabilities is 0, hence the answer is 0"	
	
def main():
	
	'''
	Painstakingly writing all the values for probabilities
	'''

	wordsGivenTags = []
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("time",None,"NN",7.0727))
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("time",None,"VB",0.0005))
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("time",None,"JJ",0))
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("flies",None,"VBZ",0.4754))
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("flies",None,"NNS",0.1610))
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("like",None,"IN",2.6512))
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("like",None,"VB",2.8413))
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("like",None,"RB",0.5086))
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("an",None,"DT",1.4192))
	wordsGivenTags.append(WordsTagsProbability.WordsTagsProbability("arrow",None,"NN",0.0215))

	tagsGivenTags = []
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"NN","S",0.6823))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"VB","S",0.5294))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"JJ","S",0.8033))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"VBZ","NN",3.9005))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"VBZ","VB",0.0566))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"VBZ","JJ",2.0934))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"NNS","NN",1.6076))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"NNS","VB",0.6566))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"NNS","JJ",2.4383))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"IN","VBZ",8.5862))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"IN","NNS",21.8302))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"VB","VBZ",0.7002))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"VB","NNS",11.1406))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"RB","VBZ",15.0350))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"RB","NNS",6.4721))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"DT","IN",31.4263))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"DT","VB",15.2649))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"DT","RB",5.3113))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"NN","DT",38.0170))
	tagsGivenTags.append(WordsTagsProbability.WordsTagsProbability(None,"E","NN",0.2069))

	#Storing the tag sequence as an iterable list. Easy to work with
	tagList1 = ["S","VB","NNS","IN","DT","NN","E"] #Sequence 1
	tagList2 = ["S","JJ","VBZ","VB","DT","NN","E"] #Sequence 2
	sentence = ["S","time","flies","like","an","arrow","E"] #Given Sentence

	calculate(sentence, tagList1,wordsGivenTags,tagsGivenTags)
	calculate(sentence, tagList2,wordsGivenTags,tagsGivenTags)

	#The output is given below.
def antilog(logvalues):
	return 10 ** logvalues

if __name__ == "__main__": main()	


'''
Output: 

From state S to state VB
Recording probability for the tag VB given the probabaility of S
Recording probability of word time given the probability of VB
From state VB to state NNS
Recording probability for the tag NNS given the probabaility of VB
Recording probability of word flies given the probability of NNS
From state NNS to state IN
Recording probability for the tag IN given the probabaility of NNS
Recording probability of word like given the probability of IN
From state IN to state DT
Recording probability for the tag DT given the probabaility of IN
Recording probability of word an given the probability of DT
From state DT to state NN
Recording probability for the tag NN given the probabaility of DT
Recording probability of word arrow given the probability of NN
From state NN to state E
Recording probability for the tag E given the probabaility of NN

Log values for logTags: -8.72682588457
Log values for logWord: -15.1862795662
Antilog values for tags: 1.8757463733e-09
Antilog values for words : 6.51209059648e-16
Total probability : 1.22150303189e-24

For the second sequence
From state S to state JJ
Recording probability for the tag JJ given the probabaility of S

Error : 
One or more of the probabilities is 0, hence the answer is 0

'''