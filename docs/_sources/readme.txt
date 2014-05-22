Project Proposal
****************

This document covers the various the aspects proposed for developing a Low Cost Modular Data Acquisition(DAQ) System. For more, http://en.wikipedia.org/wiki/Data_acquisition

Introduction
============

Problem Statement
-----------------

Despite the widespread use of Data Acquisition in the labs and industries, it is quite difficult to find a DAQ system which is cost effective and at the same time, provides a highly configurable environment.

Solution
--------

To develop a low cost Data Acquisition System (DAQ) which is configurable and user friendly that operates by plugging in sensor modules and displaying the data on the Aakash Tablet.

Motivation
==========

Problem Description
-------------------

	*	Engineers and scientists use data acquisition (DAQ) products for validating and verifying a design prototype, teaching in a university lab, diagnosing a machine malfunction, or controlling a manufacturing process etc.

	*	But the products available are quite expensive and use proprietary softwares which further add to the cost. Also, those products that are cost effective do not provide a high amount of user customization.

Existing DAQ Systems
--------------------
NI Wi-Fi DAQ
+++++++++++++++
The latest Data Acquisition System from National Instruments offers connectivity over wireless and cabled Ethernet. Its major features include:
	*	It supports for over 50 measurement modules.
	*	It has 802.11 wi-fi connectivity
	*	The device includes built-in signal conditioning
	*	It has direct sensor connectivity for electrical, physical, mechanical, and acoustic signals.  
	*	The NI-DAQmx driver delivers features such as the configuration-based NI DAQ Assistant with code generation for both LabView and text-based languages, it offers more than 3000 measurement examples and supports device simulation, and it is compatible with LabView, ANSI C/C++, C#, Visual Basic .NET, and Visual Basic 6.0.
 
But it also has major limitations like:
	*	It is complemented by the software LabVIEW 8.6 that costs around 60,000 Rs.
	*	The cost of NI Wi-Fi DAQ system is around 40,000 Rs.
 
BracheStudios – USB Data Acquisition using BeagleBone
+++++++++++++++++++++++++++++++++++++++++++++++++++++

The arm system of the BeagleBone is used as a standalone data acquisition device which has the following features:
	*	The BeagleBone (or other ARM based system) would act as the server for collecting measurements from a USB device attached to it.
	*	It uses node.js for the server backbone which is very flexible.
	*	BeagleBone would host a web page and provide javascript graphs of temperature, voltage, digital IO, etc. of an acquisition with an attached USB device which can be later downloaded or sent through email.
	*	The USB-DAQ Board is a Measurement Computing USB-2408 board which has more number of pins than present on the BeagleBone
But it has the following limitations:
	*	More hardware (like the USB-DAQ board) are needed which increase the overall cost of the system.
	*	It does not fully utilize the BeagleBone.
	*	Limited customization is possible with this system.

Possible Improvements
---------------------

	*	Cost can be reduced effectively by providing an open source software instead of using proprietary softwares like LabView and reducing the hardware used.
	*	The device can be made compatible with a wider range of existing sensors as well as the sensors that may be available in the future.
	*	User customization can be increased by allowing the user to perform various calculations and manipulations on the data received from the sensors.
	*	An application can be developed to work on any Android based device making the facility available to students all over the country.	

Project Details
===============

	.. figure::  images/block.jpg
   		:align:   center

   		Block Diagram


**Data acquisition** is the process of sampling signals that measure real world physical conditions and converting the resulting samples into digital numeric values that can be manipulated by a computer. Data acquisition systems typically convert analog waveforms into digital values for processing. The components of data acquisition systems include:
	*	Sensors that convert physical parameters to electrical signals.
	*	Signal conditioning circuitry to convert sensor signals into a form that can be converted to digital values.
	*	Analog-to-digital converters, which convert conditioned sensor signals to digital values.

Sensors
-------

A Sensor is a device that converts a physical parameter (for example:  temperature, blood pressure, humidity, speed, etc.) into a corresponding electrical signal. To measure a physical quantity these sensors give outputs in various forms like  voltage,current,resistance,capacitance,etc.
**Signal Conditioning** is required when data acquired by sensors is not suitable with the DAQ hardware.In most of the cases the signal may be fitered or amplified.
The sensors may work on several communication protocols such as UART,SPI,I2C to give a measurement of the required physical parameters.The data from the sensors after conditioning in sent to the microcontroller in the Beaglebone black which acts as the Data Acquisition Hardware.

Beagleboard as DAQ hardware
---------------------------

The Beaglebone Black hardware contains several pins to which a sensor can be interfaced :
	*	65 digital GPIOs
	*	7 analog inputs
	*	Serial UARTs
	*	2 SPI ports
	*	2 I2C ports
	*	8 PWM and 4 Timers

BeagleBone Black as a Server
----------------------------

	*	The beaglebone black will act as a microcontroller as well as a server for broadcasting the acquired data. 
	*	For this purpose, bonescript.js, a node.js library will be used for scripting purposes. It is specially optimized for Beagle family and has many in-built functions that interact with the haradware which make the whole scripting process easy, comfortable and efficient. 
	*	The BoneScript Library runs in Node.JS. It can be directly run on the board using the 'node' interpreter or the Cloud9 IDE that invokes the 'node' interpreter or by using the bonescript.js script within browser via remote procedure calls using Socket.io and served up by the web server running on your Beagle. 
	*	Access to the library functions is provided through the "require('bonescript')" function call. The call returns an object containing all of the functions and constants exported by the library. 
	*	Apart from this, the BeagleBone server will also act as a database for the sensors previously used on the board which will have the all the information related to a sensor – model name, protocol used, formula used for processing data etc.


Android Application
-------------------

	*	The main motivation of the project is that the user need not worry too much details of scripting the beaglebone and here the android application plays a major role. 
	*	The application will allow a user to enter parameters like pins to be read from the beagle board and the formula to be used for processing the data. 
	*	For enabling multiple user access, the configurations file database will also be built which can make further use of the sensors easy and hassle-free. 
	*	These configurations will be stored locally on the device as well as sent on the beagle server for easy access to other users. 
	*	As and when the pins to be read from the board are selected, a request will be sent to the server and the corresponding response will be manipulated by the configuration either entered by the user or fetched from the configurations database.


Communication Channels
----------------------

	*	Sensors will be attached to the corresponding pins of the board as per the communication protocols it follows. 
	*	The data from the pins is read directly using inbuilt bonescript functions [analogRead() ] and is made available to the server constructed on node.js. 
	*	This data is then relayed to the tablet(client) via wifi router using socket.io  on the server side and Gottox java-client libraries on the client side.


Workflow
--------

.. figure::  images/workflow.jpg
   		:align:   center

   		Workflow of the application

Issues and Challenges
=====================

	*	The Beagle Bone black has a limited number of pins , thus limiting the number / type of sensors that can be attached. An additional USB peripheral board will have to be connected to the board and configured accordingly.
	*	The protocols for communication between the sensors and server are limited on the BeagleBone Black. Other protocols that may come in the future or that are unsupported by the Beagle version are not addressed by our system.
	*	Though a USB cable will be the most efficient / foolproof channel to transfer data from the board to the tablet, there are limitations on the client side in that there is limited support for android platform.
	*	Using a wifi dongle will put geographical constraints on the functioning of the DAQ system. 

Extension of the current tools/systems
======================================

We are modifying the current DAQ systems built on BeagleBone Black board by integrating Data aquisition , control and server side work on a single board  i.e. the BeagleBone black. 

What makes the project unique ?
===============================

System is unique because :
	*	Customizable: The application will be as user friendly as we can make it and user interactive. Several editable parameters will be in the hands of the user. 
	*	Cost-effective: Such a custamizable DAQ application rarely comes at an affordable price. Our system however optimises at every level of development to produce an inexpensive yet robust solution.

Deliverables
============

	*	A standalone android application that can be installed on any tablet or mobile device running on Android (preferably version 2.2 or higher).
	*	Set of scripts written in bonescript.js which will enable the beagle bone server to interact with the android application.

Conclusion
==========

The total estimated cost for the whole system comes out to be:
	*	Under 10,000 Rs.- if Aakash tablet is needed
	*	Under 6000 Rs.- if the user already has the Aakash tablet

The system that we plan to build will be compatible with a wide range of existing sensors as well as the sensors that may be available in the future.
The user will be able to perform any number of calculations and manipulations on the data.

Thus in conclusion, we plan to build an efficient Data Acquisition system and supporting Android app that is cost efficient and highly customizable thus giving the user the best working experience possible.

References
==========

	*	http://beagleboard.org/Support/BoneScript
	*	http://en.wikipedia.org/wiki/Data_acquisition
	*	http://www.edn.com/electronics-products/electronic-product-reviews/other/4378779/NI-debuts-WiFi-DAQ-systems
	*	http://www.ni.com/white-paper/3536/en/
	*	http://brachestudios.com/beaglebone-with-usb-data-acquisition-hardware/
	*	http://beagleboard.org/static/beaglebone/a3/Docs/Hardware/BONE_SRM.pdf
	*	http://elinux.org/Beagleboard:Cape_Expansion_Headers


