"""
Day 30 Activity: EDA Exercise

Tasks:

1) Load dataset

2) Run univariate, bivariate, and correlation analysis

3) Write 3 insights

"""

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt


# TODO: Load data from data/day30_eda.csv

df = pd.read_csv('Day 30 + CSV/day30_eda.csv')

# TODO: Perform basic EDA and write insights

sns.histplot(df['age'])


sns.scatterplot(data=df, x='income', y='spend', hue='segment')


sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# Income and spend have a perfect positive correlation.
# Segment C represents the highest earners and spenders.
# Spending increases linearly as age increases.