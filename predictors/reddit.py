"""
A simple post volatility calculator for reddit

Created by Jake Rockland

"""

from __future__ import division
from datetime import datetime, timedelta
from pprint import pprint
import math
import numpy
import praw

def totimestamp(dt, epoch=datetime(1970,1,1)):
    td = dt - epoch
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6

def postDeltas(sub="all", type="new", num=100):
    r = praw.Reddit('Post volatility calculator 1.0 by u/benjamin-spanklin.'
                    'A simple Python scraper to calculate post volatility.')

    r.login('benjamin-spanklin','yhBAfBH38L7e')

    subreddit = r.get_subreddit(sub)

    if (type == "hot"):
        posts = subreddit.get_hot(limit=num)
    elif (type == "controversial"):
        posts = subreddit.get_controversial(limit=num)
    elif (type == "rising"):
        posts = subreddit.get_rising(limit=num)
    elif (type == "top"):
        posts = subreddit.get_top(limit=num)
    elif (type == "unmoderated"):
        posts = subreddit.get_unmoderated(limit=num)
    else:
        posts = subreddit.get_new(limit=num)

    now = float(math.trunc(totimestamp(datetime.utcnow())))

    deltas = []

    for post in posts:
        deltas.append(abs(now - post.created_utc))

    return deltas

def main():
    hot_deltas = numpy.array(postDeltas("all", "hot", 1000))
    controversial_deltas = numpy.array(postDeltas("all", "controversial", 1000))
    rising_deltas = numpy.array(postDeltas("all", "rising", 1000))

    print("Hot:\t" + str(numpy.mean(hot_deltas)) + "\t" + str(numpy.var(hot_deltas)))
    print("Controversial:\t" + str(numpy.mean(controversial_deltas)) + "\t" + str(numpy.var(controversial_deltas)))
    print("Rising:\t" + str(numpy.mean(rising_deltas)) + "\t" + str(numpy.var(rising_deltas)))

if __name__ == "__main__": main()
