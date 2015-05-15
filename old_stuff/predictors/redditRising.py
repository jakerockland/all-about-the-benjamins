# This predictor predicts values will increase if it reddit's rising board is volatile

from redditPredictor import RedditPredictor

class RedditRising(RedditPredictor):
    def __init__(self):
        self.sub = "all"
        self.type = "rising"
        self.threshold = "0.1"

if __name__ == "__main__":
    print(RedditRising().goes_up())
