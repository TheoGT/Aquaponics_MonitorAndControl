#define INPUT_PIN 12
#define RESET_PIN 9

bool pressed = false;                                       //Ensures only rising edge signal is sent

void setup() 
{
  pinMode(RESET_PIN, INPUT); 
  pinMode(RESET_PIN, INPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if (digitalRead(RESET_PIN))
  {
    //Serial.println("RESET");                                //Sends RESET string to python code
  }
  else if (digitalRead(INPUT_PIN) && !pressed)
  {
    Serial.println("PRESSED");                              //Sends a generic PRESSED string to python code
    pressed = true;
  }

  else if (!digitalRead(INPUT_PIN) && pressed)
  {
    pressed = false;
  }
}
