"""

Day 19 Activity: Transformation Practice

Tasks:

1) Load skewed feature

2) Apply log1p, sqrt, and Yeo-Johnson

3) Compare before/after

"""

import matplotlib.pyplot as plt
 
import seaborn as sns

import pandas as pd

import numpy as np

from sklearn.preprocessing import PowerTransformer

 

# TODO: Load data from data/day19_transform.csv

df = pd.read_csv('Day 19 + CSV/day19_transform.csv')

# TODO: Apply transforms and compare summary stats

print(df["spend"].describe()) 
sns.histplot(df["spend"], kde=True)
plt.show()