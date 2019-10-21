import os
import time
import Adafruit_ADS1x15
from time import sleep
from datetime import datetime
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
scale = 6.144/32767

file = open("./data_log.csv","a")

while True:
    wind_ads = adc.read_adc(1, gain = 2/3)
    temp_ads = adc.read_adc(2, gain = 2/3)
    battery_ads = adc.read_adc(3, gain = 2/3)
    wind_voltage = wind_ads*scale
    temp_voltage = temp_ads*scale
    battery_voltage = battery_ads*scale*5
    zero_wind_volt = 1.30
    temp = (temp_voltage-0.4)/0.0195
    if (wind_voltage-zero_wind_volt)<0:
        wind_vel = 0
    else: 
        wind_vel = (((wind_voltage-zero_wind_volt)/(3.038517*(temp**0.115157)))/0.087288)**3.00964
    
    print 'The wind velocity is:',wind_vel,'mph'
    print 'The temperature is:',temp
    print 'The voltage is:', battery_voltage
    file.write(str(wind_vel) + "," + str(datetime.now())[0:19]+","+str(battery_voltage)+"\n")
    time.sleep(1)

