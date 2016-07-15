# This script delivers the trimmed tweets back to rethink

import rethinkdb as r
import sys
import json
from conn import conn


data = sys.stdin.readlines()
data = ''.join(data)
tweets = json.loads(data)


for tweet in tweets:
    r.db('aggregator').table('trimmed').insert(tweet).run()
