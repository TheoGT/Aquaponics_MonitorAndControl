import serial
import statistics
from datetime import datetime

#Define a class
#Class handles both analyzing incoming data by taking average of 10 datapoints
#and writing data to the correct file
class dataHandler:      
    def __init__(self, name):
        fileName = name + ".txt"
        self.file = open(fileName, "w")     #text file that records data
        self.data = []                      #Buffer that stores and averages dataPoints
        self.numData = 10
        

    
    

port = "/dev/cu.wchusbserial1410"   #port name, probably COM4 on window

ard = serial.Serial(port, 9600)     #9600 open on arduino
dict = {}
count = 0

ard.readline()                      #Reads initial data which can be garbage since port opens in middle of writing

print("Recording...")
while (count < 100):
    byte = ard.readline()           #reads byte code ending in line-terminator
    msg = byte.decode("utf-8")      #Convert to string
    time = datetime.now()
    msgList = msg.split()
    print(msgList[0])
    print(msgList[1])
    print("---------------\n")

    for dataPoints in msgList:
        dataSplit = dataPoints.split(":")
        print(dataSplit[0])
        print(dataSplit[1])
        print("====\n")
        try:                                                                        #Store data in the correct DataHandler class
            dictEntry = dict[dataSplit[0]]
            dictEntry.data.append(float(dataSplit[1]))
            if (len(dictEntry.data) >= dictEntry.numData):
                dataPoint = statistics.mean(dictEntry.data)
                dictEntry.file.write(str(time) + "," + str(dataPoint) + "\n")
                dictEntry.data = []
        except KeyError:                                                            #New Datatype is received, must create file for it
            print("new entry created\n")
            newEntry = dataHandler(dataSplit[0])
            newEntry.data.append(float(dataSplit[1]))
            dict[dataSplit[0]] = newEntry
            
    count+=1   

    
print("Done Recording")
for entries in dict:
    dict[entries].file.close()
ard.close()

