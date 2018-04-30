from threading import Thread
import math

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
        self.pwm.set_pwm(self.channel, 0, int(self.calcPulseLen(timeForAngle)))
    
    def setSinAngleHelper(self, wavefn, endPeriod):

        currAnglePulse = self.servoMap(self.currentAngle)
        finalAnglePulse = self.servoMap(self.newAngle)
        
        pulseDiff = finalAnglePulse - currAnglePulse

        theta = 0.0
        speed = 0.006
        
        i = 0; 
        while (theta <= endPeriod):
            currentMS = currAnglePulse + (wavefn(theta) * pulseDiff)
            self.pwm.set_pwm(self.channel, 0, int(self.calcPulseLen(currentMS)))
            theta += speed    
            i+=1 
    
    def run(self):
        self.setSinAngleHelper()
        
    def setSinAngle(self, angle, wavefn = math.sin, endPeriod = math.pi/2):
        #self.thread = Thread(target=self.run)
        self.newAngle = angle
        self.setSinAngleHelper(wavefn, endPeriod)
        #self.thread.start()
        #self.thread.join()
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
            self.setSinAngle(int(name))
            print(name)

           
