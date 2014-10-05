#!usr/bin/python
import sys
import WordsTagsProbability

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

	print len(wordsGivenTags)


if __name__ == "__main__": main()	