from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN)

while(1):
    print(GPIO.input(12))
    sleep(0.01)