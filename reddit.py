"""
A simple scraper for reddit

Created by Jake Rockland

"""

from __future__ import division
from datetime import datetime, timedelta
from pprint import pprint
import math
import praw

r = praw.Reddit('Hot post counter 1.0 by u/benjamin-spanklin.'
                'A simple Python scraper to count post velocity.')

r.login('benjamin-spanklin','yhBAfBH38L7e')

all_subreddit = r.get_subreddit('all')

hot_posts = all_subreddit.get_new(limit=10) # change limit to +1000?

for post in hot_posts:
    timestamp = post.created_utc
    pprint(timestamp)

def totimestamp(dt, epoch=datetime(1970,1,1)):
    td = dt - epoch
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6

now = float(math.trunc(totimestamp(datetime.utcnow())))
