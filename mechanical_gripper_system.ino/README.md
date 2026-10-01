# Mechanical Hand Gripper with Force Sensing

Individual First year engineering project, University of Kent

![Finished mechanical gripper](physical%20mechanical%20gripper%20system%20.png)

## Summary
- **Gripper:** servo-driven gripper with geared arms, a wooden chassis and 3D printed tips
- **Force sensing:** a force sensitive resistor (FSR) measures grip force
- **Feedback:** force reading and grip level shown on an OLED screen, with a buzzer warning above a set force
- **Control:** two push buttons to open and close the gripper
- **Bluetooth (advanced functionality):** the gripper opens when `0` is sent and closes when `1` is sent from an Android device, with grip force sent back over Bluetooth
- **PCB:** PCB mounted onto the back of the mechanical gripper, designed to connect the sensors, buttons, buzzer, LEDs, servo and relay to the microcontroller board

## My Role
- Designed the PCB schematic and layout, connecting the sensors, buttons, buzzer, LEDs, servo and relay to the microcontroller
- Designed the gripper arms and full assembly in Fusion 360. My parts weren't manufactured in time, as a result the final build used kit arms provided by the university
- Wrote the Arduino code for both the main version and the Bluetooth version
- Added Bluetooth control as advanced functionality, so the gripper can be operated from an Android device
- Assembled, wired and tested the finished gripper

## Hardware
- Arduino Uno
- Servo motor
- Force sensitive resistor
- 0.96 inch OLED display
- Piezo buzzer, LEDs and 2 push buttons
- Relay circuit on the PCB
- Bluetooth module
- Wooden chassis with geared gripper arms

## How It Works

### Main code (`mechanical_gripper_main_1.ino`)
- The FSR is read with `analogRead()` (0 to 1023) and printed to the serial monitor
- The reading is sorted into a grip level:
  - under 200: light grip
  - 200 to 499: light to medium grip
  - 500 to 799: medium grip
  - 800 and above: strong grip
- The force reading and grip level are shown on the OLED screen
- If the reading goes above 512, the buzzer sounds at 1 kHz as a warning
- One button sweeps the servo from 0° to 180° and back in 1° steps, and the other moves it to 180° to close the gripper

### Bluetooth code (`bluetoothinterface.ino`)
- Sending `0` from a phone opens the gripper
- Sending `1` starts gripping
- While gripping, the force reading is mapped to a servo angle between 60° and 180°, so the gripper closes further as more force is applied
- The force reading is sent back to the phone so it can be monitored live

## PCB Schematic
The schematic covers the switches, OLED, servo, buzzer, force sensor, LEDs and a relay circuit, with two headers that mate onto the microcontroller board.

![PCB schematic](PCB%20schematic%20.png)


## How to Run
- Open either `.ino` file in the Arduino IDE (the IDE will ask to put it in a folder with the same name, click OK)
- Install the Adafruit GFX and Adafruit SSD1306 libraries from the Library Manager (Servo and SoftwareSerial are already built into the Arduino IDE)
- Select your board and port, then upload
- Open the serial monitor at 9600 baud to see the force readings
- For the Bluetooth version, pair with the Bluetooth module and send `0` or `1` from a Bluetooth serial terminal app
- To view the CAD, open `Mechanical gripper assembled.f3z` in Fusion 360360


