"""
Day 29 Activity: Correlations

Tasks:

1) Compute correlation matrix

2) Plot heatmap

3) Plot scatter plots for strong/weak pairs
"""

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

# TODO: Load data from data/day29_correlations.csv

df = pd.read_csv('Day 29 + CSV/day29_correlations.csv')

# TODO: Compute corr and plot heatmap

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Corr Hmap')
plt.show()

# TODO: Scatter plots for key pairs

sns.scatterplot(data=df, x='feature_x', y='target')
plt.title('Pcorr')
plt.show()

sns.scatterplot(data=df, x='feature_z', y='target')
plt.title('NCorr')
plt.show()