# This predictor is completely random.

import random

class RandomPredictor(Predictor):
	threshold = 0.5
	def goesUp(self):
		return random.random() > threshold

if __name__ == "__main__":
	print(RandomPredictor().goesUp())
