from robot import Robot
from servo import Servo
import math
import Adafruit_PCA9685
import time
from pool import ThreadPool

FREQ = 60; 
joints = dict()

pwm = Adafruit_PCA9685.PCA9685(0x40) 
pwm.set_pwm_freq(FREQ) 
pwm2 = Adafruit_PCA9685.PCA9685(0x41)
pwm2.set_pwm_freq(300.0)
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

shoulder = Servo(pwm, SHOULDER_CHANNEL, SHOULDER180_MIN, SHOULDER180_MAX, SHOULDER_MINTIME, SHOULDER_MAXTIME, "shoulder", printing = True)
joints['shoulder'] = shoulder

#Elbow Servo - HS645MG
ELBOW_CHANNEL = 2

#150 degrees of freedom as is! 
ELBOW180_MIN = 850
ELBOW180_MAX = 2250

ELBOW_MINTIME = 1150 
ELBOW_MAXTIME = 2400 

elbow = Servo(pwm2, ELBOW_CHANNEL, ELBOW180_MIN, ELBOW180_MAX, ELBOW_MINTIME, ELBOW_MAXTIME, "elbow", servoAngleMax = 150.0, frequency=300.0) 
joints['elbow'] = elbow

#Wrist Servo - HS645MG 
WRIST_CHANNEL = 5

WRIST180_MIN = 650
WRIST180_MAX = 2520

WRIST_MINTIME = 700 
WRIST_MAXTIME = 2520

wrist = Servo(pwm, WRIST_CHANNEL, WRIST180_MIN, WRIST180_MAX, WRIST_MINTIME, WRIST_MAXTIME, "wrist")
joints['wrist'] = wrist

#Neck Servo - HS422
NECK_CHANNEL = 4

NECK180_MIN = 600
NECK180_MAX = 2590

NECK_MINTIME = 600
NECK_MAXTIME = 2590

neck = Servo(pwm, NECK_CHANNEL, NECK180_MIN, NECK180_MAX, NECK_MINTIME, NECK_MAXTIME, "neck")
joints['neck'] = neck

#Phone Servo - HS645MG
PHONE_CHANNEL = 3
PHONE180_MIN = 553
PHONE180_MAX = 2520


PHONE_MINTIME = 553
PHONE_MAXTIME = 2520

phone = Servo(pwm, PHONE_CHANNEL, PHONE180_MIN, PHONE180_MAX, PHONE_MINTIME, PHONE_MAXTIME, "phone")
joints['phone'] = phone
robit = Robot(joints)

moveSet = {
    'shoulder': 40, 
    'elbow' : 70, 
    'wrist' : 40, 
    'neck' : 76, 
    'phone': 40
}

def square(x):
    return (x)**2

def negSquare(x):
    return -((x)-1)**2 + 1
def sawTooth(x): 
    return math.sin(x - math.sin(x) / 2)


def smoothInitializePosition(robit, pool):
    initialPos = {'shoulder': 20, 'elbow': 50, 'wrist': 0, 'neck': 90, 'phone': 0, 'speed':0.004}
    robit.moveToPos(initialPos,pool)

def noNoise(robit, pool):
    pos = {'shoulder': 0, 'elbow':90, 'wrist':0, 'neck':90, 'phone':0, 'speed':0.004}
    robit.moveToPos(pos, pool)

if __name__=='__main__':
    try:
        pool = ThreadPool(5)
        smoothInitializePosition(robit, pool)
        while(True):
            robit.setManyAngles()
    except KeyboardInterrupt: 
        print("keyboard interruption")
        robit.writePositions()
        







