import paho.mqtt.client as mqtt
import json
from tapo_plug import tapoPlugApi

device = {
    "tapoIp": "192.168.43.77",
    "tapoEmail": "smidla@gmail.com",
    "tapoPassword": "sopron2022"
}
bulbOn = True

def on_connect(client, userdata, flags, rc):
    print("Csatlakoztunk a brokerhez, ezzel a koddal: "+str(rc))
    client.subscribe("v1/devices/me/rpc/request/+")
    #threading.Timer(1, send).start()
    #quit()
    
def on_message(client, userdata, msg):
	global device
	global bulbOn
	print(msg.topic+" "+str(msg.payload))
	#return 0
	data = json.loads(msg.payload)
	print(data["method"])
	if data["method"] == "setValue":
		state = data["params"]
		print(state)
		if state == True:
			print("be")
			tapoPlugApi.plugOn(device)
			bulbOn = True
		else:
			print("ki")
			tapoPlugApi.plugOff(device)
			bulbOn = False
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("kw2GPEyeV7hQr8uCujKr", "")

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()
