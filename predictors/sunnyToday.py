# This predictor predicts values will increase if it is forecast to be sunny in the next hour

from forecastPredictor import ForecastPredictor
import pyowm

class SunnyToday(ForecastPredictor):
    def goesUp(self):
        next_hour = pyowm.timeutils.next_hour()
        return True if self.forecast.will_be_sunny_at(next_hour) else False

if __name__ == "__main__":
    print(SunnyToday().goesUp())
