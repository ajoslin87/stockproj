import ccxt
import auth

import paho.mqtt.client as mqtt

ftx = ccxt.ftx({
    'apiKey':auth.API_KEY,
    'secret':auth.API_SECRET,
    "hostname":'ftx.us'
})

def get_quote(request):

    # data = request.get_json()

    order = ftx.create_market_buy_order(request, 1)

    print(order)

    return order


def on_connect(client, userdata, flags, rc):
    print("rc" + str(rc))
    mqttc.subscribe("aj/ftx/#", 2)

def on_message(client, userdata, msg):
    # if(msg.topic != "aj/ftx/send_back"):
    #     get_quote(msg.payload.decode())
    #     print(msg.payload.decode())

    mqtt_topic = msg.topic.split('/')
    master_topic = mqtt_topic[1]
    print(master_topic)

mqttc = mqtt.Client("4e0c52019c6b46788ce6768949194d88")
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("broker.hivemq.com", 1883,60)
mqttc.loop_forever()