import sqlite3
import global_module
from log_class import Log_Class
import os

databaseFile = './ServerDatabase.db'
sqlFile = './ServerDatabase.sql'
conn = None;
global_module.db_cursor =  None;
# connects to the logging database and makes on e if ot does not exist

def connect_database():
	if os.path.exists(databaseFile):
		print "Exists"
		# establish connection with the database and make one if it does not exist
		conn = sqlite3.connect(databaseFile)
		# making a Cursor Object for executing sqlite3 commands
		global_module.db_cursor = conn.cursor()
	else :
		print "Server Databse Created"
		sql = open(sqlFile,'r').read()
		sqlite3.complete_statement(sql);
		conn = sqlite3.connect(databaseFile)
		global_module.db_cursor = conn.cursor();
		global_module.db_cursor.executescript(sql);
	print type(global_module.db_cursor);

def createLog(sensorObj):
	sql_cmd = "UPDATE LOGGING SET SENSOR_CODE = '" + sensorObj.code + "', QUANTITY = '" + sensorObj.quantity + "', IS_LOGGING = 1 WHERE PIN_NO = '" + sensorObj.pin + "'"
	print type(global_module.db_cursor);
	global_module.db_cursor.execute(sql_cmd)
	global_module.logged.append(Log_Class(sensorObj))

def stopLog(logObj):
	sql_cmd = "UPDATE LOGGING SET IS_LOGGING = 0 WHERE PIN_NO = '" + logObj.pin + "'"
	global_module.db_cursor.execute(sql_cmd)
	logObj.stop()
