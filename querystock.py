from yahoo_fin import stock_info as si
# from yahoo_fin import get_quote_table as qt
import paho.mqtt.client as mqtt
import time 
import datetime
import json
import requests
import requests_html
import pandas as pd

now = datetime.datetime.now()
timestamp = now.strftime("%H:%M:%S")
datestamp = now.strftime("%m:%d:%Y")


def get_live_pprice(ticker):

    ticker_price = si.get_live_price(ticker)

    d = {"date": timestamp, "price": ticker_price}

    df = pd.DataFrame(data=d, index = [0])

    return(df)


        
