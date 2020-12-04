#include <NewPing.h>
#include <OneWire.h> 
#include <DallasTemperature.h>

#define TRIGGER_PIN_1  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN_1     11  // Arduino pin tied to echo pin on the ultrasonic sensor.

#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS); 
DallasTemperature sensors(&oneWire);

NewPing sonar = NewPing(TRIGGER_PIN_1, ECHO_PIN_1, MAX_DISTANCE);


void setup() {
  Serial.begin(9600); // Open serial monitor at 9600 baud to see ping results.
   sensors.begin();
}

void loop() {                    // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  
    Serial.print("Ping:");
    Serial.print(sonar.ping_cm()); // Send ping, get distance in cm and print result (0 = outside set distance range)
    Serial.print(" ");

    sensors.requestTemperatures();
    Serial.print("Temp:");
    Serial.println(sensors.getTempCByIndex(0));

}
