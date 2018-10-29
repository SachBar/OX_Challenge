from app import app
from flask import jsonify, render_template

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd

data = 'data/final.csv'

global bool


@app.route('/')
@app.route('/index')
@app.route('/graph_example')
def graph_example():
    return render_template('index.html')


@app.route('/test')
def test():
    global bool
    if bool == 0:
        response = {'discount': False, "timeRemaining": 60}
    else:
        response = {'discount': True, "timeRemaining": 60}

    return jsonify(response)


@app.route('/value/<x>')
def value(x):
    print(x)
    df = pd.read_csv(data)
    global bool
    if df.iloc[int(x)-1, 2] - df.iloc[int(x)-1, 1] > 0:
        bool = 1
    else:
        bool = 0
    return render_template('index.html')
