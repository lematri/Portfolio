
# Leila Elmatri - Engineering Portfolio

Biomedical Engineering undergraduate at the University of Kent, with interests in robotics, embedded systems, sensing and medical devices.

This portfolio showcases projects in robotics, signal processing, machine learning, PCB design and simulation, from university projects to industry work.

## Industry Experience

### Medical simulations Intern, LHUSTEK Health Technology Incubation Centre and Vital Simulation Center, Lokman Hekim University, Ankara
July 2 2026 to July 31 2026
([view project](EMG%20gesture%20classification/))

- Built an EMG gesture classification pipeline in Python, decoding hand gestures from surface EMG signals using the public Ninapro DB1 dataset as a first step towards myoelectric prosthetic control 
  - Random Forest reached 97.92% accuracy on a single subject, confirmed at 95.36% ± 2.44% with 5 fold cross-validation
  - Tested on an unseen subject, where accuracy dropped to 67%, and analysed whether this came from inter subject variability or data scarcity
- Contributed to a comparative research report benchmarking the Vital Simulation Center against internationally accredited simulation centres (WISER, SIMS, CAMES)
- Wrote a blog post for LHUSTEK on biomedical engineering entrepreneurship, covering idea validation, medical device regulation (EU MDR, UK UKCA/MHRA, Turkey TITCK) and commercialisation
- Skills: Python, scikit-learn, signal processing, machine learning, research and benchmarking, medical device regulation, technical writing

### Research Intern, University of Kent, Engineering labs
December 2024 to February 2025
[View project](Capacitive%20cell%20growth%20sensor/)

- Designed and simulated an interdigitated electrode capacitive sensor for monitoring human cell growth, then printed it using a direct-write PCB printer.
- Simulated the electric field, potential distribution and capacitance matrix in CST Studio Suite
- Found a mutual capacitance of about 35 pF between the electrodes
- Skills: CST Studio Suite, electrostatic simulation, sensor design, printed electronics

## Projects

### Bipedal Walking Robot: Walking, Towing and Squatting
[View project](Bipedal%20robot/)

Second year team project (team of four). A 6-servo bipedal robot controlled by an M5StickS3 (ESP32-S3), able to walk, tow a weighted sled, and squat while holding a load.

- My role: robot kinematics and movement
- Implemented inverse kinematics for the walking gait, modelling each leg as a two-link chain
- Wrote and tuned the walking gait and squatting routine, changing one parameter at a time and logging each trial
- Improved squat depth from 3.5 cm to 4.5 cm, holding 1.35 kg in the weight holder
- Team result: towing increased from 200 g to 1 kg, controlled from a WiFi web interface hosted on the robot
- Tools: Arduino/C++, M5StickS3, I2C servo control, Fusion 360

### Mechanical Hand Gripper with Force Sensing
[View project](mechanical_gripper_system.ino/)

Individual first year project. A servo-driven gripper with a force sensor, OLED display, buzzer warning and Bluetooth control from an Android device.

- Designed the PCB schematic and layout, mounted onto the back of the gripper
- Designed the gripper arms and full assembly in Fusion 360
- Wrote the Arduino code for the main version and the Bluetooth version
- Tools: Arduino/C++, PCB design, Fusion 360, Bluetooth

## Upcoming Projects

### Robotic Light Sensitive Eye
Final year project, University of Kent

Retina scanners in high security settings can sometimes be fooled by a copy or photo of a person's eye, so some systems now shine a light and check that the pupil responds, to confirm it's a real person. This project will test how robust that check is by building a 3D printed artificial eye whose pupil responds to light in a realistic way.
- Design a light sensitive circuit to detect changes in light level
- Build a microscale bladder system to change the size of an artificial pupil in response to light
- 3D print the eye and tune the pupil response to match a real eye as closely as possible
- Areas: biomedical sensing, embedded systems, soft robotics, biometric security
  
## Technical Skills

**Programming & Data Analysis**
Python, C++, MATLAB, R

**Signal Processing & Machine Learning**
Biosignal processing (EMG), feature extraction, Random Forest, SVM, cross-validation

**Robotics**
Inverse kinematics, gait design, servo control

**Design & Simulation**
Fusion 360, COMSOL Multiphysics, CST Studio Suite

**Embedded Systems**
Arduino, ESP32, M5Stack, PCB design, sensors, I2C, Bluetooth, WiFi, IoT

**Biomedical Engineering**
Medical device design, biosignal processing, biomechanics, medical device regulation

## Career Interests

Industry roles and graduate study in:

- Robotics and automation
-  AI and machine learning for engineering, especially applying it to sensor data, signal processing and robotic control
- Embedded systems and sensing
- Medical devices
- General engineering roles in design, testing and development

## Contact

- Email: leilaelmateri@icloud.com
- LinkedIn: https://www.linkedin.com/in/leila-elmatri-355023308?utm_source=share_via&utm_content=profile&utm_medium=member_ios 
