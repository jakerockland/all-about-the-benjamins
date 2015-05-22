#!/usr/bin/python

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from bayesian_utilities import *
    else:
        from ..bayesian_utilities import *
    test = True;
import unittest

# unittests for Interpreter
class BayesUtilsTests (unittest.TestCase):
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
