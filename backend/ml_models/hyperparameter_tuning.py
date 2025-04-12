
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from catboost import CatBoostClassifier
from scipy.stats import uniform, randint

def tune_logistic_regression(X_train, y_train):
    param_dist = {
        'C': uniform(0.1, 10),
        'penalty': ['l1', 'l2'],
        'solver': ['liblinear', 'saga']
    }
    model = LogisticRegression(class_weight='balanced', max_iter=1000)
    return RandomizedSearchCV(model, param_distributions=param_dist, n_iter=5, cv=3, scoring='f1_macro', random_state=42).fit(X_train, y_train)

def tune_decision_tree(X_train, y_train):
    param_dist = {
        'max_depth': randint(2, 10),
        'min_samples_split': randint(2, 20),
        'min_samples_leaf': randint(1, 10)
    }
    model = DecisionTreeClassifier(class_weight='balanced', random_state=42)
    return RandomizedSearchCV(model, param_distributions=param_dist, n_iter=5, cv=3, scoring='f1_macro', random_state=42).fit(X_train, y_train)

def tune_random_forest(X_train, y_train):
    param_dist = {
        'n_estimators': randint(50, 200),
        'max_depth': randint(10, 50),
        'min_samples_split': randint(2, 20),
        'min_samples_leaf': randint(1, 10)
    }
    model = RandomForestClassifier(class_weight='balanced', random_state=42)
    return RandomizedSearchCV(model, param_distributions=param_dist, n_iter=5, cv=3, scoring='f1_macro', random_state=42).fit(X_train, y_train)

def tune_catboost(X_train, y_train):
    param_dist = {
        'iterations': randint(100, 500),
        'learning_rate': uniform(0.01, 0.3),
        'depth': randint(4, 10),
        'l2_leaf_reg': randint(1, 10)
    }
    model = CatBoostClassifier(verbose=0, random_state=42)
    return RandomizedSearchCV(model, param_distributions=param_dist, n_iter=5, cv=3, scoring='f1_macro', random_state=42).fit(X_train, y_train)

def tune_gradient_boosting(X_train, y_train):
    param_dist = {
        'n_estimators': randint(50, 200),
        'learning_rate': uniform(0.01, 0.3),
        'max_depth': randint(3, 10),
        'min_samples_split': randint(2, 20),
        'min_samples_leaf': randint(1, 10)
    }
    model = GradientBoostingClassifier(random_state=42)
    return RandomizedSearchCV(model, param_distributions=param_dist, n_iter=5, cv=3, scoring='f1', random_state=42).fit(X_train, y_train)
