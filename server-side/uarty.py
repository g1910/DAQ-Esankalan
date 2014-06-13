import Adafruit_BBIO.UART as UART
import serial
import sys
import json
import global_module
import datetime
import threading
import time

class Uart() :
	number = 0;
	def __init__(self,jsonObj):
		json_string = json.dumps(jsonObj)
		decoded = json.loads(json_string)
		self.rate =  decoded["rate"];
		self.protocol = decoded["protocol1"];
		#self.baudrate = decoded["baudrate"]
		self.byte1 = "8"#decoded["byte1"]
		self.command = "31"
		self.pin = "UART1";
		self.numb = Uart.number;
		Uart.number = Uart.number + 1;
		self.arr = [];
		UART.setup(self.pin)
		self.out=''
		self.serial_port = serial.Serial(port = "/dev/ttyO1", baudrate = int("9600",10))
		#self.serial_port.close()
		self.serial_port.open()
		self.stop = threading.Event()
		self.sensor_thread = threading.Thread(target = self.task)
		self.sensor_thread.start()
		
		
#txt = sys.argv[1]
#things needed for uart

	def task(self):
		while not self.stop.isSet():
		#for i in range(1,100):
			self.serial_port.write('1') #''.join([chr(int(''.join(c), 16)) for c in zip(self.command[0::2],self.command[1::2])]))
			self.out = self.serial_port.read(8)
			now = datetime.datetime.now()
			print self.out + " : " + self.protocol + str(self.numb) + " : %d : %d : %d \n" %(now.minute,now.second,now.microsecond)
			time.sleep(0.25);
		 

	def stopRead(self):
		self.stop.set();
		if self.sensor_thread.isAlive():
			self.sensor_thread.join();
#hex - acscii - string
