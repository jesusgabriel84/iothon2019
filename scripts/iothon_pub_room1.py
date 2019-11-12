import paho.mqtt.client as mqtt
import pandas as pd
import json
import time


#====================================================
# MQTT Settings 
MQTT_Broker = "195.148.126.70"
MQTT_Port = 1883
Keep_Alive_Interval = 45
ROOM_ID = 1
MQTT_Topic = "/TUAS/"+str(ROOM_ID)+"/people"

#====================================================

def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print "Unable to connect to MQTT Broker..."
	else:
		print "Connected with MQTT Broker: " + str(MQTT_Broker)

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass

#==============================
# Sensor settings		
mqttc = mqtt.Client("R1")
mqttc.on_connect = on_connect
mqttc.username_pw_set("mqttuser",password="mqttpassword")
#mqttc.tls_set("/home/gabriel/Documents/ex2/certs/client.crt",None,None,cert_reqs=ssl.CERT_NONE,tls_version=ssl.PROTOCOL_TLSv1,ciphers=None)
#mqttc.tls_insecure_set(True)
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		
#==============================
		
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print ""


#====================================================
# Sensor publishing 
# Reading values from csv file and publish to the MQTT broker

df = pd.read_csv("iothon_sensor_data.csv")
f = df.loc[df['roomid'] == ROOM_ID]

def publish_Sensor_Values_to_Mosquitto():
	
	for index,row in f.iterrows():
		time.sleep(30)		
		People_Data = {}
		People_Data['roomid'] = str(row['roomid'])
		People_Data['timestamp'] = str(row['timestamp'])
		People_Data['count'] = str(row['count'])
		people_json_data = json.dumps(People_Data)
		print "Publishing people data: " + str(row['count']) + "..."
		publish_To_Topic (MQTT_Topic, people_json_data)
		
publish_Sensor_Values_to_Mosquitto()

#====================================================
