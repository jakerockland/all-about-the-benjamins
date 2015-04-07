class Updater(object):
	def getPredictors(self):
		predictors = []

		with open('list_of_predictors','r') as f:
			for line in f:
				predictors.append(line.rstrip())

		return predictors

	def getResults(self,predictor):
		predictionStatsUpdate = None # TODO
		return predictionStatsUpdate

	def updatePredictionStats(self):
		predictors = getPredictors()

		for predictor in predictors:
			predictionStatsUpdate = getResults(predictor)
			# TODO

if __name__ == "__main__":
	Updater().updatePredictionStats()
