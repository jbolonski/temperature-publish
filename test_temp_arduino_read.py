#!/usr/bin/env python

import yaml
import serial
from time import sleep
from datetime import datetime
import json

print("Starting Temperature Monitor Arduino Test")

print("Loading Configuration")
with open("configuration.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile,Loader=yaml.FullLoader)


print("Connecting to Arduino")

arduino=serial.Serial(cfg['arduino']['device'],cfg['arduino']['baud'], timeout=cfg['arduino']['timeout'])
with arduino:
    arduino.setDTR(False)
    sleep(1)
    arduino.flushInput()
    arduino.flushOutput()
    arduino.setDTR(True)
    
    arduino.write(str('H'))
    sleep(1)
    connect=arduino.readline()
    print(connect)

    arduino.write(str('T'))
    sleep(1)
    result=arduino.readline()
    data=json.loads(result)
    tempC = float(data["Temperature"])
    tempF = (tempC * 1.8)+32
    tempData = "{0:.1f}".format(tempF)
    timeData = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    logData = timeData + ", " + tempData + " F"
    print(logData)

