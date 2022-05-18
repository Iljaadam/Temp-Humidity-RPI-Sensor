#!/usr/bin/env python3
#############################################################################
# Filename    : DHT11.py
# Description :	read the temperature and humidity data of DHT11
# Author      : freenove
# modification: 2020/10/16
########################################################################
import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT
import json
from os import path
DHTPin = 11     #define the pin of DHT11
list_of_temperatures = list()
list_of_humidities = list()
def loop():
    dht = DHT.DHT(DHTPin)   #create a DHT class object
    counts = 0 # Measurement counts
    while(True):
        counts += 1
        print("Measurement counts: ", counts)
        for i in range(0,15):            
            chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                print("DHT11,OK!")
                break
            time.sleep(0.1)
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
        
        if path.isfile(data_humidities.json) is False:
            raise Exception("File not found")
        with open(data_humidities.json) as hdties:
            templist_humidity = json.load(hdties)
        templist_humidity.append(dht.humidity)

        if path.isfile(data_temperatures.json) is False:
            raise Exception("File not found")
        with open(data_temperatures.json) as temps:
            templist_temperatures = json.load(temps)
        templist_temperatures.append(dht.temperature)

        with open(data_temperatures.json) as json_temperatures:
            json.dump(templist_temperatures, json_temperatures)
        with open(data_humidities.json) as json_humidities:
            json.dump(templist_humidity, json_humidities)

        time.sleep(30)       
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()  


