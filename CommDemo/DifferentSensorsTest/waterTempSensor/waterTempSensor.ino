//Code from https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806

#include <OneWire.h> 
#include <DallasTemperature.h>

//Pin Choice is arbitary, pin 2 is used
#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS); 
DallasTemperature sensors(&oneWire);
//Setting up the wire

//OneWire oneWire2(ARB_PIN);
//DallasTemperature sensors2(&oneWire2);

//Code for second sensor if needed
//ARB_PIN is another arbitary pin

void setup(void) 
{ 
 Serial.begin(9600); 
 Serial.println("Dallas Temperature IC Control Library Demo"); 
 
 sensors.begin(); 
 //sensors2.begin();
} 

void loop(void) 
{ 
 sensors.requestTemperatures(); 
 // Send the command to get temperature readings 
 
 Serial.print("Temperature is: "); 
 Serial.println(sensors.getTempCByIndex(0)); 
 //Serial.println(sensors2.getTempCByIndex(0));
 
 delay(1000); 
} 
