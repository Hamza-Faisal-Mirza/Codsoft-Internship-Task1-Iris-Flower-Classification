# -*- coding: utf-8 -*-
"""Codsoft-Task3-IRIS FLOWER CLASSIFICATION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1scLz5avZzTO0NpQyMm2mCyIkzVxeBwPU
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Load the data from the CSV file
data = pd.read_csv('IRIS.csv')

# Step 2: Data Preprocessing
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]  # Features
y = data['species']  # Target

# Encode the target variable into numerical values
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# Step 3: Data Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Model Selection and Training (Random Forest Classifier in this example)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Step 5: Model Evaluation
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=le.classes_)

print("Accuracy:", accuracy)
print("Classification Report:\n", report)

# Step 6: Make predictions on new data
new_data = pd.DataFrame({
    'sepal_length': [5.0],
    'sepal_width': [3.0],
    'petal_length': [1.5],
    'petal_width': [0.2]
})
new_predictions = clf.predict(new_data)
species = le.inverse_transform(new_predictions)
print("Predicted species for new data:", species)