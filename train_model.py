import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import pickle

# Simulated CBC data
np.random.seed(42)
num_samples = 5000
X = pd.DataFrame({
    'hemoglobin': np.random.normal(13.5, 1.5, num_samples),
    'hematocrit': np.random.normal(40, 4, num_samples),
    'mcv': np.random.normal(90, 8, num_samples),
    'mch': np.random.normal(30, 3, num_samples),
    'rdw': np.random.normal(13, 1.2, num_samples)
})

# Classes: 0 = No Anemia, 1 = Iron Deficiency, 2 = Vitamin Deficiency
y = np.random.choice([0, 1, 2], size=num_samples, p=[0.6, 0.25, 0.15])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# SMOTE for class balancing
smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Feature scaling
scaler = StandardScaler()
X_resampled_scaled = scaler.fit_transform(X_resampled)
X_test_scaled = scaler.transform(X_test)

# Model training
model = GradientBoostingClassifier()
scores = cross_val_score(model, X_resampled_scaled, y_resampled, cv=5)
print(f"Cross-validated accuracy: {scores.mean():.4f}")

model.fit(X_resampled_scaled, y_resampled)

# Save model
with open('anemia_model.pkl', 'wb') as f:
    pickle.dump(model, f)
