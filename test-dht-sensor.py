#!/usr/bin/python
import sys
import Adafruit_DHT

while True:
    sensor = Adafruit_DHT.DHT11
    # GPIO Port
    # Jeffrey - 
    gpio = 7

    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    print('Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(temperature, humidity))