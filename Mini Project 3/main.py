import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df = pd.read_csv('Mini Project 3/day35_project.csv')

df_features = df.copy()
df_features["price_per_sqft"] = df["price"] / df["sqft"].replace({0: np.nan})
df_features["price_per_sqft"] = df_features["price_per_sqft"].fillna(df_features["price_per_sqft"].median())
df_features["revenue_per_user"] = df["price"] / df["rooms"].replace({0: np.nan})

numeric_features = ["price", "rooms", "price_per_sqft", "revenue_per_user"]

X = df_features[numeric_features]
y = df_features["sqft"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

preprocess = ColumnTransformer(
    transformers=[
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]), numeric_features)
    ]
)

final_model = Pipeline([
    ("preprocess", preprocess),
    ("model", RandomForestRegressor(random_state=0))
])

final_model.fit(X_train, y_train)
print("R²:", r2_score(y_test, final_model.predict(X_test)))