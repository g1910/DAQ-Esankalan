import Adafruit_BBIO.ADC as ADC
import sys
import json
import global_module
import datetime
import threading
from time import sleep

class Adc() :
	def __init__(self,jsonObj):
		print type(self)
		json_string = json.dumps(jsonObj)
		decoded = json.loads(json_string)
		self.rate =  decoded["rate"];
		self.protocol = decoded["protocol"]
		self.pin = decoded["pin"];
		self.code = decoded["sensor_code"]
		self.quantity = decoded["quantity"]
		self.isLogging = decoded["isLogging"]
		self.log_file = open('./logs/' + self.code + "_" + self.quantity + ".txt", 'a')
		self.stop = threading.Event()
		self.sensor_thread = threading.Thread(target = self.task)
		self.sensor_thread.start()
		
		
	def task(self):
		ADC.setup()
		while not self.stop.isSet():
							        
			value = ADC.read_raw(self.pin) 
			now = datetime.datetime.now()
			print  self.protocol + "%f : %d : %d : %d "%(value,now.minute,now.second,now.microsecond)
			val = str(value) + " : " + str(now.minute) + " : " + str(now.second) + " : " + str(now.microsecond)+"\n"
			global_module.wifi_namespace_reference.on_send(val);
			if self.isLogging:
				self.log_file.write(val)
			sleep(1);
		 
	def stopRead(self):
		self.log_file.close();
		self.stop.set();
		if self.sensor_thread.isAlive():
			self.sensor_thread.join();

