import json
class Updater:
	
	def Updater(self):
		pass
	
	def dumpToDataBase(predictions):
		with open('predictions','w') as f:
			json.dump(predictions,f)

	def getPredictions(self):
		return predictions

	def update(self):
		predictions = self.getPredictions()
		
		self.dumpToDataBase(predictions)


if __name__ == "__main__":
	u = Updater()
	u.update()
