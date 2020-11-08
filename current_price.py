from yahoo_fin import stock_info as si
# from yahoo_fin import get_quote_table as qt
import paho.mqtt.client as mqtt
import time 
import datetime
import json

mqttc = mqtt.Client()

mqttc.connect("broker.hivemq.com", 1883,60)

print(si.get_quote_table('aapl')['Previous Close'])

# while True:

#     now = datetime.datetime.now()
#     timestamp = now.strftime("%H:%M:%S")

#     aapl_price = si.get_live_price("aapl")

#     gold_price = si.get_live_price("gold")

#     # print(now, live_price)
#     message = json.dumps({"aapl":aapl_price, "gold": gold_price, "time":timestamp})
#     print(message)
#     mqttc.publish("aj/switch/aapl", message)
#     # mqttc.publish("aj/switch/time", year)

#     time.sleep(30)