from flask import Flask, render_template
import rethinkdb as r


r.connect(HOST,PORT).repl()
# Get the HOST and PORT from the notes.


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
