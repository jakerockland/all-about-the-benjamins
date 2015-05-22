def apply_bayes(prior,prediction,pyy,pyn):
    # Takes in above, spits out posterior according to bayes thm
    pDy = 1-prediction-pyy
    pDn = 1-prediction-pyn
    if pDn == pDy or pDn == 0 or pDy == 0:
        return prior
    return pDy/pDn * prior
