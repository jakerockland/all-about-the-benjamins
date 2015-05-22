#!/usr/bin/python

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from interpreter.interpreter import Interpreter
    else:
        from ..interpreter.interpreter import Interpreter
    test = True;
import unittest

# unittests for Interpreter
class InterpreterTests (unittest.TestCase):
    def set_up(self):
        # Setting up for the test
        print "InterpreterTests:set_up_:begin"
        ## We'll use this when doing more databasey stuff
        print "InterpreterTests:set_up_:end"

    def tear_down(self):
        # Cleaning up after the test
        print "InterpreterTests:tear_down_:begin"
        ## We'll use this once we actually have databases
        print "InterpreterTests:tear_down_:end"

    def test_bayes(self):
        # Test if the Bayes method does what it should
        a = Interpreter()
        # apply_bayes(prior,pDy,pDn)
        self.failUnless(a.apply_bayes(0.5,0.5,0.5)==0.5)
        self.failUnless(a.apply_bayes(1,0,1)==0)
        self.failUnless(a.apply_bayes(0.5,.9,.1)==4.5)
        self.failUnless(a.apply_bayes(1,1,0)>100000)
        self.failUnless(a.apply_bayes(0,1,1)==0)
        self.failUnless(a.apply_bayes(1,0.3,0.6)==0.5)
        print "InterpreterTests:test_bayes"

    def test_make_prediction(self):
        # Test if predictions come out right
        a = Interpreter()
        # name, prediction, y|y, y|n
        predictions = [["testP1",1,0.3,0.6]]
        prior = 1
        epsilon = 10**(-15)
        p = a.make_prediction(predictions,prior)
        self.failUnless(abs(p - 0.5)<epsilon)
        print "InterpreterTests:test_predictions"

    def test_get_predictions(self):
        # Test if get_predictions loads files in right; uses testfile in unittests
        a = Interpreter()
        fileName = "testConfidences"
        p = a.get_predictions(fileName)
        self.failUnless(p == [[1,2,3,4],[2,3,4,5]])

    def test_run(self):
        # Test if runs without errors
        a = Interpreter()
        a.run()
        print "InterpreterTests:test_run"

if __name__ == '__main__':
    unittest.main()
