# This predictor predicts values will decrease if it is forecast to tornado

from predictor import Predictor
import pyowm

class TornadoForecast(Predictor):
    api_id = "be12f64238d2cb8b7c50b13e2faf7537"
    owm = pyowm.OWM(api_id)

    def __init__(self,city="New York",country="US"):
        self.city = city
        self.country = country

    def decisionGoesUp(self):
        forecast = owm.daily_forecast(city + "," + country)
        return True if !forecast.will_have_tornado() else False
