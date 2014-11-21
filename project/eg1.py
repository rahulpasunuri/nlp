import os
import io

def main():
	reviewDirectory = "nyu\\PROJECTS\\Epicurious\\DATA\\reviews\\"
	ratingList = []
	reviewList = []	

	fileList = os.listdir(reviewDirectory)
	
	for f in fileList:
		currentFile = io.open(reviewDirectory+f,newline="",encoding="cp437")
		recipeName = getRecipeName(f)
		print
		for line in currentFile:
			if line=="\n":
				continue
			if "Rating" in line:
				rating = line[len(line)-2]
				print  recipeName+" = "+rating
				try:
					rating = int(rating)
				except :
					continue	
				ratingList.append(int(rating))
			else : 
				try:
					review = line.encode('utf-8')
					reviewList.append(str(review))
				except :
					ratingList.pop();		
					continue

def getRecipeName(rawRecipeName):
	startIndex = rawRecipeName.rfind('_');
	endIndex = rawRecipeName.rfind('-');
	semiProcessed = rawRecipeName[startIndex+1:endIndex]
	processedName = semiProcessed.replace('-',' ')
	return processedName


if __name__=="__main__": main()		

	