#!/usr/bin/python
import sys
from math import *

trigramCounts={}
bigramCounts={}
conditionalProbabilities={}

trigramCounts2={}
bigramCounts2={}
conditionalProbabilities2={}




def nGramTrain():
	f1=open("hw2-train.txt", 'r')
	sentences=f1.readlines()	
	f1.close()
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
	
	#compute conditional probabilities of training set
	print "Printing conditional probabilities of the Training set"
	for key in trigramCounts:
		conditionalProbabilities[key] = float(trigramCounts[key])/bigramCounts[(key[0]),key[1]]
		print "Conditional Probability of \""+key[2]+"\" given \""+key[1] +"\" and \""+key[0]+"\" is: "+str(conditionalProbabilities[key])
		

def nGramTest():
	f2=open("hw2-test.txt", 'r')
	sentences2=f2.readlines()	
	f2.close()
	sentences2=[modifyString(s).split() for s in sentences2]

	#compute bigram counts
	for s in sentences2:
		numWords=len(s)
		for i in range(0,numWords-1):
			if s[i]== "</end>":
				break
			if (s[i],s[i+1]) in bigramCounts2:
				bigramCounts2[(s[i],s[i+1])] +=1
			else:
				bigramCounts2[(s[i],s[i+1])] =1
	#print bigramCounts
	
	#compute trigram counts
	for s in sentences2:
		numWords=len(s)
		for i in range(0,numWords):
			if s[i+1] == "</end>":
				break
			else:
				if (s[i],s[i+1],s[i+2]) in trigramCounts2:
					trigramCounts2[(s[i],s[i+1],s[i+2])]+=1
				else:
					trigramCounts2[(s[i],s[i+1],s[i+2])]=1

	
	#compute conditional probabilities of training set
	print "Printing conditional probabilities of the Test set"
	for key in trigramCounts2:
		conditionalProbabilities2[key] = float(trigramCounts2[key])/bigramCounts2[(key[0]),key[1]]
		print "Conditional Probability of \""+key[2]+"\" given \""+key[1] +"\" and \""+key[0]+"\" is: "+str(conditionalProbabilities2[key])
		


def computePerplexity():
	#computing preplexities......
	f2=open("hw2-test.txt", 'r')		
	#start reading test set now..
	testLines = [modifyString(s).split() for s in f2.readlines()]
	
	print "\n\nPrinting Perplexities per line:"
	totalCount=0
	totalPerplexity=1
	for line in testLines:
		numWords=len(line)
		perplexity=1
		count=0	
		#print " ".join(line)+":"
		for i in range(0,numWords):
			if(line[i+1]=="</end>"):
				break
			if (line[i],line[i+1],line[i+2]) in conditionalProbabilities:		
				perplexity*= (conditionalProbabilities[(line[0],line[1],line[2])])
			else:
				perplexity*=(0.0001)
			count+=1
		if count!=0:
			totalCount+=count
			totalPerplexity*=perplexity
			perplexity = pow(perplexity, float(-1)/count)				
			print " ".join(line)+" : "+str(perplexity)
	print "total count is "+str(totalCount)
	totalPerplexity = pow(totalPerplexity, float(-1)/totalCount)				
	print "\nTotal Perplexity of test set based on training set: "+str(totalPerplexity)+"\n"
	

	
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
	nGramTrain()
	nGramTest()											
	computePerplexity()
	
#Execution begins here
if __name__ == "__main__" : main()	
		
