class WordsTagsProbability:
	def __init__(self, word=None, tag1=None, tag2=None, probability=None):
		'''
		The objects of this class will hold the word|tag probability or
		tag1|tag2 probability. 
		'''
		self.word=word
		self.tag1=tag1
		self.tag2=tag2
		self.probability=probability/100

