import pandas as pd
import numpy as np

# Load your data (replace with your CSV file)
df = pd.read_csv('output/extracted_error_features.csv')

# Option 1: Total Missing Value Counts per Column
print(df.isnull().sum())

# Option 2: Percentage of Missing Values per Column
print(df.isnull().sum() * 100 / len(df))

# Option 3: Boolean Matrix (True = Missing)
print(df.isnull())

# Option 4: Visualizing Missing Values (requires additional libraries)
import seaborn as sns 
import matplotlib.pyplot as plt

sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()