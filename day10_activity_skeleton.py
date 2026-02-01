"""
Day 10 Activity: Outliers Practice
Tasks:
1) Implement IQR-based outlier detection
2) Implement z-score detection
3) Compare strategies: no handling, IQR capping, log1p transform
"""

import numpy as np
import pandas as pd

# Sample heavy-tailed data
np.random.seed(10)
values = np.concatenate([np.random.lognormal(10, 0.5, 1000), [1e7, 2e7]])

df = pd.DataFrame({"income": values})

def iqr_bounds(s, k=1.5):
 q1, q3 = s.quantile(0.25), s.quantile(0.75)
 iqr = q3 - q1
 return q1 - k * iqr, q3 + k * iqr
lower, upper = iqr_bounds(df["income"], k=1.5)
mask_iqr = (df({'income'}) < lower) | (df({'income'}) > upper)

def detect_outliers_iqr(df, col, k=1.5):
 lower, upper = (df({'income'}), k==k)
 return (df[col] < lower) | (df[col] > upper)

lower, upper = iqr_bounds(df({"income"}), k=1.5)

df_capped = df.copy()

df_capped["income_capped"] = df_capped["income"].clip(lower=lower, upper=upper)

# TODO: Implement iqr_bounds and detect_outliers_iqr
# TODO: Implement detect_outliers_zscore
# TODO: Apply capping and log1p transformation
