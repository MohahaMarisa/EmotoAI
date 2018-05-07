from threading import Thread
import math

class Servo(object): 
    
    def __init__(self, pwm, channel, servoPulseTimeMin, servoPulseTimeMax, 
                 safeMinTime, safeMaxTime, printing=False, servoAngleMin=0.0, servoAngleMax = 180.0, frequency=60.0):
        

        #these values below represent the maximum rotation times for the servo,
        #but say nothing about the saftey of these rotations
        self.minTime = servoPulseTimeMin #this time should be calibrated so this is 0
        self.maxTime = servoPulseTimeMax #this time should be calibrated so this is angleMax 
      
        #these times are the safe range of movement for each servo  
        self.safeMinTime = safeMinTime
        self.safeMaxTime = safeMaxTime 

        #these degree values are the servos hard stops for motion, defaulted from [0, 180.0]
        self.angleMin = servoAngleMin
        self.angleMax = servoAngleMax
        
        self.pwm = pwm
        self.channel = channel
        #define our constants 
        self.NUM_TICKS = 4096
        self.FREQUENCY = frequency
        self.TIME_PER_TICK = 1/self.FREQUENCY
        self.TIME_PER_TICK = self.TIME_PER_TICK * 1000
        self.TIME_PER_TICK /= self.NUM_TICKS
        self.TIME_PER_TICK *= 1000
        
        self.currentAngle = 20 
        self.newAngle = None
        self.interpfunction = math.sin
        self.endPeriod = math.pi/2 
        self.printing = printing
    
    def constrain(self,val, minVal, maxVal):
        return min(maxVal, max(minVal, val))
    def specialSin(self,x): 
        return ((x/2)**2)
    def setAngle(self, angle):
        timeForAngle = self.servoMap(angle)
        self.pwm.set_pwm(self.channel, 0, int(self.calcPulseLen(timeForAngle)))
    
    def setSinAngleHelper(self, wavefn, endPeriod, speed):

        currAnglePulse = self.servoMap(self.currentAngle, self.angleMin, self.angleMax)
        currAnglePulse = self.constrain(currAnglePulse, self.safeMinTime, self.safeMaxTime)
        
        finalAnglePulse = self.servoMap(self.newAngle, self.angleMin, self.angleMax)
        finalAnglePulse = self.constrain(finalAnglePulse, self.safeMinTime, self.safeMaxTime);  

        pulseDiff = finalAnglePulse - currAnglePulse
        
        theta = 0.0
         
        i = 0; 
        while (theta <= endPeriod):
            currentMS = currAnglePulse + (wavefn(theta) * pulseDiff)
#            if(self.printing):
#                print("wavefn(theat): ", wavefn(theta))
            self.pwm.set_pwm(self.channel, 0, int(self.calcPulseLen(currentMS)))
            theta += speed    
            i+=1 
    
    def run(self):
        self.setSinAngleHelper()
    
    def setSinAngle(self, angle, wavefn=math.sin, endPeriod=math.pi/2, speed=0.006):
        #self.thread = Thread(target=self.run)
        self.newAngle = angle
        self.setSinAngleHelper(wavefn, endPeriod, speed)
        #self.thread.start()
        #self.thread.join()
        self.currentAngle = angle
    
    def servoMap(self, angle, servoMinAngle, servoMaxAngle): 
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
        finalAngle = 0 
        while True: 
            name = raw_input("enter angle` value ")
            if name == "end" : break
            self.setSinAngle(int(name))
            finalAngle = int(name) 
            print(name)
        return finalAngle
           
