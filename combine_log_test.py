import pandas as pd

# Load the DataFrames
df_access = pd.read_csv('output/filtered_access_features.csv')
df_error = pd.read_csv('output/filtered_error_features.csv')

# Combine logs (inner join) with suffixes, and then remove 'client_ip'
df_combined = pd.merge(df_access, df_error, 
                       on=['hour', 'day', 'month', 'year'], 
                       how='inner', 
                       suffixes=('_access', '_error'))  # Prevent column name conflicts

# Save the combined DataFrame 
df_combined.to_csv('output/combined_data.csv', index=False) 
print("Combined data saved to 'combined_data.csv'")