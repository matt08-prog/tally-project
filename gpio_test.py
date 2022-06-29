from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.setup(22, GPIO.OUT)
sleep(1)
# while(1):
GPIO.output(11, 0)
GPIO.output(12, 0)
GPIO.output(13, 0)
GPIO.output(15, 0)
GPIO.output(16, 0)
GPIO.output(18, 0)
GPIO.output(23, 0)
#     
GPIO.output(22, 1)
sleep(0.01)
# GPIO.cleanup()
