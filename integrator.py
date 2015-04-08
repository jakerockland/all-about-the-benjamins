from yahoo_finance import Share
from datetime import datetime, timedelta
import json

class Integrator(object):
    def __init__(self):
        self.yesterday = datetime.strftime(datetime.utcnow()-timedelta(1), '%Y-%m-%d')
		with open('predictors.json','r') as f:
            self.predictors = json.load(f)

	def aggregate_predictions(self,predictions,threshold=0.5):
		yes_count = no_count = 0
		for prediction in predictions:
			if prediction[0].split()[0] == self.yesterday:
				if prediction[1]:
					yes_count += 1
				else:
					no_count += 1
		return True if (yes_count / (yes_count + no_count)) > threshold else False

    def performance_up(self,symbol='^GSPC'):
        share = Share(symbol)
        data = share.get_historical(self.yesterday,self.yesterday)[0]
        delta = float(data.get('Close')) - float(data.get('Open'))
        return True if delta > 0 else False

	def integrate_predictions:
		file = 'interpreter/predictions.json'
		with open(file,'r') as f:
            log = json.load(f)

		for predictor in self.predictors:
			with open('predictions/' + predictor + '.json','r') as f:
                predictions = json.load(f)
			prediction = aggregate_predictions(predictions)
			performance = performance_up()

			predictor_log = log.get(predictor)
			if predictor_log != None:
				pass # FIXME


        with open(file,'w') as f:
            json.dump(log,f)

	# def getPredictions(self):
    #     enhanced_predictions = []
    #     predictors = getPredictors()
    #     performance = getPerformance()
    #     predictor_data = {}
    #
    #     for predictor in predictors:
    #         predictor_data = getPredictorData(predictor)
    #         # Compare data with performance, calculate y|y, y|n
    #         numyy = 0 # y|y
    #         numxy = 0 # |y
    #         numyn = 0 # y|n
    #         numxn = 0 # |n
    #         for day in performance:
    #             # Check if key is in dict
    #             if day in predictor_data:
    #                 # check if conditioning on down or up
    #                 if performance[day]==0:
    #                     numxn+=1
    #                     if predictor_data[day]==1:
    #                         numyn+=1
    #                 if performance[day]==1:
    #                     numxy+=1
    #                     if predictor_data[day]==1:
    #                         numyy+=1
    #         # Divide totals to get percentages
    #         yy = numyy/(float(numxy))
    #         yn = numyn/(float(numxn))
    #
    #         # dump prediction and related to 4-tuple in list
    #         enhanced_predictions.append((predictor,predictors[predictor],yy,yn))
    #
    #     return enhanced_predictions
	#
    # def integratePredictions(self):
    #     predictions = self.getPredictions()
    #     dumpPredictions(predictions)

if __name__ == "__main__":
    Integrator().performace_up()
