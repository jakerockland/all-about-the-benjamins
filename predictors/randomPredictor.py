# This predictor is completely random.

from predictor import Predictor
import random

class RandomPredictor(Predictor):
	def __init__(self):
		self.threshold = 0.5
	
	def goesUp(self):
		return random.random() > self.threshold

if __name__ == "__main__":
	print(RandomPredictor().goesUp())
