import json
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
	
	def Interpreter(self):
		pass

	def getPredictions(self):
		# The file confidences contains a list
		# entries are of the form
		# (name, prediction, y|y, y|n)
		with open('confidences', 'r') as f:
			return json.load(f)

	def applyBayes(self,prior,pDy,pDn):
		# Does a Bayesian model comparison
		# between the hypothesis "goes up" and the
		# hypothesis "somethig else"
		# Returns postY/postN  = pDy/pDn * priorY/priorN
		# Note that priorY/priorN = prior
		if pDn == 0:
			return 100000000
		return pDy/pDn * prior

	def makePrediction(self,predictions, prior):
		# Returns the confidence it has in the stock going
		# up tomorrow.
		#
		# Applies Bayes' Thm to predictions and a
		# non-informational prior in order to perform a model
		# comparison. 
		#
		# Will return a rational value which represents the
		# number of times more probable it is that the stock
		# will go up.
		posterior = prior
		
		for prediction in predictions:
			# assign sensible names to imported values
			prior = posterior
			pDy = abs(prediction[1]-prediction[2]-1)
			pDn = abs(prediction[1]-prediction[3]-1)

			# Do the actual calculation
			posterior = self.applyBayes(prior,pDy,pDn)
		
		return posterior
	
	def main(self):
		predictions = self.getPredictions()
		return self.makePrediction(predictions,1)

if __name__ == "__main__": 
	a = Interpreter()
	print a.main()
