import pandas as pd

# --- Access Log Filtering ---
start_date = '2023-03-01'
end_date = '2023-05-31'

df_access = pd.read_csv('output/extracted_access_features.csv')

# Filter based on year, month, day columns
df_access_filtered = df_access[(df_access['year'] == 2023) &
                               (df_access['month'] >= 3) & 
                               (df_access['month'] <= 5)]

df_access_filtered.to_csv('output/filtered_access_features.csv', index=False)

# --- Error Log Filtering ---
# We need the name of the equivalent column for dates in your error log
error_log_date_column = '...'  # Replace '...' with the actual column name

df_error = pd.read_csv('output/extracted_error_features.csv')

df_error_filtered = df_error[(df_error['year'] == 2023) &
                             (df_error['month'] >= 3) & 
                             (df_error['month'] <= 5)]

df_error_filtered.to_csv('output/filtered_error_features.csv', index=False)

print("Filtering complete!")
