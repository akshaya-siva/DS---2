import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from catboost import CatBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the training data
train_df = pd.read_csv("train_data.csv")
X_train = train_df.drop('No-show', axis=1)
y_train = train_df['No-show']

# Load the testing data
test_df = pd.read_csv("test_data.csv")
X_test = test_df.drop('No-show', axis=1)
y_test = test_df['No-show']

# Preprocessing (if needed): Convert categorical features to numerical using one-hot encoding
X_train = pd.get_dummies(X_train, drop_first=True)
X_test = pd.get_dummies(X_test, drop_first=True)


# Align columns in case of mismatches
X_train, X_test = X_train.align(X_test, join='inner', axis=1)


# Train and evaluate models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),  # Increased max_iter
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "CatBoost": CatBoostClassifier(verbose=0),  # Set verbose to 0 to suppress output
    "Gradient Boosting": GradientBoostingClassifier()
}

results = {}

for name, model in models.items():
    print(f"Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = {
        "accuracy": accuracy,
        "classification_report": classification_report(y_test, y_pred)
    }
    print(f"{name} Accuracy: {accuracy}")
    print(f"{name} Classification Report:\n{classification_report(y_test, y_pred)}")
    print("-"*40)

# Print overall results (optional)
print("Overall Results:")
for name, result in results.items():
    print(f"{name}: Accuracy = {result['accuracy']}")
