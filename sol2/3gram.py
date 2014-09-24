#!/usr/bin/python
import sys


trigramCounts={}
bigramCounts={}
conditionalProbabilities={}

def main():
	#(w1,w2,w3,count)--is the structure of the trigrams
	f=open("hw-train.txt", 'r')
	sentences=f.readlines()	
	sentences=[(" <s1> <s2> "+s+" </s2> </s1> ").replace('.','').replace(',',"").split() for s in sentences]

	#compute bigram counts
	for s in sentences:
		numWords=len(s)
		for i in range(0,numWords-1):
			if (s[i],s[i+1]) in bigramCounts:
				bigramCounts[(s[i],s[i+1])] +=1
			else:
				bigramCounts[(s[i],s[i+1])] =1
	#print bigramCounts
	
	#compute trigram counts
	for s in sentences:
		numWords=len(s)
		for i in range(0,numWords):
			if s[i] == "</s2>":
				break
			else:
				if (s[i],s[i+1],s[i+2]) in trigramCounts:
					trigramCounts[(s[i],s[i+1],s[i+2])]+=1
				else:
					trigramCounts[(s[i],s[i+1],s[i+2])]=1
	#print "Printing trigram counts"
	#print trigramCounts
	
	#compute conditional probabilities
	for key in trigramCounts:
		conditionalProbabilities[key] = float(trigramCounts[key])/bigramCounts[(key[0]),key[1]]
	
	#compute probabilities on the training set

#Execution begins here
if __name__ == "__main__" : main()	
		
