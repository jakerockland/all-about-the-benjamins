# This predictor predicts values will decrease if it is forecast to storm

from forecastPredictor import ForecastPredictor

class ForecastStorm(ForecastPredictor):
    def goesUp(self):
        return True if not self.forecast.will_have_storm() else False

if __name__ == "__main__":
    print(ForecastStorm().goesUp())
