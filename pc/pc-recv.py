# -*- coding: utf-8 -*- 

comPort = "com29"   #PC的TTL2USB port
baudRate = 9600

import serial
import pyautogui
import sys
import time
import playsound
import random


serial = serial.Serial(comPort, baudRate)

i = 0
nowtime = 0
lastClicktime = 0


while True:
	
	nowtime = int(round(time.time() * 1000)) 
	out = ''
	
	while(serial.inWaiting()):
		out += str(serial.read(1).decode('UTF-8'))
	
	if out != '':
		print(out)
		if(out=="D"):
			pyautogui.typewrite(["right", "ctrlright"]) 
			
		if(out=="U"):
			pyautogui.typewrite(["left", "ctrlleft"])
			
		if(out=="N"):
			file = "notice" + str(random.randrange(1, 6)) + ".wav"
			playsound.playsound(file, True)

		serial.flushInput()