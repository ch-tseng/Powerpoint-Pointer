# -*- coding: utf-8 -*- 

comPort = "com4"   #PC的TTL2USB port
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
switchClick = True  #是否切換為scroll的方式
scrollSpeed = 0
scrollValue = 100

while True:
	
	nowtime = int(round(time.time() * 1000)) 
	out = ''
	
	while(serial.inWaiting()):
		out += str(serial.read(1).decode('UTF-8'))
		'''
		strA = serial.read(1)
		print(strA)
		out += str(strA.decode('UTF-8'))
		'''
	if out != '':
		print(out)
		
		if(scrollSpeed==0):
			scrollValue = 100
		elif(scrollSpeed==1):
			scrollValue = 800
		elif(scrollSpeed==2):
			scrollValue = 800
		elif(scrollSpeed==3):
			scrollValue = 1500
		elif(scrollSpeed==4):
			scrollValue = 3000
			
		if(out=="D"):

			if(switchClick==False):
				pyautogui.typewrite(["right", "ctrlright"]) 
			else:
				pyautogui.scroll(scrollValue)
			
		if(out=="U"):

			if(switchClick==False):
				pyautogui.typewrite(["left", "ctrlleft"])
			else:
				pyautogui.scroll(-scrollValue)
			
		if(out=="N"):
			
			scrollSpeed += 1
			if(scrollSpeed>1): scrollSpeed=0
			
			'''
			if(switchClick==True):
				file = "click.wav"
				playsound.playsound(file, True)
				switchClick = False
			else:
				file = "scroll.wav"
				playsound.playsound(file, True)			
				switchClick = True
			'''
			file = "mouse_" + str(scrollSpeed) + ".wav"
			#laysound.playsound(file, True)			
			#switchClick = True
			
		serial.flushInput()
