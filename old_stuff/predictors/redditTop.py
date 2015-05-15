# This predictor predicts values will increase if it reddit's top board is volatile

from redditPredictor import RedditPredictor

class RedditTop(RedditPredictor):
    def __init__(self):
        self.sub = "all"
        self.type = "top"
        self.threshold = "0.1"

if __name__ == "__main__":
    print(RedditTop().goes_up())
