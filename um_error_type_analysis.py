import pandas as pd

# Apply fix for DtypeWarning (if needed)
error_df = pd.read_csv('output/extracted_error_features.csv', dtype={'column_0': str, 'column_4': int})  

# Create a nested dictionary to store results
results = {}

# Group by file, then by error type
for file, file_group in error_df.groupby(['error_file', 'error_type_encoded']):
    error_file, error_type = file 

    # Initialize nested structure if needed
    if error_file not in results:
        results[error_file] = {} 

    results[error_file][error_type] = file_group.size 

# Convert to DataFrame (rest of the code is very similar)
output_df = pd.DataFrame.from_dict(results, orient='index')
output_df = output_df.fillna(0).astype(int)

# Assuming your error types are numeric, ensure consistent ordering
unique_error_types = error_df['error_type_encoded'].unique()
output_df = output_df.reindex(columns=unique_error_types) 

output_df.to_csv('output/error_type_analysis.csv', index=True, index_label='File Name') 
