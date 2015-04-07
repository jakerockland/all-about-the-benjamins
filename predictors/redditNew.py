# This predictor predicts values will increase if it reddit's new board is volatile

from predictor import Predictor
from reddit import deltas
import math
import numpy

class RedditNew(Predictor):
    coeff_threshold = 0.1

    def __init__(self,sub="all"):
        self.sub = sub

    def getDeltas(self):
        return numpy.array(deltas(self.sub, "new", 1000))

    def goesUp(self):
        deltas = self.getDeltas()
        coeff = math.sqrt(numpy.var(deltas)) / numpy.mean(deltas)
        return True if coeff < self.coeff_threshold else False

if __name__ == "__main__":
    print(RedditNew().goesUp())
