#################################################
# testing paho mqtt client
#################################################
import time#maybe this is useful?
from datetime import datetime#but not essential for my part
import threading#idk, you do what you gotta do for threading

import paho.mqtt.client as mqtt 


class pahoClient(object): 

    def __init__(self, onConnect, onMessage):
        self.BROKER = 'broker.shiftr.io'
        self.USERNAME = 'emotingWOZ' 
        self.PASSWORD = 'lucasMarisaGautam'
        self.client = mqtt.Client("physical") #create new instance
        self.client.username_pw_set(self.USERNAME, self.PASSWORD)
        self.client.connect(self.BROKER,1883, 60)
        self.client.on_connect = onConnect
        self.client.on_message = onMessage
        self.client.loop_forever()
    def manualLoop(self):
        self.client.loop()
    def loopStart(self):
        self.client.loop_forever()
        
