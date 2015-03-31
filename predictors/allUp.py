# This predictor always predicts values will rise.

from predictor import *

class AllUp(Predictor):
	def decisionGoUp():
		return True
