# This predictor always predicts values will rise

from predictor import Predictor

class AllUp(Predictor):
	def decisionGoUp(self):
		return True
