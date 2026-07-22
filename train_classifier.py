import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load the features and labels saved from preprocessing
features = np.load('features.npy')
labels = np.load('labels.npy')

print("Features shape:", features.shape)
print("Labels shape:", labels.shape)

# Split into train/test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42, stratify=labels
)

print("\nTraining samples:", X_train.shape[0])
print("Test samples:", X_test.shape[0])

# --- Train an SVM classifier ---
svm_model = SVC(kernel='rbf', C=1.0)
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_test)
svm_accuracy = accuracy_score(y_test, svm_predictions)

print(f"\nSVM Accuracy: {svm_accuracy:.2%}")

# --- Train a Random Forest classifier for comparison ---
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)

print(f"Random Forest Accuracy: {rf_accuracy:.2%}")

# --- Pick the better model and show detailed results ---
best_model_name = "SVM" if svm_accuracy >= rf_accuracy else "Random Forest"
best_predictions = svm_predictions if svm_accuracy >= rf_accuracy else rf_predictions

print(f"\nBest model: {best_model_name}")
print("\nClassification Report:")
print(classification_report(y_test, best_predictions, target_names=['Rest', 'Open Hand', 'Fist']))

# --- Confusion matrix ---
cm = confusion_matrix(y_test, best_predictions)
plt.figure(figsize=(7, 6))
plt.imshow(cm, cmap='Blues')
plt.title(f'Confusion Matrix - {best_model_name}')
plt.colorbar()
plt.xticks([0, 1, 2], ['Rest', 'Open Hand', 'Fist'])
plt.yticks([0, 1, 2], ['Rest', 'Open Hand', 'Fist'])
plt.xlabel('Predicted')
plt.ylabel('Actual')

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha='center', va='center', color='black')

plt.savefig('confusion_matrix.png')
print("\nConfusion matrix saved as confusion_matrix.png")