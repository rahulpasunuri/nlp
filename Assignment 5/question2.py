#!/usr/bin/python

liRules=[] #this will hold the list of all rules.

class rule:
	def __init__(self, parent, liChildren, prob):
		self.parent = parent #this is the left hand side of a rule. 
		self.liChildren = liChildren #this is the list of children in the RHS.
		self.prob = prob # this is the probability of the rule.
		
def printRule(r):
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
	
def main():		
	addRules()
	printRules()
	print
	
	
#Execution begins here
if __name__ == "__main__" : main()	
		
