from time import sleep
import serial

# ser = serial.Serial('/dev/ttyAMA0', 9600, write_timeout=1,timeout=0)
ser = serial.Serial('/dev/serial0', 9600, timeout=1)
ser.close()
# sleep(4)
ser.open()

# ser.write(00000000)
# while(1):
print("about to send")
ser.write(bytes("The", 'utf-8'))
print("sending")
ser.close()
# try:
#     while (1):
#         response = ser.readline()
#         print(response)
# except KeyboardInterrupt:
#     ser.close()

# def serial_ports():
#     """ Lists serial port names
# 
#         :raises EnvironmentError:
#             On unsupported or unknown platforms
#         :returns:
#             A list of the serial ports available on the system
#     """
#     if sys.platform.startswith('win'):
#         ports = ['COM%s' % (i + 1) for i in range(256)]
#     elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
#         # this excludes your current terminal "/dev/tty"
#         ports = glob.glob('/dev/ttyUSB*') # ubuntu is /dev/ttyUSB0
#     elif sys.platform.startswith('darwin'):
#         # ports = glob.glob('/dev/tty.*')
#         ports = glob.glob('/dev/tty.SLAB_USBtoUART*')
#     else:
#         raise EnvironmentError('Unsupported platform')
# 
#     result = []
#     for port in ports:
#         try:
#             s = serial.Serial(port)
#             s.close()
#             result.append(port)
#         except serial.SerialException as e:
#             if e.errno == 13:
#                 raise e
#             pass
#         except OSError:
#             pass
#     return result


# if __name__ == '__main__':
#     print(serial_ports()) 