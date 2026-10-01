# Interdigitated Electrode Capacitive Sensor for Cell Growth Monitoring: Simulation and Printing

Research internship, [University of kent] (December 2024 to Feburary 2025)

## Summary
- **Sensor:** interdigitated electrode (IDE) capacitive sensor on a circular polyimide substrate
- **Simulation:** electrostatic simulation in CST Studio Suite, giving the electric field, potential distribution and capacitance matrix
- **Result:** mutual capacitance of about 35 pF between the two electrodes
- **Fabrication:** printed using a Voltera V-One direct write PCB printer
- **Application:** monitoring human cell growth in a Petri dish filled with  nutrient broth

## Motivation
This project was inspired by FinalSpark's Neuroplatform, a biocomputing system that uses living human brain organoids placed on multi electrode arrays (Jordan et al., 2024). The paper sparked my interest in how electrodes are designed to interface with biological systems, which led to this project on simulating and printing an interdigitated electrode capacitive sensor.

The sensor was designed to monitor human cell growth in a Petri dish. As cells grow and cover the electrodes, they change the electric field between the electrode fingers, which changes the measured capacitance. The circular substrate was designed to fit inside the dish.

- ## My Role
I carried out this project under the supervision of Viktorija Makavoraite, who oversaw the work and demonstrated the PCB printer.
- Designed the interdigitated electrode geometry in CST Studio Suite
- Set up the electrostatic simulation, including the materials, boundary box and electrode potentials
- Ran the simulations and extracted the electric field, potential distribution and capacitance matrix
- Explored how finger width, height and gap affect capacitance in simulation before settling on the final design
- Prepared the design for printing and learned how direct-write PCB printing works through a demonstration

## Sensor Model
- Two interdigitated electrodes (Pos and Neg) on a circular polyimide substrate (relative permittivity 3.5)
- Modelled in CST Studio Suite and placed inside a bounding box for the electrostatic solver

## Simulation

### Electric Field and Potential
- A potential difference was applied between the two electrodes
- The field is strongest in the gaps between the electrode fingers, which is the sensing region of an IDE sensor

### Capacitance Matrix
| | Neg | Pos |
|---|---|---|
| **Neg** | 39.5 pF | -35.0 pF |
| **Pos** | -35.0 pF | 39.1 pF |

- The diagonal values are each electrode's self-capacitance
- The off diagonal value gives the mutual capacitance between the electrodes, about 35 pF, which is the value that changes when the sensor is used

## Fabrication
- The sensor design was printed with a [Voltera V-One] direct-write PCB printer using conductive ink

## Images

**1. Sensor model in CST Studio Suite**
Interdigitated electrodes on a circular polyimide substrate, inside the bounding box used by the electrostatic solver.

![Sensor model in CST](images/sensor_model.png)

**2. Electric field**
Electric field vectors across the sensor, strongest in the gaps between the electrode fingers.

![Electric field](images/electric_field.png)

**3. Electric potential distribution**
Potential across the sensor surface, with the positive electrode in red and the negative electrode in blue.

![Electric potential distribution](images/electric_potential.png)

**4. Capacitance matrix results**
Self and mutual capacitance values from the electrostatic solver.

![Capacitance matrix results](images/capacitance_matrix.png)

**5. Electrode port setup**
Schematic view showing the Pos and Neg potential ports assigned to the two electrodes.

![Electrode port setup](images/schematic_view.png)

**6. Direct-write PCB printer**
The [Voltera V-One] printer used to print the sensor design with conductive ink.

![PCB printer](images/printer.png)

## Limitations
- The printed sensor's capacitance wasn't measured, so the simulated value hasn't been compared against a real sensor yet

## Future Work
- Measure the printed sensor's capacitance with an LCR meter and compare it to the 35 pF simulation
- Repeat the finger width, height and gap study in CST and record the capacitance for each design, to show how geometry affects sensitivity
- Test the sensor in a Petri dish with nutrient broth, first without cells to get a baseline, then track how the capacitance changes as cells grow on the electrodes

## Tools
- CST Studio Suite (electrostatic solver)
- Voltera V-One direct write PCB printer

## Reference
Jordan, F.D., Kutter, M., Comby, J.-M., Brozzi, F. and Kurtys, E. (2024) 'Open and remotely accessible Neuroplatform for research in wetware computing', *Frontiers in Artificial Intelligence*, 7, 1376042. https://doi.org/10.3389/frai.2024.1376042