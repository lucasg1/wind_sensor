# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1
scale = 6.144/32767

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
# Main loop.
while True:
    wind_ads = adc.read_adc(1, gain = 2/3) #gain=GAIN)
    temp_ads = adc.read_adc(2, gain = 2/3) #gain=GAIN)
    wind_voltage = wind_ads*scale
    temp_voltage = temp_ads*scale
    zero_wind_volt = 1.30
    temp = (temp_voltage-0.4)/0.0195
    if (wind_voltage-zero_wind_volt)<0:
        wind_vel = 0
    else: 
        wind_vel = (((wind_voltage-zero_wind_volt)/(3.038517*(temp**0.115157)))/0.087288)**3.00964
    
    print 'The wind velocity is:',wind_vel,'mph'
   # print 'Wind voltage =',wind_voltage
   # print 'Wind ads =',wind_ads
    print 'The temperatue is:',temp

    # Each value will be a 16 bit signed integer value
    # ADC (ADS1115 = 16-bit).
    
    # Pause for half a second.
    time.sleep(0.5)
