# 📘 Hackathon Notebook: Medical No-Show Appointments - Data Preparation

# ✅ Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# ✅ Step 2: Load Dataset
df = pd.read_csv("KaggleV2-May-2016.csv")  # Replace with actual file path

# ✅ Step 3: Exploratory Data Analysis (EDA)
print("\n🔍 Dataset Overview:")
print(df.head())
print("\n📏 Shape of dataset:", df.shape)
print("\n🧼 Missing values:")
print(df.isnull().sum())
print("\n🔢 Data types:")
print(df.dtypes)

# Distribution of target variable
sns.countplot(x='No-show', data=df)
plt.title("Distribution of No-show")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# ✅ Step 4: Clean 'No-show' Column
# Normalize formatting
df['No-show'] = df['No-show'].astype(str).str.strip().str.lower()

# Convert to binary labels
df['No-show'] = df['No-show'].replace({'yes': 1, 'no': 0})

# Drop rows where conversion failed (if any)
df = df[df['No-show'].notnull()]

# ✅ Step 5: Drop Unnecessary Columns
cols_to_drop = ['PatientId', 'AppointmentID']
df = df.drop(cols_to_drop, axis=1, errors='ignore')

# ✅ Step 6: Train-Test Split (Stratified 80/20)
X = df.drop('No-show', axis=1)
y = df['No-show']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# ✅ Step 7: Save Outputs
# Full cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)
df.to_pickle("cleaned_dataset.pkl")

# Training and testing sets
train_df = X_train.copy()
train_df['No-show'] = y_train
train_df.to_csv("train_data.csv", index=False)

test_df = X_test.copy()
test_df['No-show'] = y_test
test_df.to_csv("test_data.csv", index=False)

# ✅ Step 8: Data Validation
# 1. Check for data leakage
overlap = pd.merge(X_train, X_test, how='inner')
print("\n🔍 Overlapping rows between train and test sets:", len(overlap))

# 2. Class balance check
print("\n📊 Class distribution:")
print("Full dataset:", y.value_counts(normalize=True))
print("Train set:", y_train.value_counts(normalize=True))
print("Test set:", y_test.value_counts(normalize=True))

# ✅ Step 9: (Optional) Visualize Class Balance
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Full Dataset")

plt.subplot(1, 3, 2)
sns.countplot(x=y_train)
plt.title("Training Set")

plt.subplot(1, 3, 3)
sns.countplot(x=y_test)
plt.title("Test Set")

plt.tight_layout()
plt.show()
