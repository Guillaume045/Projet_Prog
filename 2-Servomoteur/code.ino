#include <Servo.h>

Servo servo_1;

void setup() {
servo_1.attach(8); 
}

void loop() {
  servo_1.write(0);
  delay(1500);
  servo_1.write(180);
  delay(1500);
}