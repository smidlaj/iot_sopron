import paho.mqtt.client as mqtt
import time
import threading
from random import random
import sys

print(len(sys.argv))
temp = 30
if len(sys.argv) == 2:
	temp = int(sys.argv[1])

requestId = 0

def send():
    global temp 
    temp += (random() - 0.5)*2
    print("Homerseklet kuldese: " + str(temp))
    client.publish("v1/devices/me/telemetry", "{\"temperature\":" + str(temp) + "}")
    #threading.Timer(1, send).start()

def on_connect(client, userdata, flags, rc):
	global requestId
	client.subscribe('v1/devices/me/attributes')
	client.subscribe('v1/devices/me/attributes/response/+')
	client.subscribe('v1/devices/me/rpc/request/+')
	print("Csatlakoztunk a brokerhez, ezzel a koddal: "+str(rc))
	#client.publish("v1/devices/me/rpc/request/" + str(requestId), 
	#	"{\"method\": \"cardState\", \"status\" : \"active\"}")
	#requestId += 1
	#threading.Timer(1, send).start()
	#quit()
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("3fslg8U7VUEslJakSSjW", "")

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()
