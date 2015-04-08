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
	def setUp(self):
		# Setting up for the test
		print "InterpreterTests:setUp_:begin"
		## We'll use this when doing more databasey stuff
		print "InterpreterTests:setUp_:end"

	def tearDown(self):
		# Cleaning up after the test
		print "InterpreterTests:tearDown_:begin"
		## We'll use this once we actually have databases
		print "InterpreterTests:tearDown_:end"

	def testBayes(self):
		# Test if the Bayes method does what it should
		a = Interpreter()
		# applyBayes(prior,pDy,pDn)
		self.failUnless(a.applyBayes(0.5,0.5,0.5)==0.5)
		self.failUnless(a.applyBayes(1,0,1)==0)
		self.failUnless(a.applyBayes(0.5,.9,.1)==4.5)
		self.failUnless(a.applyBayes(1,1,0)>100000)
		self.failUnless(a.applyBayes(0,1,1)==0)
		self.failUnless(a.applyBayes(1,0.3,0.6)==0.5)
		print "InterpreterTests:testBayes"

	def testMakePrediction(self):
		# Test if predictions come out right
		a = Interpreter()
		# name, prediction, y|y, y|n
		predictions = [["testP1",1,0.3,0.6]]
		prior = 1
		epsilon = 10**(-15)
		p = a.makePrediction(predictions,prior)
		self.failUnless(abs(p - 0.5)<epsilon)
		print "InterpreterTests:testPredictions"

	def testGetPredictions(self):
		# Test if getPredictions loads files in right; uses testfile in unittests
		a = Interpreter()
		fileName = "testConfidences"
		p = a.getPredictions(fileName)
		self.failUnless(p == [[1,2,3,4],[2,3,4,5]])

	def testRun(self):
		# Test if runs without errors
		a = Interpreter()
		a.run()
		print "InterpreterTests:testRun"

if __name__ == '__main__':
	unittest.main()
