#include <Servo.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

int pos = 0;    // variable to store the servo position
//all variables
String grip;
Servo myservo;
const int pot_pin = A0; //Oled pin
const int FSR_PIN = A1; //force sensor pin
const int BUZZER_PIN = 12; //buzzer pin
const int buttonPin = 2; //SW2
const int buttonpin1 = 4; //SW1
const int ledPin = 6; //led pin
const int open_arms = 0; // open gripper arm variable
const int close_arms = 180; //closed gripper arm variable

 //servo and button state variables to control grippers
int val;
int servo_angle = 0;
int analogReading = 0;
int buttonState = 0;
int buttonstate1 = 0;
int lastbuttonState =LOW;
int lastbuttonState1 =LOW;

//output and input set ups
void setup() {
  Serial.begin(9600);
  myservo.attach(11);
  pinMode(pot_pin, INPUT);
  pinMode(FSR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(buttonpin1, INPUT);


  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("failed to access OLED."); //display if oled unable to connect to oled
    for(;;);
  }


}
void loop() {
  // Read force sensor
  analogReading = analogRead(FSR_PIN); //analogue read for force sensor
  val = analogReading;

  Serial.print("FSR reading: ");
  Serial.print(val);

  // Map the force sensor value to servo angle
  servo_angle = map(val, 0, 1023, 0, 180);
  Serial.print(" mapped value ");
  Serial.println(servo_angle);
  myservo.write(servo_angle);

  buttonState = digitalRead(buttonPin);
  buttonstate1 = digitalRead(buttonpin1);

  if (buttonState == HIGH && lastbuttonState1 == LOW)
  {
    Serial.println("OPENING GRIPPER");
  //myservo.write(open_arms);
    for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees

    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       //15ms delay
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       //15ms delay

  }
  }

  if (buttonstate1 == HIGH && lastbuttonState == LOW){ //tells buttons it should be the opposite of last button state
  Serial.println("CLOSING GRIPPER");
  myservo.write(close_arms);
  }
  delay (1000); //delays the grippers from closing by 1s

  //reading state of buttons
  lastbuttonState = digitalRead(buttonPin);
  lastbuttonState1 = digitalRead(buttonpin1);

  if (buttonState == HIGH);{
    digitalWrite(ledPin, LOW);
  }

    if (buttonState == HIGH);{
    digitalWrite(ledPin, LOW);
    }

  // Determine grip strength
  if (analogReading < 200) {
    Serial.println(" light grip"); //if the force detected by the buzzer is 200-400 it is a light a force
    grip = " light grip";
  }
  else if (analogReading < 500) {
    Serial.println(" light to medium grip");//if the force detected by the buzzer is 500-700 it is a light a force
    grip = " light to medium grip";
  }
  else if (analogReading < 800) {
    Serial.println(" medium grip");//if the force detected by the buzzer is 800 it is a light a force
    grip = " medium grip";
  }
  else {
    Serial.println(" strong grip");//any force over 800 is a strong grip
    grip = " strong grip";
  }

  // Update oled display
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 10);
  display.print("Force reading = "); //this will be displyed on the oled screen before force sensor value
  display.println(analogReading);
  display.println(grip);
  display.display();


  // Buzzer control
  if (val > 512) { //if force sensor detects a pressure of 512 it will activate the buzzer to start
    tone(BUZZER_PIN, 1000);
  }
  else {
    noTone(BUZZER_PIN);
  }
}
