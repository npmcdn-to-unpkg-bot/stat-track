
from flask import Flask
import json
import rethinkdb as r
from conn import c, init_dbs
import json


#########################
tab = init_dbs()


app = Flask(__name__)

@app.route('/')
def home():

    response = []
    raw = tab.pluck('numbers').run(c)

    for doc in raw:
        response.append(doc)

    data = response[0]['numbers']

    data = json.dumps(data)

    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
