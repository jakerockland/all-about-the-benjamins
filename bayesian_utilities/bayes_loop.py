from bayes_calc import BayesCalc
from data_utilities import Dumper

class BayesLoop(object):
    def make_prediction(self):
        # Grabs predictors using dumper
        # Loops through all and outputs final prediction
        predictors = Dumper.get_predictors()
        prior = 1
        for predictor in predictors:
            prior = BayesCalc.apply_bayes(prior, predictor[prediction], predictor[pyy], predictor[pyn])
        return prior
