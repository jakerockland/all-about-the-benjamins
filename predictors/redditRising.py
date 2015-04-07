# This predictor predicts values will increase if it reddit's rising board is volatile

from predictor import Predictor
from reddit import deltas
import math
import numpy

class RedditRising(Predictor):
    coeff_threshold = 0.1

    def __init__(self,sub="all"):
        self.deltas = numpy.array(deltas(sub, "rising", 1000))

    def decisionGoesUp(self):
        coeff = math.sqrt(numpy.var(self.deltas)) / numpy.mean(self.deltas)
        return True if coeff < self.coeff_threshold else False

if __name__ == "__main__":
    print(RedditRising().decisionGoesUp())
