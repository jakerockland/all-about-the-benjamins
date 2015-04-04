#!/usr/bin/python

import unittest
from interpreter import Interpreter

class InterpreterTests (unittest.TestCase):
	# unittests for Interpreter

	def setUp(self):
		""" Setting up for the test """
		print "InterpreterTests:setUp_:begin"
		## We'll use this when doing more databasey stuff
		print "InterpreterTests:setUp_:end"

	def tearDown(self):
		""" Cleaning up after the test"""
		print "InterpreterTests:tearDown_:begin"
		## We'll use this once we actually have databases
		print "InterpreterTests:tearDown_:end"

	def testBayes(self):
		a = Interpreter()
		# applyBayes(prior,pDy,pDn)
		self.failUnless(a.applyBayes(0.5,0.5,0.5)==0.5)
		self.failUnless(a.applyBayes(1,0,1)==0)
		self.failUnless(a.applyBayes(0.5,.9,.1)==4.5)
		self.failUnless(a.applyBayes(1,1,0)>100000)
		self.failUnless(a.applyBayes(0,1,1)==0)
		self.failUnless(a.applyBayes(1,0.3,0.6)==0.5)

	def testPredictions(self):
		a = Interpreter()
		# name, prediction, y|y, y|n
		predictions = [["testP1",1,0.3,0.6]]
		prior = 1
		epsilon = 10**(-15)
		p = a.makePrediction(predictions,prior)
		self.failUnless(abs(p - 0.5)<epsilon)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
		
