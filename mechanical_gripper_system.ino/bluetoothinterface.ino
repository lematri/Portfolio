#include <Servo.h>
#include <SoftwareSerial.h>

// Bluetooth Configuration
#define Blue_RX_PIN 10  // Connect pin 10 to TX
#define Blue_TX_PIN 9 // Connect pin 9 to Rx
SoftwareSerial Blue(10, 9);  // RX, TX pins


Servo myservo; //servo variables
const int servo_pin = 11;
const int open_arms = 0;
const int closed_arms = 180;


const int FSR_PIN = A1; // force sensor variables
int forceValue = 0;
int close = false;

void setup() {
Serial.begin(9600);
Blue.begin(9600);  // Start Bluetooth

myservo.attach(servo_pin);
pinMode(FSR_PIN, INPUT);

  myservo.write(open_arms);  // open gripper
Blue.println("Ready: 1=Open, 0=close");
  }

  void loop()
  {

forceValue = analogRead(FSR_PIN);   //read force sensor
if(Blue.available()) {  // Process bluetooth commands
char cmd = Blue.read();
if(cmd == '0') {        // Open command
myservo.write(open_arms);
close = false;
Blue.println("Opened");
}

else if(cmd == '1') {  // cube is being gripped
close = true;
Blue.println("Gripping");
}
}
if(close) {
int angle = map(forceValue, 0, 1023, 60, closed_arms);
myservo.write(angle);
Blue.print("Force:");
Blue.println(forceValue);
}
delay(50);
}
