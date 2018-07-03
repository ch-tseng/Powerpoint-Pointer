#include <SoftwareSerial.h>
SoftwareSerial Serial1(2, 3); // RX, TX

byte pinNotify = 5;
byte pinUp = 8;
byte pinDown = 9;

boolean notifyState = 0;
boolean upState = 0;
boolean downState = 0;

void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);

  pinMode(pinUp, INPUT);
  pinMode(pinDown, INPUT);

}

void loop() {
  notifyState = digitalRead(pinNotify);
  upState = digitalRead(pinUp);
  downState = digitalRead(pinDown);

  //Serial.print(upState);
  //Serial.print(" / ");
  //Serial.println(downState);

  if ( notifyState == 1) {
    Serial.println("Notice");
    Serial1.write('N');
    delay(500);
    Serial1.flush();
  }

  if (upState == 1) {
    Serial.println("Up");
    Serial1.write('U');
    delay(500);
    Serial1.flush();
  }

  if (downState == 1) {
    Serial.println("Down");
    Serial1.write('D');
    delay(500);
    Serial1.flush();
  }



}
