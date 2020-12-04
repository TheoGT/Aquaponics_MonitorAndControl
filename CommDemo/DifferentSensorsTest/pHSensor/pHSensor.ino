#include "ph_grav.h"                           

Gravity_pH pH = Gravity_pH(A0);
//Must use an analog input pin

uint8_t user_bytes_received = 0;                
const uint8_t bufferlen = 32;                   
char user_data[bufferlen];
//Variables for reading data

//Used for calibration
//*************************************************
void parse_cmd(char* string) {                   
  strupr(string);                                
  if (strcmp(string, "CAL,7") == 0) {       
    pH.cal_mid();                                
    Serial.println("MID CALIBRATED");
  }
  else if (strcmp(string, "CAL,4") == 0) {            
    pH.cal_low();                                
    Serial.println("LOW CALIBRATED");
  }
  else if (strcmp(string, "CAL,10") == 0) {      
    pH.cal_high();                               
    Serial.println("HIGH CALIBRATED");
  }
  else if (strcmp(string, "CAL,CLEAR") == 0) { 
    pH.cal_clear();                              
    Serial.println("CALIBRATION CLEARED");
  }
}
//*************************************************

void setup() {
  Serial.begin(9600);                            
  
  if (pH.begin())
  {                                     
    Serial.println("Loaded EEPROM");
    //If text does not show up pH sensor did not begin fully
    //Reset arduino and rerun code
  }
}

void loop() {
  //Code for reading User inputed commands
  //Used for calibration purposes
  //*************************************************
  if (Serial.available() > 0) 
  {                                                      
    user_bytes_received = Serial.readBytesUntil(13, user_data, sizeof(user_data));   
  }

  if (user_bytes_received) 
  {                                                      
    parse_cmd(user_data);                                                          
    user_bytes_received = 0;                                                        
    memset(user_data, 0, sizeof(user_data));                                         
  }
  //*************************************************
  
  //Code that receives and dispays pH
  Serial.println(pH.read_ph());                                                      
}
