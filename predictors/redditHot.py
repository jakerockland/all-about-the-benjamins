# This predictor predicts values will increase if it reddit's hot board is volatile

from redditPredictor import RedditPredictor

class RedditHot(RedditPredictor):
    def __init__(self):
        self.sub = "all"
        self.type = "hot"
        self.threshold = "0.1"

if __name__ == "__main__":
    print(RedditHot().goesUp())
