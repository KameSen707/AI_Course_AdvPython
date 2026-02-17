"""
Day 28 Activity: Grouping & Aggregation

Tasks:

1) Load dataset

2) Compute groupby summaries

3) Plot aggregated metric
"""

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

# TODO: Load data from data/day28_groupby.csv

df = pd.read_csv ('Day 28 + CSV/day28_groupby.csv')

# TODO: Group by region and segment

groups = df.groupby(['region', 'segment'])['sales'].mean().reset_index()
print(groups)

# TODO: Plot mean sales by region

sns.barplot(data=groups, x='region', y='sales', hue='segment')
plt.title('Average Sales by Region')
plt.show()