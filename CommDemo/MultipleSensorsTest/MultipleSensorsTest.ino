#include <NewPing.h>

//Distance sensor1 pin configuration
#define TRIGGER_PIN_1  12
#define ECHO_PIN_1     11 

//Distance sensor2 pin configuration
#define TRIGGER_PIN_2  10
#define ECHO_PIN_2     9

//Once again pin choice is arbitary

#define SONAR_NUM 2

#define MAX_DISTANCE 200 
// Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.


//Sensors are saved in array of sonars
NewPing sonar[SONAR_NUM] = 
{
  NewPing(TRIGGER_PIN_1, ECHO_PIN_1, MAX_DISTANCE),
  NewPing(TRIGGER_PIN_2, ECHO_PIN_2, MAX_DISTANCE)
};

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  //Print the data from the first sensor
  Serial.print("Ping1:");
  Serial.print(sonar[0].ping_cm());
  Serial.print(" ");
  
  //Print the data from the second sensor
  Serial.print("Ping2:");
  Serial.print(sonar[1].ping_cm());
  Serial.println("");
}
