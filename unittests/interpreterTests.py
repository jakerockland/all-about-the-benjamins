#!/usr/bin/python

import unittest

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

	def testCheckBayes(self):
		a = Interpreter()
		self.failUnless(a.applyBayes(0.5,0.5,0.5)==0.5)
		self.failUnless(a.applyBayes(0,1,1)==0)
		self.failUnless(a.applyBayes(.9,.1,0.5)==4.5)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
		
