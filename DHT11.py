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
DHTPin = 11     #define the pin of DHT11
def loop():
    dht = DHT.DHT(DHTPin)   #create a DHT class object
     # Measurement counts
    while(True):
        for i in range(0,15):            
            chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                print("DHT11,OK!")
                break
            time.sleep(0.1)
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))

        def write_json(data, filename="data.json"):
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)

        dt = datetime.now()

        with open("data.json") as json_file:
            data = json.load(json_file)
            temp = data["data"]
            y = {"temperature": dht.temperature, "humidity": dht.humidity, "date": dt}
            temp.append(y)

        write_json(data)
        time.sleep(10)
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()  


