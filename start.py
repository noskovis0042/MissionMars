from flask import Flask, render_template, redirect
import json

app = Flask(__name__)


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:prof>')
def training(prof):
    return render_template('base.html', title=prof)


if __name__ == "__main__":
    app.run()
