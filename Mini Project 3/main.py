import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Mini Project 3/day35_project.csv')

# Univariate EDA

sns.histplot(data=df, x="age", kde=True)
plt.title('Age distribution')
plt.show()

# count plot
sns.countplot(data=df, x="segment")
plt.title('Count of each segment')
plt.show()

# Relationship EDA

# Scatter plot showing income vs spend
sns.scatterplot(data=df, x="income", y="spend")
plt.title('Income vs Spend')
plt.show()

# Boxplo
sns.boxplot(data=df, x="segment", y="spend")
plt.title('Spend by Segment')
plt.show()

# Faceted
sns.scatterplot(data=df, x="income", y="spend", hue="segment")
plt.title('Income vs Spend by Segment')
plt.show()