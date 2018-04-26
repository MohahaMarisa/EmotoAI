import time, sched
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
        for joint in self.joints:
            print(joint)
            self.joints[joint].setAngleMode()

    def setJoint(self, joint, angle):
        desiredJoint = self.joints[joint]
        desiredJoint.setAngle(angle)
