from flask import Flask, render_template
import rethinkdb as r


HOST = '45.55.172.73'
PORT = 32769

r.connect(HOST,PORT).repl()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/API')
def API():
    return render_template('api.html')

if __name__ == '__main__':
    app.run(debug=True)
