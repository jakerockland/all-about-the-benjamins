# from __future__ import division
# from datetime import datetime, timedelta
# import math
import json
import predictors

class Updater(object):
    def __init__(self):
        with open('predictors.json','r') as f:
            self.predictors = json.load(f)

    # def totimestamp(dt, epoch=datetime(1970,1,1)):
	#     td = dt - epoch
	#     return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6

    def updatePredictor(self,instance):
        prediction = {}
        # now = float(math.trunc(self.totimestamp(datetime.utcnow())))
        prediction['recent'] = []
        prediction['log'] = [None,0,0]

        with open('data/' + instance.getName() + '.json','r') as f:
            pass # TODO
        with open('data/' + instance.getName() + '.json','w') as f:
            json.dump(prediction,f)

    def updateAll(self):
        for predictor in self.predictors:
            if predictor == "ForecastHurricane":
                instance = predictors.ForecastHurricane()
            elif predictor == "ForecastStorm":
                instance = predictors.ForecastStorm()
            elif predictor == "ForecastTornado":
                instance = predictors.ForecastTornado()
            elif predictor == "RedditControversial":
                instance = predictors.RedditControversial()
            elif predictor == "RedditHot":
                instance = predictors.RedditHot()
            elif predictor == "RedditNew":
                instance = predictors.RedditNew()
            elif predictor == "RedditRising":
                instance = predictors.RedditRising()
            elif predictor == "RedditTop":
                instance = predictors.RedditTop()
            elif predictor == "SunnyToday":
                instance = predictors.SunnyToday()
            elif predictor == "SunnyTomorrow":
                instance = predictors.SunnyTomorrow()

            self.updatePredictor(instance)

if __name__ == "__main__":
    Updater().updateAll()
