"""

Day 27 Activity: Histograms & Boxplots

Tasks:

1) Plot histogram for numeric variable

2) Plot boxplot for numeric by category

3) Compare group distributions

"""

 

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

 

# TODO: Load data from data/day27_boxplots.csv


df = pd.read_csv('Day 27 + CSV/day27_boxplots.csv')
 

# TODO: Histogram for score

df["score"].hist(label = 'Histogram')

plt.show()

# TODO: Boxplot for score by group

plt.boxplot(df["score"], vert=True, showfliers=True)
df.boxplot(column="score"); plt.title("pandas boxplot")
plt.title("Score — Boxplot"); plt.ylabel("Score")

plt.show()

