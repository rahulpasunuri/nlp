#!/usr/bin/python
import sys

def main():
	fileName = "results10.txt"
	testFile = "vectors/testVectors10.txt"
		
	predLabels = [float(a) for a in open(fileName, "r").readlines()]		
	actualLabels = [float(a.split()[0]) for a in open(testFile, "r").readlines()]
	
	numSamples = len(predLabels)

	correct = {}
	wrong = {}
		
	
	for i in range(numSamples):
		if predLabels[i] == actualLabels[i]:
			if actualLabels[i] in correct:
				correct[actualLabels[i]] += 1
			else:
				correct[actualLabels[i]] = 1
				
		else:
			if actualLabels[i] in wrong:
				wrong[actualLabels[i]] += 1
			else:
				wrong[actualLabels[i]] = 1
				
				
	totalLabels = [k for k in correct]
	for k in wrong:
		if k not in totalLabels:
			totalLabels.append(k)
	
	for label in totalLabels:
		c=0
		w=0
		if label in correct:
			c = correct[label]
		if label in wrong:
			w = wrong[label]
			
			
		print "Number of Correct predictions for label - ",label, " is ", c
		print "Number of Wrong predictions for label - ",label, " is ", w	
		print 
		
if __name__=="__main__": main()
