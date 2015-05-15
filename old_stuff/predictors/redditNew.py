# This predictor predicts values will increase if it reddit's new board is volatile

from redditPredictor import RedditPredictor

class RedditNew(RedditPredictor):
    def __init__(self):
        self.sub = "all"
        self.type = "new"
        self.threshold = "0.1"

if __name__ == "__main__":
    print(RedditNew().goes_up())
