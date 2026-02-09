#Day 18 Activity: Binning Practice

"""
Tasks:

1) Load age dataset

2) Apply equal-width bins, equal-frequency bins, and domain bins

3) One-hot encode bins and compare

"""

import pandas as pd

# TODO: Load data from data/day18_binning.csv

df = pd.read_csv('Day 18 + CSV/day18_binning.csv')

# pd.cut chooses boundaries based on min/max - may not align with meaningful ages

bin_edges = [0, 18, 35, 50, 100]
labels = ["Child", "YoungAdult", "Adult", "Senior"]
df["age_bins_width"] = pd.cut(df["age"], bins=bin_edges, labels=labels, right=False)

# TODO: Apply pd.cut and pd.qcut

df["age_bin_3"] = pd.cut(df["age"], bins=3)
print(df[["age", "age_bin_3"]].head())

# TODO: Create domain bins

age_edges = [0, 13, 18, 65, 120]
age_labels = ["Child", "Teen", "Adult", "Senior"]
df["age_group"] = pd.cut(df["age"], bins=age_edges, labels=age_labels, right=False)
print(df["age_group"].value_counts())

# TODO: Compare value counts

print(df["age_bins_width"].value_counts())