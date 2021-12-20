import talib
import yfinance as yf
import pandas as pd
import paho.mqtt.client as mqttc
import json


pd.set_option("display.max_rows", None, "display.max_columns", None)

class Mqttcalls:

        def get_data(ticker):
        
                data = yf.download(ticker, start='2020-01-01', end='2021-08-01')

                morningstar = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

                # engulf = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

                hits = (morningstar[morningstar != 0]).to_json(orient='index')
                
                json_hits= {ticker: hits}

                print (json_hits)

                return json.dumps(json_hits)