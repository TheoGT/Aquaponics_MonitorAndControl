import serial
import pandas as pd
from datetime import datetime

port = "COM3"   #port name, probably COM4 on window
f = open('numPress.txt', 'w');

ard = serial.Serial(port, 115200)     #9600 open on arduio
count = 0

while count<100:
    byte = ard.readline()           #reads byte code ending in line-terminator
    msg = byte.decode("utf-8")      #Convert to string
    time = datetime.now()
    f.write(str(time) + ": Sensor recorded " + str(msg) + '\n')
    count+=1
    print(msg)
    
ard.close()
f.close()
