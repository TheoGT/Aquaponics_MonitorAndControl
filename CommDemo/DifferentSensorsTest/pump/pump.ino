#include <SoftwareSerial.h>                           
#define rx 2                                          
#define tx 3  
//RX = Receive Data
//TX = Transmit Data
//Pins are arbitary

SoftwareSerial myserial(rx, tx);
//Put the RX pin first, followed by the TX pin
//Mnemomic: Listen (receive) before you speak (transmit)


String inputstring = "";
String devicestring = "";

boolean input_string_complete = false;
boolean device_string_complete = false;

float ml;                                             



void setup() 
{                                        	      
  Serial.begin(9600); 
  
  myserial.begin(9600);
  //Serial used by pump
	
  inputstring.reserve(10);                    
  devicestring.reserve(30);
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
    if (input_string_complete == true) 
    {             
        myserial.print(inputstring);
        myserial.print('\r');
        //Command is sent to pump
	//IF YOU ONLY CARE ABOUT HOW TO USE THE PUMP
	//THE ABOVE TWO LINES OF CODE ARE TO SEND COMMNANDS
	 
	//Removes the user original command
        inputstring = "";
	input_string_complete = false;
  }

  //Pump sends information back
  //Exampes of inforamtion are things such as pumping status and total volumed pump
  if (myserial.available() > 0) 
    char inchar = (char)myserial.read();
    devicestring += inchar; 
    //All the information from the pump has been transmitted
    if (inchar == '\r') 
    {
      device_string_complete = true;
    }
  }

  //Prints the information from the pump onto the serial monitor
  if (device_string_complete == true) 
  {
    Serial.println(devicestring); 
    if (isdigit(devicestring[0]) || devicestring[0]== '-')
    {
        ml = devicestring.toFloat();
    }
	  
    //Remove the original data sent by the pump  
    devicestring = ""; 
    device_string_complete = false;  
  }
}
