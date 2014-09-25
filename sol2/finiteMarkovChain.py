#!/usr/bin/python
import sys

def matrixMultiplication(a,b):
	# a is 1*4 matirix 	#b is 4*4 matrix
	result=[]
	for i in range(0,4):
		val=0.0
		for j in range(0,4):
			val = val + (a[j] * b[j][i])

		result.append(val)
	return result

def main():
	#here the first column is for state 0, 2nd for state 1, 3rd for state 2, and 4th for state 3.
	v = [0.5, 0.3, 0.2, 0.0]
	#below matrix is the transition matrix
	P=[[0.2,0.5,0.2,0.1],[0.3,0.4,0.2,0.1],[0.1,0.3,0.4,0.2],[0.1,0.1,0.3,0.5]]
		
	temp=v
	l=len(v)
	for i in range(0,l):
		# we need 4 multiplications
		temp=matrixMultiplication(temp,P)
	
	print
	print "Printing the probability vector for each state after 4 steps"
	print temp
	
	print
	
	print "By, this the probability that 3 lines would be busy after 4 steps is:"
	print temp[3]
	
	print
	
	maxProbability=0
	mostLikely=[]
	for i in range(0,l):
		if(temp[i]==maxProbability):
			mostLikely.add(i)
		elif(temp[i]>maxProbability):
			mostLikely=[]
			mostLikely.append(i)
			maxProbability=temp[i]
	print "States with maximum probability are (note that there can be more than one state here.):"
	print mostLikely
			
			
	


#Execution begins here
if __name__ == "__main__" : main()	
		
