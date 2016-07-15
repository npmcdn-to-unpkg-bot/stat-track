# Get tweets ready for jq

import sys
import rethinkdb as r
import json
from conn import conn


response = r.db('aggregator').table('default').run()

