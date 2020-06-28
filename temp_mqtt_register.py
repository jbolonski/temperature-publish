#!/usr/bin/env python
import yaml
from time import sleep
from datetime import datetime
import paho.mqtt.client as mqtt
import json

action=input("(R)egister or (U)nregister from HomeAssistant (R/U) :")
if action.upper()=="R":
    registrationData='{"device_class": "temperature", "name": "Garage Temperature", "state_topic": "homeassistant/sensor/sensorGarageTemp/state", "unit_of_measurement": "°F" }'
    print("Starting Temperature Monitor Registration")
else:
    registrationData=''
    print("Starting Temperature Monitor Removal")



print("Loading Configuration")
with open("configuration.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile,Loader=yaml.FullLoader)


print( "Connecting to MQTT @ " + cfg['mqtt']['server'] )

mqttc=mqtt.Client()
mqttc.username_pw_set(username=cfg['mqtt']['username'], password=cfg['mqtt']['password'])
mqttc.connect(cfg['mqtt']['server'],cfg['mqtt']['port'],60)
mqttc.loop_start()


try:
    mqttc.publish("homeassistant/sensor/sensorGarageTemp/config",registrationData,2)
except:
    print("Error Registering")


mqttc.loop_stop()
mqttc.disconnect()

