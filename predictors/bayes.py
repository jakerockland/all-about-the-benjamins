class Bayes (object):
    def apply_bayes(self,prior,pDy,pDn):
        if pDn == pDy or pDn == 0 or pDy == 0:
            return prior
        return pDy/pDn * prior
