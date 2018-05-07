#################################################
# testing paho mqtt client
#################################################
import time#maybe this is useful?
from datetime import datetime#but not essential for my part
import threading#idk, you do what you gotta do for threading

import paho.mqtt.client as mqtt 


class pahoClient(object): 

    def __init__(self):
        self.BROKER = 'broker.shiftr.io'
        self.USERNAME = 'emotingWOZ' 
        self.PASSWORD = 'lucasMarisaGautam'
        self.client = mqtt.Client("physical") #create new instance
        self.client.username_pw_set(self.USERNAME, self.PASSWORD)
        self.client.connect(self.BROKER,1883, 60)
        self.client.on_connect = onConnect
        self.client.on_message = onMessage
        self.client.loop_forever() 


def onConnect(client, userdata, rc):
    print("Connected with result code ")
    client.subscribe("emote")
    client.subscribe("motion",2)
    
def onMessage(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    
#def initialize(self):
        #if self.thread is None:
            # start background servo thread
            #now = datetime.now()
            #ts  = now.strftime("%B%d_%H%M")
            #Servo.thread = threading.Thread(target=self._thread)
            #Servo.thread.start()

wef = pahoClient()

