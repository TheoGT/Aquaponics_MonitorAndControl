import serial
from datetime import datetime

port = "/dev/cu.usbmodem1411"   #port name, probably COM4 on window
f = open('numPress.txt', 'w');

ard = serial.Serial('COM3', 115200)     #9600 open on arduio
count = 0

while True:
    byte = ard.readline()           #reads byte code ending in line-terminator
    msg = byte.decode("utf-8")      #Convert to string
    time = datetime.now()
    f.write('Sensor recorded ' + time)
    #count+=1

"""
    if(count == 10):
        ard.close()                 #Reset string to close port
        f.write('The number of count is ' + str(count) + '\n')
        break
"""
