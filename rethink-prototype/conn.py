# This will define the database connection

import sys
import json
import rethinkdb as r

conn = r.connect('45.55.172.73',32769).repl()


default = r.db('aggregator').table('default')

response = default.run()

data = []

for i in response:
    data.append(i)

data = json.dumps(data)
sys.stdout.write(data)
