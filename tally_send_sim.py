import socket, time, random
from time import sleep
import serial

import RPi.GPIO as GPIO

# GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)


Green_pins = [11,12,13]
Red_pins = [15,16,18]
Green_last = -1
Red_last = -1

for pin in Green_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for pin in Red_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
        Status = 0x32
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
#     print("Hex Print:     ")
#     hex_print(seq)
    UDPClientSocket.sendto(seq, SERVER_ADDRESS_PORT)
    
#     print("about to send")
    ser.write(seq)
#     ser.write(bytes(seq, 'utf-8'))
#     print("sending")
#     ser.close()

last = 0
for i in range(3):
    msg = get_message(i, "Off")
    sleep(0.1)
    send_message(bytearray(msg))
    sleep(0.1)
print("done setting up")
#     msg = get_message(i+1, "Off")
#     send_message(bytearray(msg))
#     sleep(4)
#     now = random.randrange(5) + 1
#     while now == last:
#         now = random.randrange(5) + 1
#     print('Change:', now)
while True:
#     print("start")
    for pin in Green_pins:
        if(GPIO.input(pin) == 1):
#             print(pin, ": On")
            if(Green_pins.index(pin) != Green_last):
                on = get_message(Green_pins.index(pin), "Green")
                print("turning pin ", pin, " on")
                send_message(bytearray(on))
                sleep(0.1)
                if(Green_last != -1):
                    off = get_message(Green_last, "Off")
                    send_message(bytearray(off))
                    print("turning pin ", Green_last, on)
                Green_last = Green_pins.index(pin)
            sleep(0.1)
        #     hex_print(on)
#             send_message(bytearray(on))
#             send_message(bytearray(off))
#         else:
#             print(pin, ": Off")
    for pin in Red_pins:
        if(GPIO.input(pin) == 1):
#             print(pin, ": On")
            if(Red_pins.index(pin) != Red_last):
                on = get_message(Red_pins.index(pin), "Red")
                print("turning pin ", pin, " on")
                send_message(bytearray(on))
                sleep(0.1)
                if(Red_last != -1):
                    off = get_message(Red_last, "Off")
                    send_message(bytearray(off))
                    print("turning pin ", Red_last, " off")
                Red_last = Red_pins.index(pin)
            sleep(0.1)
#         else:
#             print(pin, ": Off")
        #     hex_print(on)
#             send_message(bytearray(on))
#             send_message(bytearray(off))
    #     wipe = random.randrange(9)
    #     time.sleep(2)
    #     if wipe == 7:
    #         m = random.randrange(6) + 1
    #         print('wipe:', m)
    #         time.sleep(m)
    #     hex_print(off)
        
        
    #     print()
    #     time.sleep(3)

