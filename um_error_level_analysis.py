import pandas as pd

# Apply fix for DtypeWarning
error_df = pd.read_csv('output/extracted_error_features.csv', dtype={'column_0': str, 'column_4': int})  

# Create a nested dictionary to store results
results = {}

# Group by file, then by error level
for file, file_group in error_df.groupby(['error_file', 'error_level_encoded']):
    error_file, error_level = file
    if error_file not in results:
        results[error_file] = {}
    results[error_file][error_level] = file_group.size 

# Convert nested dictionary to DataFrame
output_df = pd.DataFrame.from_dict(results, orient='index')

# Fill missing error levels with 0
output_df = output_df.fillna(0).astype(int)

# Ensure consistent ordering of error level columns 
output_df = output_df.reindex(columns=[1, 2, 3, 4]) 

# Save as a CSV file
output_df.to_csv('output/error_level_analysis.csv', index=True, index_label='File Name') 
