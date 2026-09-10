# EMG Gesture Classification: A Feasibility Study with a Cross-Subject Generalization Failure Analysis

## Overview
This project tests whether surface EMG signals can be decoded into hand gesture commands, the core signal processing problem behind myoelectric prosthetic control. 
Using the public Ninapro DB1 dataset, a classifier was built to distinguish three hand gestures (rest, fist, open hand), first on a single subject, then tested on 
multiple subjects it had never seen.

## Motivation
Robotic prosthetic arms translate muscle signals into movement commands. In amputees, the muscles that once controlled the hand are often still present in the residual limb
and contract when the user attempts a hand movement. Myoelectric control captures this residual signal via surface electrodes and decodes it into movement commands. 
This project tests the decoding step using public data from subjects whose limbs are still intact, learning what each gesture's muscle signal looks like so the same approach 
could be applied to detecting intended gestures from the residual muscle signals of amputees, as a foundation for more advanced robotic control systems.

## Dataset
- **Source:** Ninapro DB1, Exercise B (E2)
- **Recording setup:** 10 Otto Bock MyoBock surface EMG electrodes per subject
- **Gestures used:** Rest (label 0), Open Hand (label 5), Fist (label 6)
- **Link to source:** https://ninapro.hevs.ch/instructions/DB1.html

Exercise B has no true "pinch" gesture, so it was excluded rather than approximated with a poor substitute.

## Methodology
- **Filtering:** Raw EMG signal filtered to isolate the three target gestures
- **Windowing:** Signal split into 50-sample windows with 50% overlap.
- A 200-sample window initially left only 5 usable windows for Open Hand, since larger windows straddled label boundaries within each short gesture repetition.
- Reducing to 50 samples recovered 79 usable windows.
- **Feature extraction:** RMS, Mean Absolute Value, and Zero-Crossings extracted per window, per channel (10 channels × 3 features = 30 features per window)
- **Class balancing:** Rest samples outnumbered gesture samples (3,551 rest windows vs. 79 Open Hand windows before balancing),
  since rest periods between repetitions are recorded continuously.
- All classes were undersampled to match the smallest class to prevent the classifier from defaulting to "predict rest."
- **Classification:** Random Forest (100 trees) and SVM (RBF kernel)

## Results

### Single-Subject Classification (Subject 1)
80/20 split of Subject 1's data (189 train / 48 test windows):

| Model        |Accuracy|
|--------------|--------|
| SVM          |        |
|(RBF kernel)  | 89.58% |
|Random forest |        |
|  (100 trees) | 97.92% |

Random Forest outperformed SVM by ~8 points, consistent with its handling of the irregular, noisy patterns typical of EMG signals.

**Classification Report (Random Forest):**

| Gesture | Precision | Recall | F1-score |
|---------|-----------|--------|----------|
| Rest    |   0.94    |  1     |   0.97   |
|Open hand|    1      |  1     |    1     |
| Fist    |    1      | 0.94   |   0.97   |

![Confusion Matrix - Single Subject](single%20subject%20data/confusion_matrix.png)

**5-Fold Cross-Validation:** to check the result wasn't a lucky split, 5-fold cross validation ran on the same data:

- Mean accuracy: **95.36%** (± 2.44%)
- Range across folds: 91.67% – 97.92%

This confirms the result is stable, not an artifact of one split.

### Cross-Subject Generalization
Trained on Subjects 2 and 3 (630 windows), tested on Subject 4 (348 windows, unseen during training).

Accuracy dropped from 97.92% to **67%**:

| Gesture | Precision | Recall | F1-Score |
|---|---|---|---|
| Rest | 0.86 | 0.98 | 0.92 |
| Open hand | 0.71 | 0.04 | 0.08 |
| Fist | 0.54 | 0.97 | 0.70 |

![Confusion Matrix - Cross-Subject](multiple%20subjects%20data/confusion_matrix_multi_subject.png)

Rest and Fist transferred across subjects; Open Hand was almost never identified correctly (recall = 0.04), mostly misclassified as Fist.

## Discussion
The gap between single subject accuracy (97.92%, confirmed at 95.36% through cross validation) and cross subject accuracy (67%) reflects inter-subject variability: 
EMG patterns differ between individuals due to muscle geometry, electrode placement, and signal amplitude, so a classifier trained on one person's muscle activity 
doesn't transfer directly to another. 
This is one reason commercial myoelectric prosthetics require per-user calibration.
The Open Hand failure may not be pure inter-subject variability.Though, It had the fewest training windows even after balancing (79, vs. 128 for Fist pre-rebalancing), 
so the model may have had less data to learn robust, subject-invariant features for this gesture, a data scarcity confound, not necessarily a signal variability one. 
Separating these two explanations requires a larger, more balanced dataset.

## Limitations
- **Small dataset:** cross-validation confirmed stability (95.36% ± 2.44%), but 237 total windows remains small by ML standards
- **Limited gesture set:** 3 gestures, fewer than practical prosthetic control requires
- **Single repetition windows only:** windows straddling a label boundary were discarded, disproportionately cutting data for smaller classes
- **Confounded generalization result:** Open Hand's failure may reflect data scarcity as much as inter-subject variability (see Discussion)

## Future Work
- More subjects, to separate data scarcity from genuine inter-subject variability
- A larger gesture set
- Per subject feature normalization to reduce inter-subject variability
- Hardware simulation (ESP32 + servo gripper) for active gesture to actuation control

## How to Run
Install:
pip install numpy scipy scikit-learn matplotlib


Download Ninapro DB1 subject data from the official Ninapro website.
- `single subject data/load_emg_data.py` — preprocess and visualize Subject 1's data
- `single subject data/train_classifier.py` — train and evaluate the single-subject classifier
- `single subject data/cross_validation.py` — verify result stability
- `multiple subjects data/train_multi_subject_code.py` — build the cross-subject dataset
- `multiple subjects data/train_multi_subject_classifier.py` — train and evaluate cross-subject generalization
