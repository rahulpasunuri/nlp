#!usr/bin/python
import sys

def main():
	
	#It would have been easier, if we had these values as a csv file
	transitionMatrix = dict()

	transitionMatrix[("DT","DT")] = 0.03
	transitionMatrix[("DT","JJ")] = 0.42
	transitionMatrix[("DT","NN")] = 0.5
	transitionMatrix[("DT","VB")] = 0.05

	transitionMatrix[("JJ","DT")] = 0.01
	transitionMatrix[("JJ","JJ")] = 0.25
	transitionMatrix[("JJ","NN")] = 0.65
	transitionMatrix[("JJ","VB")] = 0.09

	transitionMatrix[("NN","DT")] = 0.07
	transitionMatrix[("NN","JJ")] = 0.03
	transitionMatrix[("NN","NN")] = 0.15
	transitionMatrix[("NN","VB")] = 0.75

	transitionMatrix[("VB","DT")] = 0.3
	transitionMatrix[("VB","JJ")] = 0.25
	transitionMatrix[("VB","NN")] = 0.15
	transitionMatrix[("VB","VB")] = 0.3

	emitMatrix = dict()

	emitMatrix[("a","DT")] = 0.85
	emitMatrix[("a","JJ")] = 0.05
	emitMatrix[("a","NN")] = 0.03
	emitMatrix[("a","VB")] = 0.05

	emitMatrix[("myth","DT")] = 0.01
	emitMatrix[("myth","JJ")] = 0.1
	emitMatrix[("myth","NN")] = 0.45
	emitMatrix[("myth","VB")] = 0.1

	emitMatrix[("is","DT")] = 0.02
	emitMatrix[("is","JJ")] = 0.02
	emitMatrix[("is","NN")] = 0.02
	emitMatrix[("is","VB")] = 0.6

	emitMatrix[("female","DT")] = 0.01
	emitMatrix[("female","JJ")] = 0.6
	emitMatrix[("female","NN")] = 0.25
	emitMatrix[("female","VB")] = 0.05

	emitMatrix[("moth","DT")] = 0.12
	emitMatrix[("moth","JJ")] = 0.13
	emitMatrix[("moth","NN")] = 0.25
	emitMatrix[("moth","VB")] = 0.2

	sentence = "a myth is a female moth"
	splitSent = sentence.split(" ")

	#Initial Vector
	vector = [0.45, 0.35, 0.15, 0.05]

	#Alpha is a dictionary of Dictionaries
	alpha =dict()
	temp = dict()
	#initial alpha 1
	temp['DT'] = vector[0]*emitMatrix[(splitSent[0],"DT")]
	temp['JJ'] = vector[1]*emitMatrix[(splitSent[0],"JJ")]
	temp['NN'] = vector[2]*emitMatrix[(splitSent[0],"NN")]
	temp['VB'] = vector[3]*emitMatrix[(splitSent[0],"VB")]
	alpha[1] = temp

	#Beta is also a dict of dict
	beta = dict()
	#Initial Beta
	beta[6] = {'DT':1, 'JJ':1, 'NN':1, 'VB':1}

	#We now use the formula we learnt to calculate all alphas
	#We are calculating all the alphas, not just the ones required to be calculated. 
	for i in range(2,len(splitSent)+1):
		temp = dict()
		temp['DT'] = (alpha[i-1]['DT']*transitionMatrix[('DT','DT')]+alpha[i-1]['JJ']*transitionMatrix[('JJ','DT')]+alpha[i-1]['NN']*transitionMatrix[('NN','DT')]+alpha[i-1]['VB']*transitionMatrix[('VB','DT')])*emitMatrix[(splitSent[i-1],'DT')]
		temp['JJ'] = (alpha[i-1]['DT']*transitionMatrix[('DT','JJ')]+alpha[i-1]['JJ']*transitionMatrix[('JJ','JJ')]+alpha[i-1]['NN']*transitionMatrix[('NN','JJ')]+alpha[i-1]['VB']*transitionMatrix[('VB','JJ')])*emitMatrix[(splitSent[i-1],'JJ')]
		temp['NN'] = (alpha[i-1]['DT']*transitionMatrix[('DT','NN')]+alpha[i-1]['JJ']*transitionMatrix[('JJ','NN')]+alpha[i-1]['NN']*transitionMatrix[('NN','NN')]+alpha[i-1]['VB']*transitionMatrix[('VB','NN')])*emitMatrix[(splitSent[i-1],'NN')]
		temp['VB'] = (alpha[i-1]['DT']*transitionMatrix[('DT','VB')]+alpha[i-1]['JJ']*transitionMatrix[('JJ','VB')]+alpha[i-1]['NN']*transitionMatrix[('NN','VB')]+alpha[i-1]['VB']*transitionMatrix[('VB','VB')])*emitMatrix[(splitSent[i-1],'VB')]
		alpha[i] = temp
	
	#Now we calculate all Beta in a similar manner to the alphas
	for i in range(5,0,-1):
		temp = dict()
		temp['DT'] = (beta[i+1]['DT']*transitionMatrix[('DT','DT')]+beta[i+1]['JJ']*transitionMatrix[('DT','JJ')]+beta[i+1]['NN']*transitionMatrix[('DT','NN')]+beta[i+1]['VB']*transitionMatrix[('DT','VB')])*emitMatrix[(splitSent[i-1],'DT')]
		temp['JJ'] = (beta[i+1]['DT']*transitionMatrix[('JJ','DT')]+beta[i+1]['JJ']*transitionMatrix[('JJ','JJ')]+beta[i+1]['NN']*transitionMatrix[('JJ','NN')]+beta[i+1]['VB']*transitionMatrix[('JJ','VB')])*emitMatrix[(splitSent[i-1],'JJ')]
		temp['NN'] = (beta[i+1]['DT']*transitionMatrix[('NN','DT')]+beta[i+1]['JJ']*transitionMatrix[('NN','JJ')]+beta[i+1]['NN']*transitionMatrix[('NN','NN')]+beta[i+1]['VB']*transitionMatrix[('NN','VB')])*emitMatrix[(splitSent[i-1],'NN')]
		temp['VB'] = (beta[i+1]['DT']*transitionMatrix[('VB','DT')]+beta[i+1]['JJ']*transitionMatrix[('VB','JJ')]+beta[i+1]['NN']*transitionMatrix[('VB','NN')]+beta[i+1]['VB']*transitionMatrix[('VB','VB')])*emitMatrix[(splitSent[i-1],'VB')]
		beta[i] = temp

	#Now we print all the calculated values.
	# Since we have all the values of alpha's and beta's calculated, you can change the key in output below to get alpha and beta of your wish	
	print ""
	print "Alpha 4 NN "+str(alpha[4]['NN'])
	print "Alpha 3 VB "+str(alpha[3]['VB'])
	print "Alpha 1 DT "+str(alpha[1]['DT'])
	
	print ""
	print "Beta 4 NN "+str(beta[4]['NN'])
	print "Beta 3 NN "+str(beta[3]['NN'])

if __name__ == "__main__": main()	

'''
Output :


Alpha 4 NN 0.00019905247002
Alpha 3 VB 0.042590091
Alpha 1 DT 0.3825

Beta 4 NN 0.002811
Beta 3 NN 0.000624033

'''