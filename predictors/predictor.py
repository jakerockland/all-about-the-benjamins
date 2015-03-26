class Predictor (object):
	# This class is the superclass for all predictors.
	# It implements some basic functionality that all
	# predictors should have (and, presumably, extend).
	# 
	# Predictors are instantiated and run by the
	# interpreter, but a predictor that requires
	# extra processing power, etc, could have an
	# external agents that runs separately and
	# dumps its conclusions to a file,
	# and then have a subclass of Predictor
	# that exists just to read in this data
	# when Interpreter asks for it. In fact,
	# this may be the best model in the long
	# run, though the subclassing functionality
	# should be kept for quick prototyping.

	pass
