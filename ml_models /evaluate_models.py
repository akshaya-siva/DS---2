
import pickle
from sklearn.metrics import classification_report, accuracy_score

def evaluate_models(model_paths, X_test, y_test):
    for name, path in model_paths.items():
        with open(path, 'rb') as f:
            model = pickle.load(f)
        y_pred = model.predict(X_test)
        print(f"\n{name} Performance:")
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print(classification_report(y_test, y_pred))
