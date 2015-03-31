# This predictor always predicts values will rise.

from predictor import *

class UpAll(Predictor):
	def decisionGoUp():
		return False
