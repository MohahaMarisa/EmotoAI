class Robot(object):
    
    def __init__(self, joints):
        self.joints = joints 

    def executeMove(self, moveDict):
        moveLen = len(moveDict['foot']) 
        for i in range(moveLen):
            if 'foot' in self.joints:
                self.joints['foot'].setAngle(moveDict['foot'][i])
            if '
            
