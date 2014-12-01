class Recipe:
	def __init__(self, name=None, rating=0, allReviews=0, numOfReviews=0, topicProbabilities=None):
		self.name = name
		self.rating = rating
		self.numOfReviews = numOfReviews
		self.allReviews = allReviews		
		self.topicProbabilities = topicProbabilities
'''
Explanation of this Object : 
name = Name of Recipe
rating = Overall Rating of Recipe
numOfReviews = Total Number of Reviews for this Recipe (Can be used as a feature )
allReviews = This is a list of tuples, each tuple consists of
				(review_as_a_bag_of_words, the_rating_for_that_review)

topicProbabilities = This is a list of list of probabilites of each topic as a tuple, 
						[(topic_number, its_probability), 
							(topic_number, its_probability), ...]
					#Iterate over allreviews using range() and use the index 
						to access topic for the corresponding review.				
					(I was going to keep only the topic with the highest probability,
						but I thought it would be useful for you to have all probabilites 
						at your disposal.)																		
'''															 


'''
changes suggested by Rahul:

1) remove bag of words from allReviews, and so allReviews would just be a simple list of review ratings...
2) elements inside the topic probabilities must be a dictionary with key as topic number and value would be the probability...

Changes implemented by Huzefa :)
'''


