#include <NewPing.h>

#define TRIGGER_PIN_1  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN_1     11  // Arduino pin tied to echo pin on the ultrasonic sensor.

#define TRIGGER_PIN_2  10  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN_2     9  // Arduino pin tied to echo pin on the ultrasonic sensor.

#define SONAR_NUM 2

#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.



NewPing sonar[SONAR_NUM] = {
  NewPing(TRIGGER_PIN_1, ECHO_PIN_1, MAX_DISTANCE),
  NewPing(TRIGGER_PIN_2, ECHO_PIN_2, MAX_DISTANCE)
};

void setup() {
  Serial.begin(115200); // Open serial monitor at 115200 baud to see ping results.
}

void loop() {                    // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  
  Serial.print("Ping1:");
  Serial.print(sonar[0].ping_cm()); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.print(" ");
  Serial.print("Ping2:");
  Serial.print(sonar[1].ping_cm()); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.println("");
}

bool timeComp()
{
}
