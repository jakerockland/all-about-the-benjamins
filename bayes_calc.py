def apply_bayes(prior,prediction,pyy,pyn):
    pDy = 1-prediction-pyy
    pDn = 1-prediction-pyn
    if pDn == pDy or pDn == 0 or pDy == 0:
        return prior
    return pDy/pDn * prior
