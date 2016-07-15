# Unit tests for new-get

import time
from new_get import listener
import rethinkdb as r
import pytest
import tweepy


# Constants
DATABASE = 'aggregator'
TABLE = 'default'

from keys import \
        CONSUMER_KEY, \
        CONSUMER_SECRET, \
        ACCESS_TOKEN, \
        ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


# Fix
@pytest.fixture
def conn():
    conn = r.connect('localhost',32769).repl()
    return conn

# Begin tests here
def test_the_listener_class_inserts_items_into_db(conn):
    current_count = r.db(DATABASE).table(TABLE).count()
    foo = listener()
    stream = tweepy.Stream(auth=api.auth, listener=foo)
    word = 'donald trump'
    stream.filter(track=[word])
    time.sleep(10)
    new_count = r.db(DATABASE).table(TABLE).count()
    current_count = int(current_count)
    new_count = int(new_count)
    assert new_count > current_count

    response = r.db(DATABASE).table(TABLE).delete()
    assert r.db(DATABASE).table(TABLE).count() == 0

