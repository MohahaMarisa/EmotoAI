from robot import Robot
from servo import Servo
import math
import Adafruit_PCA9685

FREQ = 60; 
joints = dict()

pwm = Adafruit_PCA9685.PCA9685() 
pwm.set_pwm_freq(FREQ); 

"""
#Foot Servo
FOOT_CHANNEL = 0
FOOT_MINTIME = 
FOOT_MAXTIME = 

foot = Servo(pwm, FOOT_CHANNEL, FOOT_MINTIME, FOOT_MAXTIME)

joints['foot'] = foot;
"""

#Shoulder Servo - HS755HB
SHOULDER_CHANNEL = 1
SHOULDER_MINTIME = 600
SHOULDER_MAXTIME = 2200

shoulder = Servo(pwm, SHOULDER_CHANNEL, SHOULDER_MINTIME, SHOULDER_MAXTIME)
joints['shoulder'] = shoulder

#Elbow Servo - HS645MG
ELBOW_CHANNEL = 2
ELBOW_MINTIME = 390
ELBOW_MAXTIME = 2050

elbow = Servo(pwm, ELBOW_CHANNEL, ELBOW_MINTIME, ELBOW_MAXTIME)
joints['elbow'] = elbow

#Wrist Servo - HS425BB 
WRIST_CHANNEL = 3
WRIST_MINTIME = 553
WRIST_MAXTIME = 2520

wrist = Servo(pwm, WRIST_CHANNEL, WRIST_MINTIME, WRIST_MAXTIME)
joints['wrist'] = wrist

#Neck Servo - HS422
NECK_CHANNEL = 4
NECK_MINTIME = 610
NECK_MAXTIME = 2590

neck = Servo(pwm, NECK_CHANNEL, NECK_MINTIME, NECK_MAXTIME)
joints['neck'] = neck

#Phone Servo - HS311
PHONE_CHANNEL = 5
PHONE_MINTIME = 500
PHONE_MAXTIME = 2520

#phone = Servo(pwm, PHONE_CHANNEL, PHONE_MINTIME, PHONE_MAXTIME)
#joints['phone'] = phone
robit = Robot(joints)

moveSet = {
    'shoulderGoal': 40, 
    'elbowGoal' : 70, 
    'wristGoal' : 40, 
    'neckGoal' : 76, 
    'shoulderOffset' : 10,  
    'elbowOffset' : 30, 
    'wristOffset' : 60, 
    'neckOffset' : 65 
}

theta = 0.0


while(True):
    
    for joint in joints:
        currOffset = moveSet[joint + 'Offset']
        currGoal = moveSet[joint + 'Goal']

        robit.setJoint(joint, currOffset + (((1+math.sin(theta)) * (currGoal - currOffset)))); 

    #robit.setJoint('shoulder', 10 + (((1+math.sin(theta)) * (movementGoal-10))));
    #robit.setJoint('elbow', 10 + (((1+math.sin(theta)) * (movementGoal-10))));
    
    theta += 0.006


#if __name__ == '__main__':
#   robit.executeMove(dictionary)
    #robit.setManyAngles()
