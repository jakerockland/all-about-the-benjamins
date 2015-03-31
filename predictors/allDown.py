# This predictor always predicts values will rise.

from predictor import *

class AllDown(Predictor):
	def decisionGoUp():
		return False
