#!/usr/bin/python
import sys
import os
import random
import shutil
import cPickle as pickle

def partitionForDataSet():
	dataPath = "reviews/"
	
	trainingPath = "liTrainingFiles.pickle"
	testingPath = "liTestFiles.pickle"

	files = os.listdir(dataPath)	
	totalFiles = len(files)
	random.shuffle(files) #shuffle all the files,...
	
	oneFiles = []
	twoFiles = []
	threeFiles = []
	fourFiles = []
	for f in files:
		if f[0] == "1":
			oneFiles.append(f)
		elif f[0] == "2":
			twoFiles.append(f)
		elif f[0] == "3":
			threeFiles.append(f)
		elif f[0] == "4":
			fourFiles.append(f)		
	
	liTrainingFiles = []
	liTestFiles = []			
	lenOne = len(oneFiles)
	lenTwo = len(twoFiles)
	lenThree = len(threeFiles)
	lenFour = len(fourFiles)
	
	#we will use 4 parts for training and 1 part for testing...
	for i in range(lenOne):
		if i < (4*lenOne)/5:
			liTrainingFiles.append(oneFiles[i])
		else:
			liTestFiles.append(oneFiles[i])
	 

	for i in range(lenTwo):
		if i < (4*lenTwo)/5:
			liTrainingFiles.append(twoFiles[i])
		else:
			liTestFiles.append(twoFiles[i])			
			
	for i in range(lenThree):
		if i < (4*lenThree)/5:
			liTrainingFiles.append(threeFiles[i])
		else:
			liTestFiles.append(threeFiles[i])	 

	for i in range(lenFour):
		if i < (4*lenFour)/5:
			liTrainingFiles.append(fourFiles[i])
		else:
			liTestFiles.append(fourFiles[i])	

	p1 = open( trainingPath,"wb")
	pickle.dump(liTrainingFiles, p1)
	p1.close()
	
	p2 = open( testingPath,"wb")
	pickle.dump(liTestFiles, p2)
	p2.close()
		
#partitionForDataSet()
			
