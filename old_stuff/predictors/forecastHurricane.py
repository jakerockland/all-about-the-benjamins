# This predictor predicts values will decrease if it is forecast to hurricane

from forecastPredictor import ForecastPredictor

class ForecastHurricane(ForecastPredictor):
    def goes_up(self):
        return True if not self.forecast.will_have_hurricane() else False

if __name__ == "__main__":
    print(ForecastHurricane().goes_up())
