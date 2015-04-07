# This predictor predicts values will decrease if it is forecast to hurricane

from predictor import Predictor
import pyowm

class ForecastHurricane(Predictor):
    api_id = "be12f64238d2cb8b7c50b13e2faf7537"
    owm = pyowm.OWM(api_id)

    def __init__(self,city="New York",country="US"):
        self.city = city
        self.country = country

    def decisionGoesUp(self):
        forecast = self.owm.daily_forecast(self.city + "," + self.country)
        return True if not forecast.will_have_hurricane() else False

if __name__ == "__main__":
    print(ForecastHurricane().decisionGoesUp())
