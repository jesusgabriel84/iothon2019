import json
import sqlite3

# SQLite DB Name
DB_Name =  "aalto_building.db"

#===================================================================
# Database Manager Class

class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_Name)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#===================================================================
# Function to save people count from the sensor data to the DB Table
def Sensor_People_Data_Handler(roomid,timestamp,count):

	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into Users_Data (roomid, timestamp, count) values (?,?,?)",[roomid, timestamp, count])
	del dbObj
	print "["+str(timestamp)+"]: "+"Register inserted into Database."
	print ""
