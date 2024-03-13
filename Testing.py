import pandas as pd
import matplotlib.pyplot as plt

error_df = pd.read_csv('C:/um/output/extracted_error_features.csv') 

# Check for missing values
print(error_df.isnull().sum())

# Verify unique values in each column
print(error_df['error_file'].nunique())
print(error_df['error_type_encoded'].nunique())

# Create the crosstabulation 
ct = pd.crosstab(error_df['error_file'], error_df['error_type_encoded'])

# Check if the crosstab is mostly empty
print((ct == 0).astype(int).sum().sum()) # Total number of zero values

# Try visualizing
ct.plot(kind='bar', stacked=True) 
plt.xlabel('Resource / File')
plt.ylabel('Error Count')
plt.title('Error Distribution by Resource and Type')
plt.show()
