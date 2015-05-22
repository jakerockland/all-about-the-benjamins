import bayes_calc
import dumper
def make_prediction:
    # Grabs predictors using dumper
    # Loops through all and outputs final prediction
    predictors = dumper.get_predictors()
    prior = 1
    for predictor in predictors:
        prior = bayes_calc.apply_bayes(prior, predictor[prediction], predictor[pyy], predictor[pyn])
    return prior
