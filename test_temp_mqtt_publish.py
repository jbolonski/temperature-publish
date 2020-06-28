#!/usr/bin/env python

import yaml
from time import sleep
from datetime import datetime
import paho.mqtt.client as mqtt
import json

print("Starting Temperature Monitor")

print("Loading Configuration")
with open("configuration.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile,Loader=yaml.FullLoader)


print("Connecting to MQTT @ " + cfg['mqtt']['server'])

mqttc=mqtt.Client()
mqttc.username_pw_set(username=cfg['mqtt']['username'], password=cfg['mqtt']['password'])
mqttc.connect(cfg['mqtt']['server'],cfg['mqtt']['port'],60)
mqttc.loop_start()

print("Connecting to Fake Arduino Temp Monitor")

while True:
    sleep(1)
    tempC = 20
    tempF = (tempC * 1.8)+32
    tempData = "{0:.1f}".format(tempF)
    timeData = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        mqttc.publish("homeassistant/sensor/sensorGarageTemp/state",tempData,2)
    except:
        print('error publishing')

    logData = timeData + ", " + tempData + " F"
    print(logData)

    sleep( cfg['intervals']['temperature'] )


mqttc.loop_stop()
mqttc.disconnect()

