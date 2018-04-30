import time, sched
import math

class Robot(object):
    
    def __init__(self, joints):
        self.joints = joints 
        self.framerate = 30 
    def incrementMove(self, i, moveDict):
        #if 'foot' in self.joints:                                           
        #    self.joints['foot'].setAngle(moveDict['foot'][i])
        if 'shoulder' in self.joints:
            self.joints['shoulder'].setAngle(moveDict['shoulder'][i])
        if 'elbow' in self.joints:
            self.joints['elbow'].setAngle( moveDict['elbow'][i])
        if 'wrist' in self.joints:
            #we may need to add 90 to the wrist
            self.joints['wrist'].setAngle(moveDict['wrist'][i] - 110)
        if 'neck' in self.joints:
            self.joints['neck'].setAngle(moveDict['neck'][i])
        if 'phone' in self.joints:
            self.joints['phone'].setAngle(moveDict['phone'][i])

    def executeMove(self, moveDict):
        moveLen = len(moveDict['phone']) 
        print("moveLen: ", moveLen); 
        i = 0
#        time_time = time.time
#        start = time_time()
#        period = 1.0 / self.framerate
        while(i < moveLen):
            #if (time_time() - start) > period:
                #start += period
            self.incrementMove(i, moveDict)
            i+=1

    def setManyAngles(self): 
        moveSet = dict()
        for joint in self.joints:
            print(joint)
            a = self.joints[joint].setAngleMode()
            moveSet[joint] = a
        print(moveSet)

    def setJoint(self, joint, angle):
        desiredJoint = self.joints[joint]
        desiredJoint.setAngle(angle)

    def initializePosition(self):
        for joint in self.joints:
            if joint == "neck":
                self.joints['neck'].setSinAngle(75)
            else:
                self.joints[joint].setSinAngle(0)

    def moveToPos(self, moveSet, pool, functionSet = dict(), epSet = dict()):
        elbow = self.joints['elbow']
        shoulder = self.joints['shoulder']
        wrist = self.joints['wrist']
        neck = self.joints['neck']
        phone = self.joints['phone']

        for joint in self.joints:
            if (joint in functionSet):
                self.joints[joint].interpfunction = functionSet[joint]
            else:
                self.joints[joint].interpfunction = math.sin
            if (joint in epSet): 
                self.joints[joint].ep = epSet[joint] 
            else:
                self.joints[joint].ep = math.pi/2
        
        
        pool.add_task(elbow.setSinAngle, moveSet['elbow'], self.joints['elbow'].interpfunction, self.joints['elbow'].ep)
        pool.add_task(shoulder.setSinAngle, moveSet['shoulder'], self.joints['shoulder'].interpfunction, self.joints['elbow'].ep)
        pool.add_task(wrist.setSinAngle, moveSet['wrist'], self.joints['wrist'].interpfunction, self.joints['wrist'].ep)
        pool.add_task(neck.setSinAngle, moveSet['neck'], self.joints['neck'].interpfunction, self.joints['neck'].ep)
        pool.add_task(phone.setSinAngle, moveSet['phone'], self.joints['phone'].interpfunction, self.joints['phone'].ep)
        pool.wait_completion()
      
