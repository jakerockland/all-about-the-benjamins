import json
import predictors

class Updater(object):
	def getPredictors(self):
		with open('predictors.json','r') as f:
			return json.load(f)

	def getResults(self,predictor):
		predictionStatsUpdate = None # TODO
		return predictionStatsUpdate

	def updatePredictionStats(self):
		predictors = getPredictors()

		for predictor in predictors:
			predictionStatsUpdate = getResults(predictor)
			# TODO

if __name__ == "__main__":
	print(Updater().getPredictors())
