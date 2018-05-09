from robot import Robot
from servo import Servo
import math
import Adafruit_PCA9685
import time
from pool import ThreadPool
from shiftrClient import pahoClient
import random
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
    return -((x-1)**2) + 1

def activeNeutral(robit, pool):
    theta = 0.0
    speed = 0.006


def connectPhone(pool):
    #rockBack = {'shoulder': 20, 'elbow': 65, 'wrist': 0, 'neck': 96, 'phone': 0, 'speed':0.001}
    #highPoint = {'shoulder': 40, 'elbow': 120, 'wrist': 110, 'neck': 96, 'phone': 0, 'speed':0.001}
    #launchForward = {'shoulder': 70, 'elbow': 50, 'wrist': 90, 'neck': 96, 'phone': 0, 'speed':0.001}

    rockBack = {'shoulder': 20, 'elbow': 65, 'wrist': 0, 'neck': 96, 'phone': 0, 'speed':0.004}
    highPoint = {'shoulder': 60, 'elbow': 120, 'wrist': 110, 'neck': 96, 'phone': 0, 'speed':0.004}
    launchForward = {'shoulder': 70, 'elbow': 50, 'wrist': 90, 'neck': 96, 'phone': 0, 'speed':0.006}
    finalPose = {'shoulder': 40, 'elbow': 100, 'wrist': 50, 'neck': 96, 'phone': 90} 
    
    #shake twice
    headshakeRight = {'shoulder': 70, 'elbow': 50, 'wrist': 90, 'neck': 117, 'phone': 0, 'speed': 0.039}
    headshakeLeft = {'shoulder': 70, 'elbow': 50, 'wrist': 90, 'neck': 75, 'phone': 0, 'speed': 0.039}
    
    
    #use these to return to the initialPosition
    negSquareDict = {'shoulder': negSquare, 'elbow': negSquare, 'wrist': negSquare, 'neck': negSquare, 'phone': negSquare}
    squareDict = {'shoulder':square, 'elbow':square, 'wrist':square, 'neck':square, 'phone':square}
    negSquareEPDict = {'shoulder': 2, 'elbow': 2, 'wrist':2, 'neck':2, 'phone':2}
    negSquareEP1 = {'shoulder':1, 'elbow': 1, 'wrist':1, 'neck':1, 'phone':1}
    
    robit.moveToPos(rockBack, pool, squareDict, negSquareEP1) 
    robit.moveToPos(highPoint, pool, squareDict, negSquareEP1)
    robit.moveToPos(launchForward, pool, negSquareDict, negSquareEP1)

    robit.moveToPos(headshakeRight, pool)
    robit.moveToPos(headshakeLeft, pool)
    robit.moveToPos(headshakeRight, pool)
    robit.moveToPos(headshakeLeft, pool)

    robit.moveToPos(finalPose, pool)

def quietMode(robit, pool):
    quietPos = {'shoulder': 0, 'elbow': 43, 'wrist': 0, 'neck': 96, 'phone': 0}
    robit.moveToPos(quietPos, pool)

def smoothInitializePosition(robit, pool):
    initialPos = {'shoulder': 20, 'elbow': 50, 'wrist': 0, 'neck': 96, 'phone': 0, 'speed':0.005}
    robit.moveToPos(initialPos,pool)


def off(robit, pool):
    receivingPhone = {'shoulder': 40, 'elbow': 65, 'wrist': 0, 'neck': 96, 'phone': 0} 
    robit.moveToPos(receivingPhone,pool)
def quiet(robit, pool):
    quietPos = {'shoulder':0, 'elbow':43, 'wrist':0, 'neck':95, 'phone':0, 'speed':0.004}
    robit.moveToPos(quietPos, pool)

pool = ThreadPool(5)

def linear(x): 
    return 2*x
def listeningMode(robit, pool):
    #standing is lower than initialMode
    initialMode = {'shoulder': 50, 'elbow': 100, 'wrist': 45, 'neck': 70, 'phone': 90, 'speed':0.006} 
    
    initialModeCurves = {'shoulder':linear}
    initialModeEP= {'shoulder':0.5}
    
    negSquareDict = {'shoulder': negSquare, 'elbow': negSquare, 'wrist': negSquare, 'neck': negSquare, 'phone': negSquare}
    squareDict = {'shoulder':square, 'elbow':square, 'wrist':square, 'neck':square, 'phone':square}
    linDict = {'shoulder':linear, 'elbow':linear, 'wrist':linear, 'neck':linear, 'phone':linear}
    negSquareEPDict = {'shoulder': 2, 'elbow': 2, 'wrist':2, 'neck':2, 'phone':2}
    negSquareEP1 = {'shoulder':1, 'elbow': 1, 'wrist':1, 'neck':1, 'phone':1}
    
    #finalPositions
    standing = {'shoulder': 30, 'elbow': 70, 'wrist': 40, 'neck': 96, 'phone': 90, 'speed':0.006}     
    finalPos = {'shoulder':40, 'elbow':100, 'wrist':45, 'neck':70, 'phone':70, 'speed':0.017}
    
    currPos = standing;
    robit.moveToPos(currPos, pool); 
    
    for i in range(2): 
       initialMode['neck'] = neck.currentAngle
       standing['neck'] = neck.currentAngle
       if (i == 1):
            print("moving to initalMode (high)")
            robit.moveToPos(initialMode, pool, initialModeCurves, initialModeEP)
       else: 
            print('moving to standing (lower)')
            robit.moveToPos(standing, pool) 
       
       for j in range(3):
            newAngle = random.randint(40, 140) 
            if (i==1 and j == 2): 
                newAngle = 70
            else: 
                while (abs(newAngle - neck.currentAngle) < 40):
                    newAngle = random.randint(40, 140)
            neck.setAngle(newAngle)
            #standing['neck'] = newAngle
            #robit.moveToPos(standing, pool, linDict, negSquareEP1)
            time.sleep(1)

    robit.moveToPos(finalPos, pool)
        



def activeNormal(robit, pool):
    initialMode = {'shoulder': 40, 'elbow': 100, 'wrist': 50, 'neck': 96, 'phone': 90, 'speed': 0.019}
    slightlyRaised = {'shoulder': 50, 'elbow': 110, 'wrist': 70, 'neck': 96, 'phone': 90, 'speed': 0.014}

    for i in range(3):
        robit.moveToPos(slightlyRaised, pool)
        robit.moveToPos(initialMode, pool)


def noNoise(robit, pool):
    pos = {'shoulder': 0, 'elbow':90, 'wrist':0, 'neck':90, 'phone':0, 'speed':0.004}
    robit.moveToPos(pos, pool)
def onConnect(client, userdata, rc):
    print("absolutley connected")
    client.subscribe("emote")
    client.subscribe("motion", 2)

def onMessage(client, userdata, message):
    messageStr = str(message.payload.decode("utf-8"))
    print("message recieved: " + messageStr)
    if (messageStr == 'on'): connectPhone(pool)
    if (messageStr == 'off'): off(robit, pool)
    if (messageStr == 'happy'): listeningMode(robit, pool)
    if (messageStr == 'action'): quiet(robit, pool)
    if (messageStr == 'listen'): activeNormal(robit, pool)

smoothInitializePosition(robit, pool)

try:
    paho = pahoClient(onConnect, onMessage)
except KeyboardInterrupt:
    print("writing xml")
    robit.writePositions()
except Exception:
    print("writing xml")
    print("exception Thrown")
    robit.writePositions()
