from __future__ import division
import time
import string
import math

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

numTicks = 4096 #number of ticks per cycle
hz = 60        #frequency of cycle
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

servo_min_time = 900
servo_max_time = 2100
theta = 0.0; 
while True:
    name = raw_input("enter time value ")
    if name == "end" : break
    pwm.set_pwm(2, 0, calcPulseLen(int(name)))

pwm.set_pwm(2, 100, 0) 
