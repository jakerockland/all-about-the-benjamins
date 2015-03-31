import json
class Updater:
	
	def Updater(self):
		pass
	
	def dumpToDataBase(predictions):
		with open('interpreter/predictions','w') as f:
			json.dump(predictions,f)
	
	def getPredictors(self):
		predictors = []
		with open('predictors/list_of_predictors') as f:
			for line in f:
				predictors.append(line)
		return predictors

	def getPredictions(self):
		predictors = getPredictors(self)
		
		return predictions

	def update(self):
		predictions = self.getPredictions()
		self.dumpToDataBase(predictions)

if __name__ == "__main__":
	u = Updater()
	u.update()
