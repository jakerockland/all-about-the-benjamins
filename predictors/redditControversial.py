# This predictor predicts values will increase if it reddit's controversial board is volatile

from redditPredictor import RedditPredictor

class RedditControversial(RedditPredictor):
    def __init__(self):
        self.sub = "all"
        self.type = "controversial"
        self.threshold = "0.1"

if __name__ == "__main__":
    print(RedditControversial().goes_up())
