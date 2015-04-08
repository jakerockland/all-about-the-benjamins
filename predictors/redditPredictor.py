# This predictor predicts values will increase if it reddit's controversial board is volatile

from predictor import Predictor
from reddit import deltas
import math
import numpy

class RedditPredictor(Predictor):
    def __init__(self):
        self.sub = "all"
        self.type = "new"
        self.threshold = "0.1"

    def getDeltas(self):
        return numpy.array(deltas(self.sub, self.type, 1000))

    def goesUp(self):
        deltas = self.getDeltas()
        coeff = math.sqrt(numpy.var(deltas)) / numpy.mean(deltas)
        return True if coeff < self.threshold else False

if __name__ == "__main__":
    print(RedditPredictor().goesUp())
