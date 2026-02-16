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

# TODO: Boxplot for score by group

plt.figure(figsize=(6, 4))
plt.boxplot(df["score"], vert=True, showfliers=True)
plt.title("Score — Boxplot"); plt.ylabel("Score")

plt.show()

df.boxplot(column="score"); plt.title("pandas boxplot")
plt.show()
sns.boxplot(x="group", y="score", data=df); plt.title("seaborn grouped")