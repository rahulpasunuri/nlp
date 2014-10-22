#!usr/bin/python
import sys
from EmitState import EmitState
from StateToState import StateToState

def main():
	print "Hello World"

	transitionMatrix = []
	emitMatrix = []

	transitionMatrix.append(StateToState(fromState="DT",toState="DT",prob=0.03))
	transitionMatrix.append(StateToState(fromState="DT",toState="JJ",prob=0.42))
	transitionMatrix.append(StateToState(fromState="DT",toState="NN",prob=0.5))
	transitionMatrix.append(StateToState(fromState="DT",toState="VB",prob=0.05))

	transitionMatrix.append(StateToState(fromState="JJ",toState="DT",prob=0.01))
	transitionMatrix.append(StateToState(fromState="JJ",toState="JJ",prob=0.25))
	transitionMatrix.append(StateToState(fromState="JJ",toState="NN",prob=0.65))
	transitionMatrix.append(StateToState(fromState="JJ",toState="VB",prob=0.09))
	
	transitionMatrix.append(StateToState(fromState="NN",toState="DT",prob=0.07))
	transitionMatrix.append(StateToState(fromState="NN",toState="JJ",prob=0.03))
	transitionMatrix.append(StateToState(fromState="NN",toState="NN",prob=0.15))
	transitionMatrix.append(StateToState(fromState="NN",toState="VB",prob=0.75))

	transitionMatrix.append(StateToState(fromState="VB",toState="DT",prob=0.3))
	transitionMatrix.append(StateToState(fromState="VB",toState="JJ",prob=0.25))
	transitionMatrix.append(StateToState(fromState="VB",toState="NN",prob=0.15))
	transitionMatrix.append(StateToState(fromState="VB",toState="VB",prob=0.3))

	emitMatrix.append(EmitState(word="a",state="DT",prob=0.85))
	emitMatrix.append(EmitState(word="a",state="JJ",prob=0.05))
	emitMatrix.append(EmitState(word="a",state="NN",prob=0.03))
	emitMatrix.append(EmitState(word="a",state="VB",prob=0.05))

	emitMatrix.append(EmitState(word="myth",state="DT",prob=0.01))
	emitMatrix.append(EmitState(word="myth",state="JJ",prob=0.1))
	emitMatrix.append(EmitState(word="myth",state="NN",prob=0.45))
	emitMatrix.append(EmitState(word="myth",state="VB",prob=0.1))

	emitMatrix.append(EmitState(word="is",state="DT",prob=0.02))
	emitMatrix.append(EmitState(word="is",state="JJ",prob=0.02))
	emitMatrix.append(EmitState(word="is",state="NN",prob=0.02))
	emitMatrix.append(EmitState(word="is",state="VB",prob=0.6))

	emitMatrix.append(EmitState(word="female",state="DT",prob=0.01))
	emitMatrix.append(EmitState(word="female",state="JJ",prob=0.6))
	emitMatrix.append(EmitState(word="female",state="NN",prob=0.25))
	emitMatrix.append(EmitState(word="female",state="VB",prob=0.05))

	emitMatrix.append(EmitState(word="moth",state="DT",prob=0.12))
	emitMatrix.append(EmitState(word="moth",state="JJ",prob=0.13))
	emitMatrix.append(EmitState(word="moth",state="NN",prob=0.25))
	emitMatrix.append(EmitState(word="moth",state="VB",prob=0.2))

	sentence = "a myth is a female moth"
	split = sentence.split(' ')
	print split
	initial = [0.45,0.35,0.15,0.05] 
	firstIteration = dict()
	for emit in emitMatrix:
		if(emit.word==split[0]):
			if(emit.state=="DT"):
				firstIteration['DT'] = initial[0] * emit.prob
				print emit.word+" with DT has prob = "+str(emit.prob)
			if(emit.state=="JJ"):
				firstIteration['JJ'] = initial[1] * emit.prob
				print emit.word+" with JJ has prob = "+str(emit.prob)
			if(emit.state=="NN"):
				firstIteration['NN'] = initial[2] * emit.prob
				print emit.word+" with NN has prob = "+str(emit.prob)
			if(emit.state=="VB"):firstIteration['VB']= initial[3] * emit.prob

	alpha[0] = firstIteration

	for i in range(1,len(split)):
		for emit in emitMatrix:
			for transmit in transitionMatrix:
				if()
if __name__ == "__main__":main()	