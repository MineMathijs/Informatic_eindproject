# .venv\scripts\activate

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("menu.html")


@app.route('/invoer')
def about():
    return render_template("menu2.html")


@app.route('/laad')
def laad():
    return render_template("laad.html")
