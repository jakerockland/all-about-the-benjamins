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
	
	def getPredictors(self):
		return [] #TODO

	def getPredictions(self):
		predictions = []
		predictors = self.getPredictors()

		for predictor in predictors:
			pass	

		# fake ones for now
		# It goes (prediction, % predict yes when yes, % predict yes when no)
		return [(1,.3,.3),(1,.5,.2),(0,.8,.2)]
	
	def applyBayes(self,prior,pDH,pD):
		return pDH*prior/pD

	def makePrediction(self):
		# TODO update on confidences
		finalPrediction = .5
		
		predictions = self.getPredictions()
		
		for prediction in predictions:
			prior = finalPrediction
			pBA = prediction[1]
			pBnA = prediction[2]
			pnA = 1-finalPrediction
			
			pD = prior*pBA + pnA*pBnA

			finalPrediction = self.applyBayes(prior,pBA,pD)
			print finalPrediction

		return finalPrediction

if __name__ == "__main__": 
	a = Interpreter()
	print a.makePrediction()
