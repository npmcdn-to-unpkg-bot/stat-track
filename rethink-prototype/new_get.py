# this is a rewrite of the get-tweets script
# using rethink db and a rewrite of the pipe
# scripts.
##############################
# imports
from tweepy import StreamListener
import tweepy
import json
import sys
import rethinkdb as r
from conn import conn
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import subprocess


##############################
# tweepy auth objects
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


##############################
# tweepy stream listener
class listener(StreamListener):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def add_to_db(self, some_json):
        r.db('aggregator') \
            .table('default') \
            .insert(some_json) \
            .run()

    def trim_tweets(self, tweet):
        # jq subprocess
        pass

    def on_status(self, status):
        # do something with each tweet
        tweet = status._json
        self.add_to_db(tweet)
        print('Added tweet #{} to database'.format(self.counter))
        self.counter += 1
        if self.counter == limit:
            sys.exit()


##############################
# if name == main
if __name__ == '__main__':
    print('hello')

    # Set up rethinkdb
    # I don't think anything is required here

    # Run tweepy
    foo = listener()

    limit = sys.argv[2]
    limit = int(limit)

    word = sys.argv[1]
    stream = tweepy.Stream(auth=api.auth, listener=foo)
    stream.filter(track=[word])

