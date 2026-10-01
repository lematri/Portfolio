# Mechanical Hand Gripper with Force Sensing

First year engineering project, University of Kent

![Finished mechanical gripper](physical mechanical gripper sysytem.png)

## Summary
- **Gripper:** servo-driven gripper with geared arms, a wooden chassis and 3D printed tips
- **Force sensing:** a force sensitive resistor (FSR) measures grip force
- **Feedback:** force reading and grip level shown on an OLED screen, with a buzzer warning above a set force
- **Control:** two push buttons to open and close the gripper
- **Bluetooth (advanced functionality):** open when 0 is presed and close the gripper when 1 is pressed from a android device , with grip force sent back over Bluetooth
- **PCB:** PCB mounted onto the back of the mechanical grpper designed to connect the sensors, buttons, buzzer, LEDs, servo and relay to the microcontroller board


## Hardware
- Arduino [model]
- Servo motor
- Force sensitive resistor
- 0.96 OLED display
- Piezo buzzer, LEDs and 2 push buttons
- Relay circuit on the PCB
- Bluetooth module, used in the Bluetooth version
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

![PCB schematic](PCB schematic.png)

## Files
- `mechanical_gripper_main_1.ino`: main code (buttons, force sensor, OLED and buzzer)
- `bluetoothinterface.ino`: Bluetooth control code
- `Mechanical_gripper_assembled.f3z`: full Fusion 360 assembly
- `PCB_schematic_.png`: PCB schematic
- `physical_mechanical_gripper_sysytem_.png`: photo of the finished gripper

## How to Run
- Open either `.ino` file in the Arduino IDE (the IDE will ask to put it in a folder with the same name, click OK)
- Install the Servo.h,Softwareserial.h, Adafruit GFX and Adafruit SSD1306 libraries from the Library Manager
- Select your board and port, then upload
- Open the serial monitor at 9600 baud to see the force readings
- For the Bluetooth version, pair with the Bluetooth module and send `0` or `1` from a Bluetooth serial terminal app
- To view the CAD, open `Mechanical_gripper_assembled.f3z` in Fusion 360


