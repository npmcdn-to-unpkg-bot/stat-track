######### Streaming API ##########
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

auth = OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track = ['#DeleteYourAccount'])
