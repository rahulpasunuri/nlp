from gensim import corpora, models

def main():
	s = 'abcd'
	print "s is "+s
	print type(s)
	uniS = unicode(s)
	print "uniS is "+uniS
	print type(uniS)

	listOfList = ['good', 'new', 'awesome']
	print type(listOfList[0][0])
	dictionary = corpora.Dictionary(listOfList)
	print dictionary
if __name__ == "__main__": main()