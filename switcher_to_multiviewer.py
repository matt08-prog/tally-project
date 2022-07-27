import time
from time import sleep
import serial
import RPi.GPIO as GPIO

# set the RS485 CAN HAT to Enabled
EN_485 = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)

Green_pins = [11,12,13]
Red_pins = [15,16,18]
Green_last = -1
Red_last = -1

# setup the three standby pins and the three active pins
for pin in Green_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for pin in Red_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
# setup the RS485 communication to the multiviewer
ser = serial.Serial('/dev/ttyAMA0',
                    38400,
                    timeout=1,
                    parity=serial.PARITY_EVEN,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )

ser.close()
ser.open()
sleep(1)

def get_message(cam, status):
    bmsg = [0x80 + cam]
    text = 'CAM ' + str(cam) +' '
    if status:
        text += 'ON '
    else:
        text += 'OFF'
    text += '       '
    
    # status = 0x32(green), 0x31(red), or 0x30(neither)
    if(status == "Green"):
        Status = 0x32
    elif(status == "Red"):
        Status = 0x31
    else:
        Status = 0x30
        
    bmsg.append(Status)
    for t in text:
        bmsg.append(int.from_bytes(t.encode(), byteorder='big'))
    return bmsg

def send_message(seq):
    ser.write(seq)

# start program by turning off all tally lights
last = 0
for i in range(3):
    msg = get_message(i, "Off")
    sleep(0.1)
    send_message(bytearray(msg))
    sleep(0.1)

# loop through each pin and see if there are any changes that need to be sent
# to the multiviewer to be updated.
while True:
    for pin in Green_pins:
        if(GPIO.input(pin) == 1):
            if(Green_pins.index(pin) != Green_last):
                on = get_message(Green_pins.index(pin), "Green")
                send_message(bytearray(on))
                sleep(0.1)
                if(Green_last != -1):
                    off = get_message(Green_last, "Off")
                    send_message(bytearray(off))
                Green_last = Green_pins.index(pin)
            sleep(0.1)

    for pin in Red_pins:
        if(GPIO.input(pin) == 1):
            if(Red_pins.index(pin) != Red_last):
                on = get_message(Red_pins.index(pin), "Red")
                send_message(bytearray(on))
                sleep(0.1)
                if(Red_last != -1):
                    off = get_message(Red_last, "Off")
                    send_message(bytearray(off))
                Red_last = Red_pins.index(pin)
            sleep(0.1)