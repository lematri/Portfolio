import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load the E2 file
data = scipy.io.loadmat('s1.mat/S1_A1_E2.mat')

emg = data['emg']
labels = data['restimulus']

# Keep only rest (0), fist (6), open hand (5)
target_labels = [0, 5, 6]
mask = np.isin(labels, target_labels).flatten()
emg_filtered = emg[mask]
labels_filtered = labels[mask].flatten()

print("Filtered EMG shape:", emg_filtered.shape)

# Windowing settings
window_size = 50  # samples per window 
step_size = 25    # overlap between windows (50% overlap)

def extract_features(window):
    """Extract simple time-domain features from one window of EMG data."""
    rms = np.sqrt(np.mean(window**2, axis=0)) # Root Mean Square
    mav = np.mean(np.abs(window), axis=0)  # Mean Absolute Value
    zc = np.sum(np.diff(np.sign(window), axis=0) != 0, axis=0) # Zero Crossings
    return np.concatenate([rms, mav, zc])

# --- Create windows ---
features_list = []
window_labels = []

for start in range(0, len(emg_filtered) - window_size, step_size):
    window = emg_filtered[start:start + window_size]
    window_label_set = labels_filtered[start:start + window_size]

    # Only keep windows where all samples belong to the same gesture
    if len(np.unique(window_label_set)) == 1:
        features_list.append(extract_features(window))
        window_labels.append(window_label_set[0])

features = np.array(features_list)
window_labels = np.array(window_labels)

print("\nBefore balancing:")
for g in target_labels:
    print(f"Gesture {g}: {np.sum(window_labels == g)} windows")

# --- Balance classes: undersample rest to match smallest gesture class ---
gesture_counts = {g: np.sum(window_labels == g) for g in target_labels}
min_count = min(gesture_counts.values())

balanced_indices = []
for g in target_labels:
    indices = np.where(window_labels == g)[0]
    chosen = np.random.choice(indices, size=min_count, replace=False)
    balanced_indices.extend(chosen)

balanced_indices = np.array(balanced_indices)
features_balanced = features[balanced_indices]
labels_balanced = window_labels[balanced_indices]

print("\nAfter balancing:")
for g in target_labels:
    print(f"Gesture {g}: {np.sum(labels_balanced == g)} windows")

print("\nFinal feature matrix shape:", features_balanced.shape)

# Save these for the next step (training the classifier)
np.save('features.npy', features_balanced)
np.save('labels.npy', labels_balanced)
print("\nSaved features.npy and labels.npy for next step")