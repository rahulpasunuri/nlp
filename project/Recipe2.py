class Recipe2:
	def __init__(self, name=None, rating=0, reviewRatings=0, numOfReviews=0, topicProbabilities=None):
		self.name = name
		self.rating = rating
		self.numOfReviews = numOfReviews
		self.reviewRatings = reviewRatings		
		self.topicProbabilities = topicProbabilities

'''
reviewRatings is simply the list of all ratings for individual reviewRatings
topicProbabilities is now a list of Dictionary of Topic and probability for each review.
''' 		