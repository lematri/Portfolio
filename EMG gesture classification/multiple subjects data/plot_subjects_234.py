import scipy.io
import numpy as np
import matplotlib.pyplot as plt

target_labels = [0, 5, 6]
subjects = ['s2.mat/S2_A1_E2.mat', 's3.mat/S3_A1_E2.mat', 's4.mat/S4_A1_E2.mat']
subject_names = ['Subject 2', 'Subject 3', 'Subject 4']

fig, axes = plt.subplots(3, 1, figsize=(12, 9))

for i, (path, name) in enumerate(zip(subjects, subject_names)):
    data = scipy.io.loadmat(path)
    emg = data['emg']
    labels = data['restimulus']
    mask = np.isin(labels, target_labels).flatten()
    emg_filtered = emg[mask]

    axes[i].plot(emg_filtered[:5000, 0])
    axes[i].set_title(f'Filtered EMG - {name}, Channel 1')
    axes[i].set_xlabel('Sample')
    axes[i].set_ylabel('Amplitude')

plt.tight_layout()
plt.savefig('emg_filtered_plot_subject234.png', dpi=150, bbox_inches='tight')
print("Saved emg_filtered_plot_subject234.png")