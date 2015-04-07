# This predictor predicts values will decrease if it is forecast to tornado

from forecastPredictor import ForecastPredictor

class ForecastTornado(ForecastPredictor):
    def goesUp(self):
        return True if not self.forecast.will_have_tornado() else False

if __name__ == "__main__":
    print(ForecastTornado().goesUp())
