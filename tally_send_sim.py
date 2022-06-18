import socket, time, random
from time import sleep
import serial

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

Green_pins = [11,12,13]
Red_pins = [15,16,18]

for(pin in Green_pins):
    GPIO.setup(pin, GPIO.IN)
for(pin in Red_pins):
    GPIO.setup(pin, GPIO.IN)

SERVER_ADDRESS_PORT = ("0.0.0.0", 40001)

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
ser = serial.Serial('/dev/serial0', 38400, timeout=1)
ser.close()
ser.open()
sleep(1)

def hex_print(byte_seq):
    for b in byte_seq:
        print(hex(b), end=' ')
    print('')
    print("\n")
    

def get_message(cam, status):
    bmsg = [0x80 + cam]
    text = 'CAM ' + str(cam) +' '
    if status:
        text += 'ON '
    else:
        text += 'OFF'
    text += '       '
    
    # status = 0x32(green) or 0x31(red). 0x30(neither)
    if(status == "Green"):
        Status == 0x32
    elif(status == "Red"):
        Status = 0x31
    else:
        Status = 0x30
#     Status = 0x32 if status else 0x30
    bmsg.append(Status)
    # bmsg.extend([0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63])
    for t in text:
        bmsg.append(int.from_bytes(t.encode(), byteorder='big'))
    return bmsg

def send_message(seq):
    # Send to server using created UDP socket
    print("Hex Print:     ")
    hex_print(seq)
    UDPClientSocket.sendto(seq, SERVER_ADDRESS_PORT)
    
#     print("about to send")
    ser.write(seq)
#     ser.write(bytes(seq, 'utf-8'))
#     print("sending")
#     ser.close()

last = 0
for i in range(3):
    msg = get_message(i+1, "Off")
    send_message(bytearray(msg))
#     sleep(4)
while True:

#     now = random.randrange(5) + 1
#     while now == last:
#         now = random.randrange(5) + 1
#     print('Change:', now)
    for(pin in Green_pins):
        if(GPIO.input(pin) == 1):
            on = get_message(now,"Green")
            sleep(0.1)
            off = get_message(Green_last, "Off")
            Green_last = pin
        #     hex_print(on)
            send_message(bytearray(on))
            send_message(bytearray(off))
            
    for(pin in Red_pins):
        if(GPIO.input(pin) == 1):
            on = get_message(now, "Red")
            sleep(0.1)
            off = get_message(Green_last, "Off")
            Green_last = pin
        #     hex_print(on)
            send_message(bytearray(on))
            send_message(bytearray(off))
    #     wipe = random.randrange(9)
    #     time.sleep(2)
    #     if wipe == 7:
    #         m = random.randrange(6) + 1
    #         print('wipe:', m)
    #         time.sleep(m)
    #     hex_print(off)
        
        
    #     print()
    #     time.sleep(3)
