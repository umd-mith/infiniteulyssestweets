#!/usr/bin/env python

"""
Tweet when something is annotated at http://www.infiniteulysses.com/.
"""

import re
import bs4
import tweepy
import feedparser

# you'll need to get these by creating an app at apps.twitter.com 

consumer_secret = ""
consumer_key = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twtr = tweepy.API(auth)

feed = feedparser.parse('http://www.infiniteulysses.com/annotations.xml')
for entry in feed['entries']:
    author = entry['author']
    link = entry['link']
    desc = bs4.BeautifulSoup(entry['description'])
    target = re.split(':.', desc.select('.field-quote')[0].text, 1)[1]
    msg = '"%s" annotated by %s - %s' % (target, author, link)
    if len(msg) < 140:
        # tweepy silently ignores errors due to duplicate tweets and messages 
        # that are too long ... which is nice
        twtr.update_status(msg)
