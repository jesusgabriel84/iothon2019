
import paho.mqtt.client as mqtt
from iothon_save_to_db import Sensor_People_Data_Handler
from functions_final import checkroom
import ssl, datetime

#=================================================================
# MQTT Settings 
MQTT_Broker = "195.148.126.70" #IP of our VM in the Core Network
MQTT_Port = 1883
Keep_Alive_Interval = 45
SUBSCRIBER_ID = "S1"
MQTT_Topic = "/TUAS/#" #Subscribe to all Sensors at Base Topic
#MQTT credentials
MQTT_USER = "mqttuser"
MQTT_PASSWORD = "mqttpassword"
#=================================================================

#Save Data into DB Table
def on_message(mosq, obj, msg):
	
	#Printing the MQTT messages as they are received by the sensors in real time
	print ""
	print "======================="
	print "MQTT Data Received..."
	print "MQTT Topic: " + msg.topic  
	print "People count: " + msg.payload #This is the count of people in the room
	print "======================="
		
	#Extract room ID from the message topic string, the MQTT topic sent by the sensors has the
	#form: "/TUAS/1/people", in this case the room number is '1'
	room_id = int(str(msg.topic).split('/')[2])
	current_time = str(datetime.datetime.now())
	
	#Call this function to save the information into the database, save the timestamp,
	#the room ID and the count of people in that room
	Sensor_People_Data_Handler(room_id, current_time, int(msg.payload))

	#Call this function to notify users about room status and command the building to
	#power off one room if it is not used, i.e. the count of people is 0
	checkroom(room_id,int(msg.payload))
	

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

#=======================================================
#Subscribe to MQTT broker in the VM, the variable mqttc
#is the mqtt client variable that contains all the methods
#to handle the mqtt protocol
mqttc = mqtt.Client(SUBSCRIBER_ID)
mqttc.username_pw_set(MQTT_USER,password=MQTT_PASSWORD)
#========================================================

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe

# Connect to the broker
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
mqttc.subscribe(MQTT_Topic, 0) #Subscribing with QoS = 0, it supports 3 levels of QoS

# Continue the network loop
mqttc.loop_forever()
