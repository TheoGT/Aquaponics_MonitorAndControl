//Liquid flow rate sensor -DIYhacking.com Arvind Sanjeev
byte statusLed    = 13;

byte sensorInterrupt = 0;
byte sensorPin       = 2;
//Pin 2 Must be used

// The hall-effect flow sensor outputs approximately 4.5 pulses per second per
// litre/minute of flow. Used for calibration 
float calibrationFactor = 4.5;

volatile byte pulseCount;  

float flowRate;
unsigned int flowMilliLitres;
unsigned long totalMilliLitres;

unsigned long oldTime;

void setup()
{
  Serial.begin(9600);
   
  // Set up the status LED line as an output
  pinMode(statusLed, OUTPUT);
  digitalWrite(statusLed, HIGH); 
  
  pinMode(sensorPin, INPUT);
  digitalWrite(sensorPin, HIGH);
  
  //Variables used to calcuate flow rate
  pulseCount        = 0;
  flowRate          = 0.0;
  flowMilliLitres   = 0;
  oldTime           = 0;

  // The Hall-effect sensor is connected to pin 2 which uses interrupt 0.
  // Configured to trigger on a FALLING state change (transition from HIGH
  // state to LOW state)
  attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
}

void loop()
{
   // Only process counters once per second
   if((millis() - oldTime) > 1000)
  { 
    //Temporarily disable the interrupt while calculating flow rate and sending the value to the host
    detachInterrupt(sensorInterrupt);
        
    //Code that calcualtes the flow rate
    flowRate = ((1000.0 / (millis() - oldTime)) * pulseCount) / calibrationFactor;
    flowMilliLitres = (flowRate / 60) * 1000;

    oldTime = millis();
       
     
    // Print the number of millilitres flowed in this second
    Serial.print("Current Liquid Flowing: "); 
    Serial.print(flowMilliLitres);
    Serial.print("mL/Sec");

    // Reset the pulse counter so we can start incrementing again
    pulseCount = 0;
    
    //Re-enable the interrupt again now that we've finished sending output
    attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
  }
}

/*
Insterrupt Service Routine
 */
void pulseCounter()
{
  // Increment the pulse counter
  pulseCount++;
}
