
import sqlite3

# SQLite DB Name
DB_Name =  "aalto_building.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists Users_Data ;
create table Users_Data (
  id integer primary key autoincrement,
  roomid text,
  timestamp text,
  count text
);
"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()
