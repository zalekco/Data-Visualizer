from main import app
from flask import render_template, url_for


@app.route("/")
def main():
    return render_template('main.html')