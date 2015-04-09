from yahoo_finance import Share
from datetime import datetime, timedelta
import json

class Integrator(object):
    def __init__(self):
        self.today = datetime.strftime(datetime.utcnow(), '%Y-%m-%d')
        self.yesterday = datetime.strftime(datetime.utcnow()-timedelta(1), '%Y-%m-%d')
        with open('predictors.json','r') as f:
            self.predictors = json.load(f)

    def aggregate_predictions(self,predictions,threshold=0.5):
        yes_count = no_count = 0
        for prediction in list(predictions):
            if prediction[0].split()[0] == self.today:
                if prediction[1]:
                    yes_count += 1
                else:
                    no_count += 1
                predictions.remove(prediction)
        return True if (yes_count / (yes_count + no_count)) > threshold else False

    def has_he_risen(self,symbol='^GSPC'):
        share = Share(symbol)
        data = share.get_historical(self.yesterday,self.yesterday)[0]
        delta = float(data.get('Close')) - float(data.get('Open'))
        return True if delta > 0 else False

    def integrate_predictions(self,predictor,log):
        file = 'predictions/' + predictor + '.json'
        with open(file,'r') as f:
            predictions = json.load(f)

        todays_prediction = self.aggregate_predictions(predictions)
        yesterday_rise = self.has_he_risen()

        predictor_log = log.get(predictor)
        if predictor_log is None:
            log[predictor] = [todays_prediction, 0, 0, 0, 0]
        else:
            yesterdays_prediction = predictor_log[0]
            prob_yy = predictor_log[1] # weight, predict_up|rise
            num_y = predictor_log[2] # count, rise
            prob_yn = predictor_log[3] # weight,predict_up|rise
            num_n = predictor_log[4] # count, fall
            if yesterday_rise:
                if (num_y == 0):
                    prob_yy = int(todays_prediction)
                else:
                    prob_yy = (num_y * prob_yy + int(todays_prediction)) / (num_y + 1)
                num_y += 1
            else:
                if (num_n == 0):
                    prob_yn = int(todays_prediction)
                else:
                    prob_yn = (num_n * prob_yn + int(todays_prediction)) / (num_n + 1)
                num_n += 1
            log[predictor] = [todays_prediction,prob_yy,num_y,prob_yn,num_n]

        with open(file,'w') as f:
            json.dump(predictions,f)

    def integrate_all(self):
        file = 'log.json'
        with open(file,'r') as f:
            log = json.load(f)

        for predictor in self.predictors:
            self.integrate_predictions(predictor,log)

        with open(file,'w') as f:
            json.dump(log,f)

if __name__ == "__main__":
    Integrator().integrate_all()
