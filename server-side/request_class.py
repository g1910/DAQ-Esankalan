import json

from uarty import Uart
from adc import Adc
from i2c1 import I2c

class Request_Class:

	def __init__(self,jsonReq):
		json_string  = json.dumps(jsonReq)
		decoded = json.loads(json_string)
		self.protocol = decoded["protocol"]
		self.json = jsonReq;
		self.quantity = decoded["quantity"]
		self.code = decoded["sensor_code"]
		self.isLogging = decoded["isLogging"]
		self.pin = decoded["pin"]
		self.read_sensor();
	
	def read_sensor(self):
		if self.protocol == "adc":
			self.obj = Adc(self.json);
		elif self.protocol == "uart":
			self.obj = Uart(self.json);
		elif self.protocol == "i2c":
			self.obj = I2c(self.json);
	
	def stop(self):
		self.obj.stopRead();

