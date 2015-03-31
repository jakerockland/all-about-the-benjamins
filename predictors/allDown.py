# This predictor always predicts values will fall.

from predictor import Predictor

class AllDown(Predictor):
	def decisionGoUp():
		return False
