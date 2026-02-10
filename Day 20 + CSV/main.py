"""
Day 20 Activity: Integrated Feature Engineering

Tasks:

1) Load dataset

2) Encode categoricals, scale numerics

3) Add interaction and transformed feature

4) Compare baseline vs engineered features

""" 
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv('Day 20 + CSV/day20_integration.csv')

# Create target variable (binary: high spend)
df["converted"] = (df["basket_value"] > df["basket_value"].median()).astype(int)

df["pages_per_min"] = df["pages_viewed"] / (df["session_minutes"] + 1e-3)

df["is_mobile_high_spend"] = (
    ((df["device_type"] == "mobile") &
     (df["basket_value"] > df["basket_value"].median()))
    .astype(int)
)

target = "converted"

cat_features = ["device_type", "city"]

num_features_baseline = [
    "session_minutes",
    "pages_viewed",
    "basket_value"
]

num_features_engineered = num_features_baseline + [
    "pages_per_min",
    "is_mobile_high_spend"
]

preprocess_baseline = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_features_baseline),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
    ]
)

preprocess_engineered = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_features_engineered),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
    ]
)

X = df.drop(columns=[target])
y = df[target]

baseline_pipe = Pipeline([
    ("prep", preprocess_baseline),
    ("model", LogisticRegression(max_iter=1000))
])

engineered_pipe = Pipeline([
    ("prep", preprocess_engineered),
    ("model", LogisticRegression(max_iter=1000))
])

baseline_score = cross_val_score(
    baseline_pipe, X, y, cv=2, scoring="roc_auc"
).mean()

engineered_score = cross_val_score(
    engineered_pipe, X, y, cv=2, scoring="roc_auc"
).mean()

print(f"Baseline ROC-AUC: {baseline_score:.3f}")
print(f"Engineered ROC-AUC: {engineered_score:.3f}")

# TODO: Load data from data/day20_integration.csv

# TODO: Build engineered features

# TODO: Compare baseline vs engineered (summary stats or model)

