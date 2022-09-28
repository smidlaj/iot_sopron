import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Csatlakoztunk a brokerhez, ezzel a koddal: "+str(rc))
    client.publish("v1/devices/me/telemetry", "{\"temperature\":40}")
    #quit()
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("ymRGMQtPtbOZwVQDhCDK", "")

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()