# This predictor predicts values will increase if it is forecast to be sunny in the next hour

from predictor import Predictor
import pyowm

class SunnyToday(Predictor):
    api_id = "be12f64238d2cb8b7c50b13e2faf7537"
    owm = pyowm.OWM(api_id)

    def __init__(self,city="New York",country="US"):
        self.city = city
        self.country = country

    def decisionGoesUp(self):
        forecast = self.owm.daily_forecast(self.city + "," + self.country)
        next_hour = pyowm.timeutils.next_hour()
        return True if forecast.will_be_sunny_at(next_hour) else False

if __name__ == "__main__":
    print(SunnyToday().decisionGoesUp())
