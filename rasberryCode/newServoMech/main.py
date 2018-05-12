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

    rockBack = {'shoulder': 30, 'elbow': 85, 'wrist': 0, 'neck': 96, 'phone': 0, 'speed':0.012}
    highPoint = {'shoulder': 40, 'elbow': 120, 'wrist': 110, 'neck': 96, 'phone': 0, 'speed':0.004}
    launchForward = {'shoulder': 70, 'elbow': 80, 'wrist': 90, 'neck': 96, 'phone': 0, 'speed':0.004}
    finalPose = {'shoulder': 40, 'elbow': 100, 'wrist': 50, 'neck': 96, 'phone': 90} 
    
    #shake twice
    headshakeRight = {'shoulder': 70, 'elbow': 80, 'wrist': 90, 'neck': 117, 'phone': 0, 'speed': 0.039}
    headshakeLeft = {'shoulder': 70, 'elbow': 80, 'wrist': 90, 'neck': 75, 'phone': 0, 'speed': 0.039}
    
    
    #use these to return to the initialPosition
    negSquareDict = {'shoulder': negSquare, 'elbow': negSquare, 'wrist': negSquare, 'neck': negSquare, 'phone': negSquare}
    squareDict = {'shoulder':linear, 'elbow':square, 'wrist':square, 'neck':square, 'phone':square}
    negSquareEPDict = {'shoulder': 2, 'elbow': 2, 'wrist':2, 'neck':2, 'phone':2}
    negSquareEP1 = {'shoulder':1, 'elbow': 1, 'wrist':1, 'neck':1, 'phone':1}
    neg = {'shoulder':0.3, 'elbow': 1, 'wrist':1, 'neck':1, 'phone':1}
    
    robit.moveToPos(rockBack, pool) 
    robit.moveToPos(highPoint, pool, squareDict, neg)
    robit.moveToPos(launchForward, pool, negSquareDict, negSquareEP1)

    robit.moveToPos(headshakeRight, pool)
    robit.moveToPos(headshakeLeft, pool)
    robit.moveToPos(headshakeRight, pool)
    robit.moveToPos(headshakeLeft, pool)

    robit.moveToPos(finalPose, pool)
    #paho.publishMessage("emoto")
    #listeningMode(robit, pool, True) 
    finalPos = {'shoulder': 30, 'elbow': 70, 'wrist': 40, 'neck': 96, 'phone': 90, 'speed':0.006}
    robit.moveToPos(finalPos, pool)

def quietMode(robit, pool):
    quietPos = {'shoulder': 0, 'elbow': 43, 'wrist': 0, 'neck': 96, 'phone': 0}
    robit.moveToPos(quietPos, pool)

def smoothInitializePosition(robit, pool):
    initialPos = {'shoulder': 20, 'elbow': 50, 'wrist': 0, 'neck': 96, 'phone': 0, 'speed':0.005}
    robit.moveToPos(initialPos,pool)

def oscilate(x):
    return ((-1) * math.cos(10 * x + math.pi/2)) 
def vertOSC(x):
    return ((-1) * math.cos(8 * x + math.pi/2))

def off(robit, pool):
    receivingPhone = {'shoulder': 40, 'elbow': 65, 'wrist': 0, 'neck': 96, 'phone': 0} 
    robit.moveToPos(receivingPhone,pool)
    #paho.publishMessage("phone")

def quiet(robit, pool):
    quietPos = {'shoulder':0, 'elbow':43, 'wrist':0, 'neck':95, 'phone':0, 'speed':0.004}
    robit.moveToPos(quietPos, pool)

pool = ThreadPool(5)


def linear(x): 
    return 2*x

def listeningMode(robit, pool, shouldContinue):
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
    finalPos = {'shoulder': 50, 'elbow':100, 'wrist':45, 'neck':70, 'phone':70, 'speed':0.077}
    
    currPos = standing;
    #robit.moveToPos(currPos, pool); 
    
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
    time.sleep(1.5)
    finalPos['phone'] = 90
    robit.moveToPos(finalPos, pool)
    time.sleep(0.5)
    
    if (shouldContinue): recognize(robit, pool)

def slowOsc(x):
    return (-0.5) * (math.cos(6 * x)) + 0.5

def recognize(robit, pool): 
    
    intitialMode = {'shoulder': 50, 'elbow':100, 'wrist':45, 'neck':96, 'phone':90, 'speed':0.006}
    #straightenNeck = {'shoulder': 50, 'elbow':100, 'wrist':45, 'neck':80, 'phone':90, 'speed':0.025} 
    #robit.moveToPos(straightenNeck, pool)
    initialModeCurves = {'shoulder':linear}
    initialModeEP= {'shoulder':0.5}

    shakeRight = {'shoulder': 50, 'elbow': 100, 'wrist': 45, 'neck': 60, 'phone': 95, 'speed':0.059}
    shakeLeft = {'shoulder': 50, 'elbow': 100, 'wrist': 45, 'neck': 106, 'phone': 85, 'speed':0.059}
    robit.moveToPos(shakeLeft, pool)
    robit.moveToPos(shakeRight, pool)
    robit.moveToPos(shakeLeft, pool)
    robit.moveToPos(shakeRight, pool)
    robit.moveToPos(shakeLeft, pool)
    robit.moveToPos(shakeRight, pool)
    shakeRight['phone'] = 90
    shakeRight['neck'] = 96
    robit.moveToPos(shakeRight, pool)
    happyBounce(robit, pool)
def shakeHead(robit, pool):
    pass

def happyBounceFromPos(robit, pool):
    initial = {'shoulder': shoulder.currentAngle, 'elbow': elbow.currentAngle, 'wrist': wrist.currentAngle, 'neck': neck.currentAngle, 'phone': phone.currentAngle, 'speed': 0.006}
    #robit.moveToPos(initial, pool)
    print("initialzied")
    
    initialMode = {'shoulder': 20, 'elbow': 60, 'wrist': 52, 'neck': 96, 'phone': 90, 'speed': 0.005}
    slightlyRaised = {'shoulder': 40, 'elbow': 60, 'wrist': 18, 'neck': 96, 'phone': 90, 'speed': 0.005}
    
    numSteps = 6 
     
    for i in range(numSteps):
        robit.moveToPos(slightlyRaised, pool)
        robit.moveToPos(initialMode, pool)
    
    robit.moveToPos(slightlyRaised, pool) 
    
def happyBounce(robit, pool):
    initial = {'shoulder': 40, 'elbow': 100, 'wrist': 70, 'neck': 96, 'phone': 90, 'speed': 0.006}
    robit.moveToPos(initial, pool)
    print("initialzied")
    
    initialMode = {'shoulder': 40, 'elbow': 100, 'wrist': 52, 'neck': 96, 'phone': 90, 'speed': 0.005}
    slightlyRaised = {'shoulder': 70, 'elbow': 100, 'wrist': 18, 'neck': 96, 'phone': 90, 'speed': 0.005}
    
    numSteps = 3 
     
    for i in range(numSteps):
        robit.moveToPos(slightlyRaised, pool)
        robit.moveToPos(initialMode, pool)
    
    robit.moveToPos(slightlyRaised, pool) 

    leanForward = {'shoulder': 70, 'elbow': 150, 'wrist': 60, 'neck': 96, 'phone': 90} 
    robit.moveToPos(leanForward, pool)
    
def checkWeather(robit, pool): 
  
    initial = {'shoulder': shoulder.currentAngle, 'elbow': elbow.currentAngle, 'wrist': wrist.currentAngle, 'neck': neck.currentAngle, 'phone': phone.currentAngle, 'speed': 0.004}
    checkWeatherPose = {'shoulder': 120, 'elbow': 180, 'wrist': 27, 'neck': 45, 'phone': 90, 'speed': 0.004}
    robit.moveToPos(checkWeatherPose, pool)
    time.sleep(1);
    checkWeatherPose2 = {'shoulder': 120, 'elbow': 180, 'wrist': 97, 'neck': 45, 'phone': 90, 'speed': 0.015} 
    robit.moveToPos(checkWeatherPose2, pool)
    
    time.sleep(0.5);  
    
    initial['speed'] = 0.006
    robit.moveToPos(initial, pool)

    initial['neck'] = 110;
    initial['speed'] = 0.012
    initialOSC = {'neck':vertOSC}
    robit.moveToPos(initial, pool, initialOSC)

    
def extendToUser(robot, pool): 
     initial = {'shoulder': shoulder.currentAngle, 'elbow': elbow.currentAngle, 'wrist': wrist.currentAngle, 'neck': neck.currentAngle, 'phone': phone.currentAngle, 'speed': 0.004}
     showToUser = {'shoulder': 120, 'elbow': 180, 'wrist': 0, 'neck': 80, 'phone': 0, 'speed': 0.002}
     showToUserFD = {'shoulder': linear}
     showToUserEP = {'shoulder': 0.5}
     robit.moveToPos(showToUser, pool, showToUserFD, showToUserEP)
     time.sleep(2)
     initial['phone'] = 90;
     
     robit.moveToPos(initial, pool)


def internetLookup(robit, pool):
    pass; 
    
    
    
    
    

def recognizeNew(robit, pool):
    finalPos = {'shoulder': 70, 'elbow':150, 'wrist':60, 'neck':96, 'phone':70, 'speed':0.077} 
    robit.moveToPos(finalPos, pool)
    time.sleep(1.5)
    finalPos['phone'] = 90
    robit.moveToPos(finalPos, pool)
    time.sleep(1.5)
    
    restingNeutral = {'shoulder': 40, 'elbow': 90, 'wrist': 45, 'neck': 96, 'phone': 90, 'speed':0.007}
    restingFD = {'wrist': oscilate}
    robit.moveToPos(restingNeutral, pool, restingFD)
    happyBounceFromPos(robit, pool) 

def noNoise(robit, pool):
    pos = {'shoulder': 0, 'elbow':90, 'wrist':0, 'neck':90, 'phone':0, 'speed':0.004}
    robit.moveToPos(pos, pool)

def onConnect(client, userdata, rc):
    print("absolutley connected")
    client.subscribe("emote")
    client.subscribe("motion", 2)

def onMessage(client, userdata, message):
    
    messageStr = str(message.payload.decode("utf-8"))
    print("message recieved: ", messageStr)
     
    if (messageStr == 'on'): connectPhone(pool) #Starts first chain
    if (messageStr == 'off'): off(robit, pool) #turns off
    if (messageStr == 'happy'): listeningMode(robit, pool, True) #fun listening
    if (messageStr == 'quiet'): quiet(robit, pool) #quiet
    if (messageStr == 'listen'): happyBounceFromPos(robit, pool) 
    if (messageStr == 'action'): recognizeNew(robit, pool) #recognize new person and recommend
    if (messageStr == 'weather'): checkWeather(robit, pool)
    if (messageStr == 'sad'): extendToUser(robit, pool) 

smoothInitializePosition(robit, pool)
#paho = pahoClient(onConnect, onMessage)

try:
    paho = pahoClient(onConnect, onMessage)
except KeyboardInterrupt:
    print("writing xml")
    robit.writePositions()
except Exception:
    print("writing xml")
    print("exception Thrown")
    robit.writePositions()
