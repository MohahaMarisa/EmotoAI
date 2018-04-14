""" from __future__ import division
import time
import string


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

servo_min_time = 556
servo_max_time = 2501

while True:
    name = raw_input("enter time value ")
    if name == "end" : break
    pwm.set_pwm(0, 0, calcPulseLen(int(name)))
"""
class Servo(object): 
    
    def __init__(self, pwm, channel, servoPulseTimeMin, servoPulseTimeMax, frequency=60):
        self.minTime = servoPulseTimeMin #this time should be calibrated so this is 0
        self.maxTime = servoPulseTimeMin #this time should be calibrated so this is 180
        self.pwm = pwm
        self.channel = channel
        #define our constants 
        self.NUM_TICKS = 4096
        self.FREQUENCY = frequency
        self.TIME_PER_TICK = ((1/self.FREQUENCY * 1000) / self.NUM_TICKS) * 1000; 
   
   def setAngle(self, angle):
       timeForAngle = servoMap(self, angle); 
       self.pwm.set_pwm(self.channel, 0, int(calcPulseLen(time)))

    def servoMap(self, angle, servoMinAngle=0, servoMaxAngle=180)

        rightMin = self.minTime
        rightMax = self.maxTime
    
        leftMin = servoMinAngle
        leftMax = servoMaxAngle
        
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)
