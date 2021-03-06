from __future__ import division
import time
import string
import math

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm2 = Adafruit_PCA9685.PCA9685(0x41)

numTicks = 4096 #number of ticks per cycle
hz = 300        #frequency of cycle
freqlen = 1/hz  #time in seconds of a single period
freqlenMS = freqlen * 1000 #time in ms of a single period
print(freqlenMS)
timePerTick = freqlenMS / numTicks #time in ms of a single tick
timePerTick *= 1000 #time in us of a single period. 
print(timePerTick)

def calcPulseLen(time):
    
    return int(time / timePerTick)

freqPeriodMicroSec = 16666.666666667
pwm.set_pwm_freq(hz)
pwm2.set_pwm_freq(300.0)
servo_min_time = 900
servo_max_time = 2100
theta = 0.0; 
channelSet = False
channel = 4


while True:
    name = raw_input("enter time value ")
    if name == "end" : break
    
    if (not channelSet): 
        channel = int(name)
        channelSet = True
    else: 
        pwm.set_pwm(channel, 0, calcPulseLen(int(name)))
        pwm2.set_pwm(channel, 0, calcPulseLen(int(name)))

