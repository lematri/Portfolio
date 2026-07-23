import scipy.io
import numpy as np

def load_subject_data(mat_path, target_labels=[0, 5, 6]):
    """Load and filter one subject's EMG data."""
    data = scipy.io.loadmat(mat_path)
    emg = data['emg']
    labels = data['restimulus']
    mask = np.isin(labels, target_labels).flatten()
    return emg[mask], labels[mask].flatten()

def extract_features(window):
    rms = np.sqrt(np.mean(window**2, axis=0))
    mav = np.mean(np.abs(window), axis=0)
    zc = np.sum(np.diff(np.sign(window), axis=0) != 0, axis=0)
    return np.concatenate([rms, mav, zc])

def process_subject(mat_path, window_size=50, step_size=25, target_labels=[0, 5, 6]):
    """Full pipeline: load, filter, window, extract features, balance classes."""
    emg, labels = load_subject_data(mat_path, target_labels)

    features_list = []
    window_labels = []
    for start in range(0, len(emg) - window_size, step_size):
        window = emg[start:start + window_size]
        label_set = labels[start:start + window_size]
        if len(np.unique(label_set)) == 1:
            features_list.append(extract_features(window))
            window_labels.append(label_set[0])

    features = np.array(features_list)
    window_labels = np.array(window_labels)

    # Balance classes
    gesture_counts = {g: np.sum(window_labels == g) for g in target_labels}
    min_count = min(gesture_counts.values())
    balanced_indices = []
    for g in target_labels:
        indices = np.where(window_labels == g)[0]
        chosen = np.random.choice(indices, size=min_count, replace=False)
        balanced_indices.extend(chosen)
    balanced_indices = np.array(balanced_indices)

    return features[balanced_indices], window_labels[balanced_indices]

# --- Load training subjects (1 and 2) ---
X1, y1 = process_subject('s1.mat/S1_A1_E2.mat')
X2, y2 = process_subject('s2.mat/S2_A1_E2.mat')

X_train = np.concatenate([X1, X2])
y_train = np.concatenate([y1, y2])

# --- Load test subject (3) — completely unseen during training ---
X_test, y_test = process_subject('s3.mat/S3_A1_E2.mat')

print("Training samples (subjects 1+2):", X_train.shape[0])
print("Test samples (subject 3, unseen):", X_test.shape[0])

np.save('X_train_multi.npy', X_train)
np.save('y_train_multi.npy', y_train)
np.save('X_test_multi.npy', X_test)
np.save('y_test_multi.npy', y_test)
print("\nSaved multi-subject train/test data")