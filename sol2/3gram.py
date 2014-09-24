#!/usr/bin/python
import sys


trigramCounts={}
bigramCounts={}
conditionalProbabilities={}

def pruneText(s):
	s=s.replace('.','')
	s=s.replace(',',"")
	s=s.replace("?","")
	s=s.replace("\"","")
	s=s.replace("\'","")
	s=s.replace("-","")	
	return s
	
	
	
def main():
	#(w1,w2,w3,count)--is the structure of the trigrams
	f1=open("hw2-train.txt", 'r')
	f1=open("hw2-test.txt", 'r')
	sentences=f1.readlines()	
	sentences=[(" <s1> <s2> "+pruneText(s)+" </end>").split() for s in sentences]

	#compute bigram counts
	for s in sentences:
		numWords=len(s)
		for i in range(0,numWords-1):
			if s[i]== "</end>":
				break:
			if (s[i],s[i+1]) in bigramCounts:
				bigramCounts[(s[i],s[i+1])] +=1
			else:
				bigramCounts[(s[i],s[i+1])] =1
	#print bigramCounts
	
	#compute trigram counts
	for s in sentences:
		numWords=len(s)
		for i in range(0,numWords):
			if s[i+1] == "</end>":
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
	#print conditionalProbabilities
	#compute probabilities on the training set

#Execution begins here
if __name__ == "__main__" : main()	
		
