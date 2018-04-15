class Robot(object):
    
    def __init__(self, joints):
        self.joints = joints 

    def executeMove(self, moveDict):
        moveLen = len(moveDict['foot']) 
        print("moveLen: ", moveLen); 
        for i in range(moveLen):
            #if 'foot' in self.joints:
            #    self.joints['foot'].setAngle(moveDict['foot'][i])
            if 'shoulder' in self.joints:
                self.joints['shoulder'].setAngle(moveDict['shoulder'][i])
            if 'elbow' in self.joints:
                self.joints['elbow'].setAngle(moveDict['elbow'][i])
            if 'wrist' in self.joints:
                self.joints['wrist'].setAngle(moveDict['wrist'][i])
            if 'neck' in self.joints:
                self.joints['neck'].setAngle(moveDict['neck'][i])
            if 'phone' in self.joints:
                self.joints['phone'].setAngle(moveDict['phone'][i])

    def powerDown(self): 
        for joint in self.joints:
            self.joints[joint].setAngle(self.joints[joint].minTime)
