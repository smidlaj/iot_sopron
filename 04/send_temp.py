import paho.mqtt.client as mqtt
import time
import threading
from random import random

temp = 38.5

def send():
    global temp 
    #temp += (random() - 0.5)*2
    print("Homerseklet kuldese: " + str(temp))
    client.publish("v1/devices/me/telemetry", "{\"temperature\":" + str(temp) + "}")
    threading.Timer(1, send).start()

def on_connect(client, userdata, flags, rc):
    print("Csatlakoztunk a brokerhez, ezzel a koddal: "+str(rc))
    threading.Timer(1, send).start()
    #quit()
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("uZnZbKBT72oc9o760djL", "")

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()
