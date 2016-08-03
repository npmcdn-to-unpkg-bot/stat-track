
from flask import Flask, render_template
import requests
import json
import os
import sys
import traceback
import subprocess



app = Flask(__name__)

@app.route('/')
def home():

    target = 'http://web_api:5000'

    try:
        res = requests.get(target)
    except:
        output = subprocess.check_output("curl web_api:5000", shell=True)
        msg = 'subp output: {}'.format(output)
    else:
        msg = res.text


    return render_template('home.html', attempt=target, msg=msg)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
