#include <SoftwareSerial.h>                           
#define rx 2                                          
#define tx 3   
//RX = Receive Data
//TX = Transmit Data
//Pin choice is arbitary

SoftwareSerial myserial(rx, tx);
//Put the RX pin first, followed by the TX pin
//Mnemonic: Listen (receive) before you speak (transmit)

String inputstring = "";
String sensorstring = "";

boolean input_string_complete = false; 
boolean sensor_string_complete = false;




void setup() {                                        
  Serial.begin(9600);
	
  myserial.begin(9600);
  //Serial used by sensor
	
  inputstring.reserve(10);
  sensorstring.reserve(30);
}


//Used for inputed command in Arduino serial monitor
void serialEvent() 
{
  inputstring = Serial.readStringUntil(13);
  input_string_complete = true;
}


void loop() 
{
  //User types a command in the serial monitor
  Serial.println(String(input_string_complete));
  if (input_string_complete == true) 
  { 
    myserial.print(inputstring); 
    myserial.print('\r'); 
    //Command is sent to the pH sensor
	
    //Remove the user's original command	  
    inputstring = ""; 
    input_string_complete = false;
  }

  //sensor sends data back.
  //Records data bytes to arduino serial
  if (myserial.available() > 0) 
  {
    char inchar = (char)myserial.read();
    sensorstring += inchar; 
    if (inchar == '\r') 
    { 
      sensor_string_complete = true;
    }
  }


  if (sensor_string_complete == true) 
  { 
    if (isdigit(sensorstring[0]) == false) 
    { 
      //Print non-conductivity data text
      //These are things such as pH status or errors
      Serial.println(sensorstring);  
    }
    else  
    {
      //Print the conductivity data
      print_EC_data();
    }
	  
    //Remove original data from the conductivity sensor
    sensorstring = "";
    sensor_string_complete = false;
  }
}


//Code to change sensor data to a readable string
void print_EC_data(void) 
{ 
  char sensorstring_array[30];
  char *EC;                                           
  //char pointer used in string parsing

  float f_ec;
  
  sensorstring.toCharArray(sensorstring_array, 30);
  EC = strtok(sensorstring_array, ",");
	
  Serial.print("EC:");
  Serial.println(EC);
	
  f_ec= atof(EC);                                     
  //This line to convert the char to a float
  //Used f_ec when comparing conductivity value in arduino
}
