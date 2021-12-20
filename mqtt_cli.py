import paho.mqtt.client as mqtt

print("initializing")

def on_connect(client, userdata, flags, rc):
    print("Hello")

# def on_message(client, msg):
#     simpler_call(msg.payload)

mqttc = mqtt.Client("MQTT_FX_Client")
mqttc.on_connect = on_connect
# mqttc.on_message = on_message
mqttc.connect("broker.hivemq.com", 1883,60)
mqttc.loop_forever()