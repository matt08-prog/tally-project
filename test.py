import time
from time import sleep
import serial
import RPi.GPIO as GPIO

# set the RS485 CAN HAt to Enabled
EN_485 = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)


# ser = serial.Serial('/dev/ttyS0', 38400, timeout=0)
# ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)
# ser = serial.Serial('/dev/ttyS0', 74880, timeout=1)

# setup the RS485 communication to the multiviewer
# ttyAMA0
ser = serial.Serial('/dev/ttyAMA0',
                    38400,
                    timeout=1,
                    parity=serial.PARITY_EVEN,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
# ser = serial.Serial('/dev/ttyS0',
#                     38400,
#                     timeout=1,
#                     parity=serial.PARITY_EVEN,
#                     stopbits=serial.STOPBITS_ONE,
#                     bytesize=serial.EIGHTBITS
#                     )

# ser.parity = "E"
ser.close()
ser.open()
sleep(1)



bmsg = [0x80]
ser.write(int.from_bytes("g".encode(), byteorder='big'))