from threading import Thread

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
servo_max_time = 250

while True:
    name = raw_input("enter time value ")
    if name == "end" : break
    pwm.set_pwm(0, 0, calcPulseLen(int(name)))
"""
class Servo(object): 
    
    def __init__(self, pwm, channel, servoPulseTimeMin, servoPulseTimeMax, frequency=60.0):
        self.minTime = servoPulseTimeMin #this time should be calibrated so this is 0
        self.maxTime = servoPulseTimeMax #this time should be calibrated so this is 180
        self.pwm = pwm
        self.channel = channel
        #define our constants 
        self.NUM_TICKS = 4096
        self.FREQUENCY = frequency
        self.TIME_PER_TICK = 1/self.FREQUENCY
        self.TIME_PER_TICK = self.TIME_PER_TICK * 1000
        self.TIME_PER_TICK /= self.NUM_TICKS
        self.TIME_PER_TICK *= 1000
        
        self.currentAngle = 0 
        self.newAngle = None
        

    def setAngle(self, angle):
        timeForAngle = self.servoMap(angle)
        print("Time For Given Angle: ", timeForAngle)
        self.pwm.set_pwm(self.channel, 0, int(self.calcPulseLen(timeForAngle)))
    
    def setSinAngleHelper(self):
        print("currAngle :", self.currentAngle)
        print("newAngle  :", self.newAngle)

        currAnglePulse = self.servoMap(self.currentAngle)
        finalAnglePulse = self.servoMap(self.newAngle)
        if currAnglePulse < finalAnglePulse: step = 1
        else: step = -1
        print("step: ", step) 
        for i in range(currAnglePulse, finalAnglePulse, step): 
            print("setting thing: ", i)
            self.pwm.set_pwm(self.channel, 0, int(self.calcPulseLen(i))) 
    
    def run(self):
        self.setSinAngleHelper()
        
    def setSinAngle(self, angle):
        self.thread = Thread(target=self.run)
        self.newAngle = angle
        self.thread.start()
        self.thread.join()     
        self.currentAngle = angle

    def servoMap(self, angle, servoMinAngle=0.0, servoMaxAngle=180.0): 
        value = angle;
        rightMin = self.minTime
        rightMax = self.maxTime
        leftMin = servoMinAngle
        leftMax = servoMaxAngle
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin
        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return int(rightMin + (valueScaled * rightSpan))

    def calcPulseLen(self, time):
        return time / self.TIME_PER_TICK

    def setAngleMode(self): 
        while True: 
            name = raw_input("enter time value ")
            if name == "end" : break
            self.setAngle(int(name))
            print(name)

           
