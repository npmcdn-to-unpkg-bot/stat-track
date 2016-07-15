from flask import Flask, render_template
import rethinkdb as r


HOST = '45.55.172.73'
PORT = 32769

r.connect(HOST,PORT).repl()


app = Flask(__name__)

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/visits')
def visits():
    return render_template('visits.html')

@app.route('/API')
def API():
    return render_template('api.html')
<<<<<<< HEAD
=======

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')
>>>>>>> 766799e5159bd90d4b284fa9d91ba6e32e51cefd

if __name__ == '__main__':
    app.run(debug=True)
