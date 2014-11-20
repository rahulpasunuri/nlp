import os
import io

def main():
	reviewDirectory = "nyu\\PROJECTS\\Epicurious\\DATA\\reviews\\"
	fileList = os.listdir(reviewDirectory)
	for f in fileList:
		currentFile = io.open(reviewDirectory+f,newline="")
		recipeName = getRecipeName(f)
		print
		print recipeName
		for line in currentFile:
			if line=="\n":
				continue
			print line.encode('utf-8')
			print "-------------"
		

def getRecipeName(rawRecipeName):
	startIndex = rawRecipeName.rfind('_');
	endIndex = rawRecipeName.rfind('-');
	semiProcessed = rawRecipeName[startIndex+1:endIndex]
	processedName = semiProcessed.replace('-',' ')
	return processedName


if __name__=="__main__": main()		

	