from flask import Flask, redirect, url_for, request, render_template
import os
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient(
        os.environ['DB_1_PORT_27017_TCP_ADDR'],
        27017)
db = client.homedb


@app.route('/')
def home():

    _items = db.homedb.find()
    items = [item for item in _items]

    return render_template('base.html', items=items)

@app.route('/new', methods=['POST'])
def new():

    item_doc = dict(
            name = request.form['name'],
            description = request.form['description']
            )
    db.homedb.insert_one(item_doc)
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
