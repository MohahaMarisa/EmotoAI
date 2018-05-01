from robot import Robot
from servo import Servo
import math
import Adafruit_PCA9685
import time
from pool import ThreadPool

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
ELBOW_MINTIME = 650
ELBOW_MAXTIME = 2450

elbow = Servo(pwm, ELBOW_CHANNEL, ELBOW_MINTIME, ELBOW_MAXTIME)
joints['elbow'] = elbow

#Wrist Servo - HS645MG 
WRIST_CHANNEL = 5
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

#Phone Servo - HS645MG
PHONE_CHANNEL = 3
PHONE_MINTIME = 553
PHONE_MAXTIME = 2520

phone = Servo(pwm, PHONE_CHANNEL, PHONE_MINTIME, PHONE_MAXTIME)
joints['phone'] = phone
robit = Robot(joints)

moveSet = {
    'shoulder': 40, 
    'elbow' : 70, 
    'wrist' : 40, 
    'neck' : 76, 
    'phone': 40
}

def sawTooth(x): 
    return math.sin(x - math.sin(x) / 2)

def connectPhone(pool): 
    moveSetArray = []
    moveSetArray[0] =  

    for pos in moveSetArray:
        robit.moveToPos(pos, pool); 

    return
pos1 = {'shoulder': 10, 'elbow': 0, 'wrist': 35, 'neck': 75, 'phone': 0}
pos2 = {'shoulder': 50, 'elbow': 30, 'wrist': 35, 'neck': 95, 'phone': 30} 

pos2fn = {'shoulder': sawTooth, 'elbow': sawTooth, 'wrist':sawTooth}

pos3 = {'shoulder': 70, 'elbow': 50, 'wrist': 55, 'neck': 45, 'phone': 75} 

if __name__=='__main__':
    pool = ThreadPool(5)    
    robit.initializePosition()
    
    while(True): 
        robit.moveToPos(pos1, pool)
        robit.moveToPos(pos2, pool, pos2fn)
        robit.moveToPos(pos3, pool) 








