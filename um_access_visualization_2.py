import pandas as pd
import seaborn as sns

# Load your extracted error and access logs
error_df = pd.read_csv('C:/um/output/extracted_error_features.csv')
access_df = pd.read_csv('C:/um/output/extracted_access_features.csv')

# Combine DataFrames (adding a log type column for clarity)
error_df['log_type'] = 'Error'
access_df['log_type'] = 'Access'
combined_df = pd.concat([error_df, access_df], ignore_index=True)

sns.lineplot(data=combined_df, x='timestamp', y='hour', hue='log_type') 