import json
class PredictionUpdater:
	
	def PredictionUpdater(self):
		pass
	
	def dumpToDataBase(self,predictions):
		with open('interpreter/predictions','w') as f:
			json.dump(predictions,f)
	
	def getPredictors(self):
		predictors = []
		with open('predictors/list_of_predictors','r') as f:
			for line in f:
				predictors.append(line.rstrip())
		return predictors

	def getPredictions(self):
		predictions = []
		predictors = self.getPredictors()
		
		for predictor in predictors:
			with open('predictors/'+predictor+'_stats','r') as f:
				i = 0
				prediction = []
				for line in f:
					# line 0 is the prediction (0 or 1), line 1 is the prob y|y, line 2 is prob y|n
					prediction.append(line.rstrip())
			predictions.append(prediction)
		return predictions

	def updatePredictions(self):
		predictions = self.getPredictions()
		self.dumpToDataBase(predictions)

if __name__ == "__main__":
	p = PredictionUpdater()
	p.updatePredictions()