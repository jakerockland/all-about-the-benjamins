class Interpreter (object):
	# This class is the "Bayesian Interpreter". It takes in 
	# predictions from Predictors and integrates them together
	# using Bayes Theorem. This class is very basic. It does 
	# not assume any priors, but must be given them.
	#
	# No subjective assumptions should appear here! We want
	# to be able to adjust them, so they must be passed as an
	# object or otherwise. 
	# 
	# This needs to be built in such a way so that it does not
	# have to recalculate everything over again. Speed is somewhat
	# important, especially if at some future point we become 
	# interested in calculating this sort of thing on an hourly
	# or smaller instead of a daily basis.
	
	def getPredictions():
		# fake ones for now
		return [True,True,False]
	
	def getConfidences():
		# sooo fake
		return [.5,.6,.7]

	def makePrediction():
		# TODO update on confidences
		finalPrediction = .5
		
		predictions = getPredictions()
		confidences = getConfidences()
		
		# TODO finish loop and bayes bit
		
		return finalPrediction

if __name__ == "__main__": Interpreter.makePrediction()
