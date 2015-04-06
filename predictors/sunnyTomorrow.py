# This predictor predicts values will if it is forecasted to be sunny tomorrow.

from predictor import Predictor
import pyowm

class SunnyTomorrow(Predictor):
    api_id = "be12f64238d2cb8b7c50b13e2faf7537"
    owm = pyowm.OWM(api_id)

    def __init__(self,city="New York",country="US"):
        self.city = city
        self.country = country

    def decisionGoesUp(self):
        forecast = owm.daily_forecast(city + "," + country)
        tomorrow = pyowm.timeutils.tomorrow()
        return True if forecast.will_be_sunny_at(tomorrow) else False
