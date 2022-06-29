from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


Green_pins = [11,12,13]
Red_pins = [15,16,18]
Green_last = -1
Red_last = -1
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, 0)
sleep(1)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)

GPIO.setup(22, GPIO.IN)
# 
# for pin in Green_pins:
#     GPIO.setup(pin, GPIO.IN)
# for pin in Red_pins:
#     GPIO.setup(pin, GPIO.IN)
sleep(1)
while True:
    print(GPIO.input(22))
#     for pin in Green_pins:
#         if(GPIO.input(pin) == 1):
#             print(pin, ": On")
#         else:
#             print(pin, ": Off")
# 
# 
#     for pin in Red_pins:
#         if(GPIO.input(pin) == 1):
#             print(pin, ": On")
#         else:
#             print(pin + ": Off")
