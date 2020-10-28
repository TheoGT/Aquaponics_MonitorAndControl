import serial
from datetime import datetime

port = "/dev/cu.wchusbserial1410"   #port name, probably COM4 on window
f1 = open('ping1.txt', 'w')
f2 = open('ping2.txt', 'w')

ard = serial.Serial(port, 115200)     #9600 open on arduio
count = 0

print("Recording...")
while (count < 100):
    byte = ard.readline()           #reads byte code ending in line-terminator
    msg = byte.decode("utf-8")      #Convert to string
    time = datetime.now()
    msgList = msg.split()

    for dataPoints in msgList:
        dataSplit = dataPoints.split(":")
        if dataSplit[0] == "Ping1":
            f1.write(str(time) + "|" + dataSplit[1] + "\n")
        else:
            f2.write(str(time) + "|" + dataSplit[1] + "\n")
            
    count+=1   

    
print("Done Recording")
ard.close()
f1.close()
f2.close()

