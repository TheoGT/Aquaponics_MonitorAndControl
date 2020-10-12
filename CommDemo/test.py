import serial

port = "/dev/cu.wchusbserial1410"   #port name, probably COM4 on window

ard = serial.Serial(port, 9600)     #9600 open on arduio

while True:
    byte = ard.readline()           #reads byte code ending in line-terminator
    msg = byte.decode("utf-8")      #Convert to string

    if("RESET" in msg):
        ard.close()                 #Reset string to close port
        break
    print(msg)
        
