#################################################
# testing paho mqtt client
#################################################
import time#maybe this is useful?
from datetime import datetime#but not essential for my part
import threading#idk, you do what you gotta do for threading

import paho.mqtt.client as mqtt 

BROKER = 'broker.shiftr.io'
USERNAME = 'emotingWOZ' 
PASSWORD = 'lucasMarisaGautam'

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

client = mqtt.Client("physical") #create new instance
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER,1883, 60)
client.on_connect = onConnect
client.on_message = onMessage
#client.loop_start() 
client.loop_forever()

