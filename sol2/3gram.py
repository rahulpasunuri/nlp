#!/usr/bin/python
import sys
from math import *

trigramCounts={}
bigramCounts={}
conditionalProbabilities={}
	
def modifyString(s):
	s=s.replace('.','')
	s=s.replace(',',"")
	s=s.replace("?","")
	s=s.replace("\"","")
	s=s.replace("\'","")
	s=s.replace("-","")	
	s= " <s1> <s2> "+s+" </end>"
	return s
	
def main():
	#(w1,w2,w3,count)--is the structure of the trigrams
	f1=open("hw2-train.txt", 'r')
	f2=open("hw2-test.txt", 'r')
	sentences=f1.readlines()	
	sentences=[modifyString(s).split() for s in sentences]

	#compute bigram counts
	for s in sentences:
		numWords=len(s)
		for i in range(0,numWords-1):
			if s[i]== "</end>":
				break
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
	
	#start reading test set now..
	testLines = [modifyString(s).split() for s in f2.readlines()]
	
	for line in testLines:
		numWords=len(line)
		perplexity=1
		count=0	
		for i in range(0,numWords):
			if(line[i+1]=="</end>"):
				break
			if (line[0],line[1],line[2]) in conditionalProbabilities:
				perplexity*= (conditionalProbabilities[(line[0],line[1],line[2])])
			else:
				perplexity*=(0.001)
			count+=1
		if count!=0:
			perplexity = pow(perplexity, float(-1)/count)	
			print perplexity			
	
	
#Execution begins here
if __name__ == "__main__" : main()	
		
