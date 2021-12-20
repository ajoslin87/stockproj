from flask_cors import CORS, cross_origin
import requests_html
from yahoo_fin import stock_info as si
# from yahoo_fin import get_quote_table as qt
import paho.mqtt.client as mqtt
import time 
import datetime
import json
import pandas as pd
from flask import Flask, render_template, url_for, request

app = Flask (__name__)
CORS(app)

print("initializing")

@app.route('/', methods = ['POST', 'GET'])
@cross_origin()

def index():
    if request.method == 'POST':
        ticker_content = request.form['ticker_content']
        # queryRepeatedly(ticker_content)
        simpler_call(ticker_content)
        return render_template('index.html')
    else:   
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)