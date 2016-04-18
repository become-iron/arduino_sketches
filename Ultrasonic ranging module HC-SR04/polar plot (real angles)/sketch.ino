#include "Ultrasonic.h";
#include <Servo.h>;

Ultrasonic ultrasonic(14, 16);
Servo myservo;

int PIN_ADD_VCC = 6;
int pos = 0;  // position of servo

void setup()
{
  pinMode(PIN_ADD_VCC, OUTPUT);  // additional vcc port

  myservo.attach(9);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(PIN_ADD_VCC, HIGH);
  
  for(pos = 0; pos <= 180; pos += 1)
  {
    myservo.write(pos);
    Serial.println(ultrasonic.Ranging(CM));
    Serial.println(pos);
    delay(15);
  }
  for(pos = 180; pos >= 0; pos -= 1)
  {
    myservo.write(pos);
    Serial.println(ultrasonic.Ranging(CM));
    Serial.println(pos);
    delay(15);
  }
}
