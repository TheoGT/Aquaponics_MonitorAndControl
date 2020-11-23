#include <SoftwareSerial.h>                           //we have to include the SoftwareSerial library, or else we can't use it
#define rxPump 2                                          //define what pin rx is going to be
#define txPump 3                                          //define what pin tx is going to be
#define rxEC 4
#define txEC 5

SoftwareSerial readerSerialOne(rxPump, txPump);                      //define how the soft serial port is going to work
SoftwareSerial readerSerialTwo(rxEC, txEC);                      //define how the soft serial port is going to work

String pumpString = "";                                         //a string to hold incoming data from the PC
boolean pumpStringComplete = false;
String sensorString = "";
boolean sensorStringComplete = false;

float salinity = 0.0;


void setup() 
{
  Serial.begin(9600);
  readerSerialOne.begin(9600);            //Pump
  readerSerialTwo.begin(9600);            //EC
  //readerSerialOne.listen();
  pumpString.reserve(10);
  sensorString.reserve(30);
}

void serialEvent() 
{
  sensorString = Serial.readStringUntil(13);
  sensorStringComplete = true;
}

void loop() 
{
    if (readerSerialTwo.available() > 0) 
    {                     
      char inchar = (char)readerSerialTwo.read();              
      sensorString += inchar;                           
      if (inchar == '\r') 
      {                            
        sensorStringComplete = true;                  
      }
    }
    if (sensorStringComplete == true)
    { 
      if (isdigit(sensorString[0]) == false)
        Serial.print(sensorString);
      else                                      
        printECData();  
      sensorString = "";
      sensorStringComplete = false;
      if(salinity > 1000.0)
      {
        readerSerialOne.print("D,4");
        readerSerialOne.print('\r');
        delay(2000);
      }
    }
}

void printECData(void)
{
  char *EC;
  char sensorStringArray[30];

  sensorString.toCharArray(sensorStringArray, 30);
  EC = strtok(sensorStringArray, ",");
  Serial.print("EC:");
  salinity = atof(EC);
  Serial.println(salinity);
}
