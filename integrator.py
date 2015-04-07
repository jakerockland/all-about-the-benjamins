import json
import datetime

class Integrator:
	def dumpPredictions(self,predictions):
		with open('interpreter/predictions.json','w') as f:
			json.dump(predictions,f)

	def loadPredictors(self):
		# Load a dict of predictor:prediction
		predictors = {}
		with open('data/predictors.json','r') as f:
			predictors = json.load(f)
		return predictors

	def getPerformance(self):
		# Returns a list of actual performance of the stock,
		# as a dictionary of dates to up (1) or down (0) values
		#TODO
		# Dummy values given right now.
		return {datetime.date(2015,1,1):0,datetime.date(2015,1,2):0}

	def getPredictorData(self,predictor):
			with open('data/'+predictor+'.json','r') as f:
				# Grab the date to up/down dictionary from the file
				return json.load(f)

	def getPredictions(self):
		enhanced_predictions = []
		predictors = loadPredictors()
		performance = getPerformance()
		predictor_data = {}

		for predictor in predictors:
			predictor_data = getPredictorData(predictor)
			# Compare data with performance, calculate y|y, y|n
			numyy = 0 # y|y
			numxy = 0 # |y
			numyn = 0 # y|n
			numxn = 0 # |n
			for day in performance:
				# Check if key is in dict
				if day in predictor_data:
					# check if conditioning on down or up
					if performance[day]==0:
						numxn+=1
						if predictor_data[day]==1:
							numyn+=1
					if performance[day]==1:
						numxy+=1
						if predictor_data[day]==1:
							numyy+=1
			# Divide totals to get percentages
			yy = numyy/(float(numxy))
			yn = numyn/(float(numxn))

			# dump prediction and related to 4-tuple in list
			enhanced_predictions.append((predictor,predictors[predictor],yy,yn))

		return enhanced_predictions

	def integratePredictions(self):
		predictions = self.getPredictions()
		dumpPredictions(predictions)

if __name__ == "__main__":
	Integrator().integratePredictions()
