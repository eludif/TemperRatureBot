import time
import tweepy
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def tweet_temp(tweet_lines):

    print(tweet_lines[0])
    last_tweet = api.update_status(tweet_lines[0])

    # create a loop to iterate over lines
    for tweet_line in tweet_lines[1:]:
        try:
            print(tweet_line)
            last_tweet = api.update_status(tweet_line, last_tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)
        time.sleep(5)
