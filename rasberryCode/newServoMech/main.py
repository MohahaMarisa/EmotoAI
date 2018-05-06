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
joints['foot'] = foot; """ #Shoulder Servo - HS755HB
SHOULDER_CHANNEL = 1
#hard limits
SHOULDER180_MIN = 600 
SHOULDER180_MAX = 2400

#soft limit
SHOULDER_MINTIME = 600
SHOULDER_MAXTIME = 2200

shoulder = Servo(pwm, SHOULDER_CHANNEL, SHOULDER180_MIN, SHOULDER180_MAX)
joints['shoulder'] = shoulder

#Elbow Servo - HS645MG
ELBOW_CHANNEL = 2

#150 degrees of freedom as is! 
ELBOW180_MIN = 850
ELBOW180_MAX = 2250

ELBOW_MINTIME = 850
ELBOW_MAXTIME = 2400

elbow = Servo(pwm, ELBOW_CHANNEL, ELBOW180_MIN, ELBOW180_MAX) 
joints['elbow'] = elbow

#Wrist Servo - HS645MG 
WRIST_CHANNEL = 5

WRIST180_MIN = 650
WRIST180_MAX = 2520

WRIST_MINTIME = 1300
WRIST_MAXTIME = 2520

wrist = Servo(pwm, WRIST_CHANNEL, WRIST180_MIN, WRIST180_MAX)
joints['wrist'] = wrist

#Neck Servo - HS422
NECK_CHANNEL = 4

NECK180_MIN = 600
NECK180_MAX = 2590

NECK_MINTIME = 600
NECK_MAXTIME = 2590

neck = Servo(pwm, NECK_CHANNEL, NECK180_MIN, NECK180_MAX)
joints['neck'] = neck

#Phone Servo - HS645MG
PHONE_CHANNEL = 3
PHONE180_MIN = 553
PHONE180_MAX = 2520


PHONE_MINTIME = 553
PHONE_MAXTIME = 2520

phone = Servo(pwm, PHONE_CHANNEL, PHONE180_MIN, PHONE180_MAX)
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
    receivingPhone = {'shoulder': 65, 'elbow': 30, 'wrist': 63, 'neck': 90, 'phone': 90}
    receivingPhone2 ={'shoulder': 35, 'elbow': 45, 'wrist': 95, 'neck': 90, 'phone': 90}
    receivingPhone3 =  {'shoulder': 75, 'elbow': 18, 'wrist': 120, 'neck': 90, 'phone': 90}
    headShake = {'shoulder': 75, 'elbow': 18, 'wrist': 120, 'neck': 70, 'phone': 90}
    headShake2 = {'shoulder': 75, 'elbow': 18, 'wrist': 120, 'neck': 110, 'phone': 90}
    headShake3 = {'shoulder': 75, 'elbow': 18, 'wrist': 120, 'neck': 70, 'phone': 90}
    headShake4 = {'shoulder': 75, 'elbow': 18, 'wrist': 120, 'neck': 110, 'phone': 90}
    activeMode2 ={'shoulder': 35, 'elbow': 45, 'wrist': 90, 'neck': 90, 'phone': 0}

	 
    moveSetArray = []
    moveSetArray.extend([receivingPhone,receivingPhone2,receivingPhone3,headShake,headShake2,headShake3,\
    headShake4,activeMode2])
    #moveSetArray[0] =  

    for pos in moveSetArray:
        robit.moveToPos(pos, pool); 

def smoothInitializePosition(robit,pool):
	initialPos = {'shoulder': 65, 'elbow': 30, 'wrist': 63, 'neck': 90, 'phone': 90}
	robit.moveToPos(initialPos,pool)


if __name__=='__main__':
    pool = ThreadPool(5)    
    #robit.initializePosition()
    while(True):
    	smoothInitializePosition(robit,pool)
    	command = raw_input("enter start to begin movement")
    	connectPhone(pool)
	command2 = raw_input("enter to restart loop")








