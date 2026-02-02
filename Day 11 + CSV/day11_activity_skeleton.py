"""
Day 11 Activity: Outlier Strategies
Tasks:
1) Load numeric data with outliers
2) Implement percentile capping (winsorization)
3) Implement removal strategy
4) Compare summary stats before/after
"""

import pandas as pd
import numpy as np

df11 = pd.read_csv ('Day 11 + CSV/day11_income.csv')

def winsorize_series(s: pd.Series, lower_q=0.01, upper_q=0.99) -> pd.Series:
 lower, upper = s.quantile(lower_q), s.quantile(upper_q)
 return s.clip(lower=lower, upper=upper)
df11["income_cap_1_99"] = winsorize_series(df11["income"], 0.01, 0.99)


upper_99 = df11["income"].quantile(0.99)
mask_keep = df11["income"] <= upper_99
df11_removed = df11[mask_keep].copy()
print("Original rows:", len(df11), "After removal:", len(df11_removed))

                    


# TODO: Load data from data/day11_income.csv done
# df = pd.read_csv(...)

# TODO: Implement winsorize_series(s, lower_q, upper_q)
# TODO: Implement remove_upper_tail(s, upper_q)
# TODO: Compare summary stats and print results