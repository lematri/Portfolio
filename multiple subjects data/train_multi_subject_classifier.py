import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load multi-subject train/test data
X_train = np.load('X_train_multi.npy')
y_train = np.load('y_train_multi.npy')
X_test = np.load('X_test_multi.npy')
y_test = np.load('y_test_multi.npy')

print("Training samples:", X_train.shape[0])
print("Test samples:", X_test.shape[0])

# Train Random Forest (your best model from before)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)

print(f"\nRandom Forest Accuracy (cross-subject): {rf_accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, rf_predictions, target_names=['Rest', 'Open Hand', 'Fist']))

# Confusion matrix
cm = confusion_matrix(y_test, rf_predictions)
plt.figure(figsize=(7, 6))
plt.imshow(cm, cmap='Blues')
plt.title('Confusion Matrix - Cross-Subject Test', pad=20)
plt.colorbar()
plt.xticks([0, 1, 2], ['Rest', 'Open Hand', 'Fist'])
plt.yticks([0, 1, 2], ['Rest', 'Open Hand', 'Fist'])
plt.xlabel('Predicted', labelpad=10)
plt.ylabel('Actual', labelpad=10)

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha='center', va='center', color='black', fontsize=12)

plt.tight_layout()
plt.savefig('confusion_matrix_multi_subject.png', dpi=150, bbox_inches='tight')
print("\nSaved confusion_matrix_multi_subject.png")