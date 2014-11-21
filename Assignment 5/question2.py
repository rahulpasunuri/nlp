#!/usr/bin/python

liRules=[] #this will hold the list of all rules.
beta = {} #this variable will hold all inside probabilties.
#each element in beta will be a hash from  (j, p, q) to  pr
liNonTerminals=[] # this will hold the list of all unique non terminals
liWords=[]

class rule:
	def __init__(self, parent, liChildren, prob):
		self.parent = parent #this is the left hand side of a rule. 
		self.liChildren = liChildren #this is the list of children in the RHS.
		self.prob = prob # this is the probability of the rule.
		
def printRule(r):
	# print the rules in a neat format.
	print r.parent," ---> "," ".join(r.liChildren), " ", r.prob
	
def addRules():
	global liRules		
	liRules.append(rule("S", ["NP", "VP"],1.0))
	liRules.append(rule("NP", ["DET", "N"],0.4))
	liRules.append(rule("NP", ["N"],0.3))
	liRules.append(rule("NP", ["NP", "PP"],0.3))
	liRules.append(rule("VP", ["V", "NP"],0.8))
	liRules.append(rule("VP", ["V", "XP"],0.2))
	liRules.append(rule("PP", ["IN", "NP"],1.0))
	liRules.append(rule("XP", ["NP", "PP"],1.0))
	liRules.append(rule("DET", ["a"],1.0))
	liRules.append(rule("N", ["dog"],0.1))	
	liRules.append(rule("N", ["pizza"],0.2))
	liRules.append(rule("N", ["fork"],0.4))	
	liRules.append(rule("N", ["kitchen"],0.3))
	liRules.append(rule("V", ["ate"],1.0))	
	liRules.append(rule("IN", ["with"],0.4))
	liRules.append(rule("IN", ["in"],0.6))	

def printRules():
	global liRules		
	for r in liRules:
		printRule(r)
	
def computeSplit(nt, p, q):
	global beta		
	global liRules		
	global liNonTerminals
	global liWords

	prob = 0
	if p==q: #this is the init step where we find beta values for all the words (of length 0)
		#init beta..
		for r in liRules: # loop over all the rules.
			if len(r.liChildren)==1 and r.parent == nt:  #use only those rules with a matching parent and only have one symbol on RHS.
				if r.liChildren[0] in liNonTerminals:					
					probTemp = (r.prob*computeSplit(r.liChildren[0], p, p)) #do a recursive computation of the split.
					if probTemp!=0:
						prob+=probTemp
				elif r.liChildren[0] == liWords[p]:
					prob +=  r.prob	
		return prob
				
	# d is the split between p and q.
	for d in range(p,q):
		for r in liRules: # loop over all the rules.
			if r.parent == nt: # use only those rules with matching parents (left hand side non terminal)
				#ignore other rules..
				if len(r.liChildren)==2 and (r.liChildren[0], p, d) in beta and (r.liChildren[1], d+1, q) in beta: #case where rule has two children(R.H.S)
					prob += (r.prob) * beta[r.liChildren[0], p, d] * beta[r.liChildren[1], d+1, q]
				elif len(r.liChildren)==1 and r.liChildren[0] in liNonTerminals: #case where rule only has one children.
					probTemp = computeSplit(r.liChildren[0], p, q)
					if probTemp!=0:
						prob+=r.prob*probTemp
										
	return prob				

def main():		
	global beta
	global liRules
	global liNonTerminals
	global liWords
	addRules()
	print
	print "-"*30
	print "Printing the grammar"
	print "-"*30
	print
	
	printRules()
	sentence = "A dog ate pizza with a fork in a kitchen"
	liWords = [ a.lower() for a in sentence.split()] # convert all words to a lower case.
	
	beta = {} #this variable will hold all inside probabilties.
	#each element in beta will be a hash from  (j, p, q) to  prob, where j represents a symbol, p is the starting word and q is the ending word.
	
	#get the list of all non-terminals.
	liNonTerminals = list(set([ a.parent for a in liRules])) #set removes all the repeating non terminals...	
	

	
	size = len(liWords)
	for d in range(size): #calculate probabilities starting from small distances to large distances..
		for p in range(size): # p is the word index of the start
			q = p+d
			if q < size: #q is the end index.. note that q-p is the distance between them.
				for nt in liNonTerminals:
					beta[nt, p, q] = computeSplit(nt, p, q)
	print
	print "-"*40						
	print "Printing non-zero probabilities:"
	print "-"*40
	print
	for key in beta:
		if beta[key]!=0:
			print "beta_", key[0], "(",key[1],",", key[2], ")"  " = ", beta[key]
	
#Execution begins here
if __name__ == "__main__" : main()	
		
