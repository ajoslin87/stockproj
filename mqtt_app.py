import requests_html
import paho.mqtt.client as mqtt
import time 
import datetime
import json
import pandas as pd
import talib
import yfinance as yf



starting_date = datetime.datetime.now() - datetime.timedelta(30)

ending_date = datetime.datetime.now()

def on_connect(client, userdata, flags, rc):
    print("rc" + str(rc))
    mqttc.subscribe("aj/switch/#", 2)

def on_message(client, userdata, msg):
    if(msg.topic != "aj/switch/send_back"):
        ticker = msg.payload.decode()
        data = yf.download(ticker, start='2020-01-01', end='2021-08-01')
        mqtt_topic = msg.topic.replace("aj/switch/", '')
        topic_and_message = getattr(talib, mqtt_topic)(data['Open'], data['High'], data['Low'], data['Close'])
        
        topic_and_message.to_csv("csv_files/" +ticker+ '.csv')
        
        json_hits= {ticker: topic_and_message.to_json(orient='index')}
        mqttc.publish("aj/switch/send_back", json.dumps(json_hits))
    
mqttc = mqtt.Client("4e0c52019c6b46788ce6768949194d88")
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("broker.hivemq.com", 1883,60)
mqttc.loop_forever()
