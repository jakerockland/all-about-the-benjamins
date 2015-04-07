# This predictor predicts values will increase if it is forecasted to be sunny tomorrow

from predictor import Predictor
import pyowm

class SunnyTomorrow(Predictor):
    api_id = "be12f64238d2cb8b7c50b13e2faf7537"
    owm = pyowm.OWM(api_id)

    def __init__(self,city="New York",country="US"):
        self.city = city
        self.country = country

    def goesUp(self):
        forecast = self.owm.daily_forecast(self.city + "," + self.country)
        tomorrow = pyowm.timeutils.tomorrow()
        return True if forecast.will_be_sunny_at(tomorrow) else False

if __name__ == "__main__":
    print(SunnyTomorrow().goesUp())
