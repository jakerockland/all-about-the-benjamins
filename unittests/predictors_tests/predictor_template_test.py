#!/usr/bin/python

# This currently has some serious import issues and needs to be fixed.


if __name__ == '__main__':
#    if __package__ is None:
#        import sys
#        from os import path
#        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
#        from ..predictors import TEMPLATE_PREDICTOR
#    else:
        from ...predictors import TEMPLATE_PREDICTOR
        test = True;
import unittest

# unittests for Interpreter
class TEMPLATEPredictorTests (unittest.TestCase):
    def set_up(self):
        # Setting up for the test
        pass
        # We'll use this when doing more databasey stuff

    def tear_down(self):
        pass
        # Cleaning up after the test
        pass
        # We'll use this once we actually have databases

if __name__ == '__main__':
    unittest.main()
