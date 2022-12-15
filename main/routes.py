from main import app
from flask import render_template, url_for


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/display")
def plot():
    return render_template('display.html')