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
switchClick = False  #是否切換為scroll的方式

while True:
	
	nowtime = int(round(time.time() * 1000)) 
	out = ''
	
	while(serial.inWaiting()):
		out += str(serial.read(1).decode('UTF-8'))
	
	
	if out != '':
		print(out)
		
		if(out=="D"):

			if(switchClick==False):
				pyautogui.typewrite(["right", "ctrlright"]) 
			else:
				pyautogui.scroll(250)
			
		if(out=="U"):

			if(switchClick==False):
				pyautogui.typewrite(["left", "ctrlleft"])
			else:
				pyautogui.scroll(-250)
			
		if(out=="N"):
			
			if(switchClick==True):
				file = "click.wav"
				playsound.playsound(file, True)
				switchClick = False
			else:
				file = "scroll.wav"
				playsound.playsound(file, True)			
				switchClick = True

		serial.flushInput()