from tapo_plug import tapoPlugApi
  
device = {
    "tapoIp": "192.168.43.77",
    "tapoEmail": "smidla@gmail.com",
    "tapoPassword": "sopron2022"
}
  
response = tapoPlugApi.plugOff(device)
print(response)
