# -*- coding:utf-8 -*-
import time, random
from time import sleep
import RPi.GPIO as GPIO
import serial

EN_485 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)

# t = serial.Serial("/dev/ttyS0",115200)
t = serial.Serial("/dev/ttyS0",115200)

# t = serial.Serial(
#     port='/dev/serial0',
#     baudrate=9600,
# #     parity=serial.PARITY_NONE,
# #     stopbits=serial.STOPBITS_ONE,
# #     bytesize=serial.EIGHTBITS
# #     timeout=1
# )

print (t.portstr)    
strInput = input('enter some words:')    
n = t.write(strInput.encode())    
print (n)    
str = t.read(n)    
print (str)   
