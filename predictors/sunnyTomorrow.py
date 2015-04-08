# This predictor predicts values will increase if it is forecasted to be sunny tomorrow

from forecastPredictor import ForecastPredictor
import pyowm

class SunnyTomorrow(ForecastPredictor):
    def goesUp(self):
        tomorrow = pyowm.timeutils.tomorrow()
        return True if self.forecast.will_be_sunny_at(tomorrow) else False

if __name__ == "__main__":
    print(SunnyTomorrow().goesUp())
