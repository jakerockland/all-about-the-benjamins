# This predictor predicts values will decrease if it is forecast to tornado

from predictor import Predictor
import pyowm

class ForecastPredictor(Predictor):
    api_id = "be12f64238d2cb8b7c50b13e2faf7537"
    owm = pyowm.OWM(api_id)

    def __init__(self):
        self.forecast = self.owm.daily_forecast('New York,US')

if __name__ == "__main__":
    print(ForecastPredictor().goesUp())
