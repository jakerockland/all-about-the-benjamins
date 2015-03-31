class PredictionStatsUpdater(object):

	def PredictionStatsUpdater(self):
		pass

	def getPredictors(self):
		predictors = []

		with open('list_of_predictors','r') as f:
			for line in f:
				predictors.append(line.rstrip())

	def updatePredictionStats(self):
		predictors = getPredictors(self)
		



if __name__ == "__main__":
	p = PredictionStatsUpdater()
	p.updatePredictionStats()
