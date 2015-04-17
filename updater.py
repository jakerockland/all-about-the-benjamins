import datetime
import json
import predictors
import os.path


class Updater(object):
    def __init__(self):
        with open('predictors.json','r') as f:
            self.predictors = json.load(f)

    def updatePredictor(self,instance):
        file = 'data/' + instance.getName() + '.json'
        rise = instance.goesUp()
        now = datetime.datetime.strftime(datetime.datetime.utcnow(), '%Y-%m-%d %H:%M:%S')

        # Creates data file for predictor if it does not yet exist
        if not os.path.isfile(file):
            weight = 1 if rise else 0
            prediction = {}
            prediction['recent'] = [[now,rise]]
            prediction['log'] = [now,0,0]
            prediction['predictor'] = instance.getName()

        # Otherwise, updates the data file for the respective predictor
        else:
            with open(file,'r') as f:
                prediction = json.load(f)
            prediction.get('recent').append([now,rise])

        # Writes updated data back to file
        with open(file,'w') as f:
                json.dump(prediction,f)

    def updateAll(self):
        # Goes through each predictor and updates it's respective data file
        # This needs to be continually kept up to date with predictors.json
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
	    elif predictor == "RandomPredictor":
		instance = predictors.RandomPredictor()

            self.updatePredictor(instance)

if __name__ == "__main__":
    Updater().updateAll()
