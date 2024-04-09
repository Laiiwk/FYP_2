import pandas as pd

# Load your access log data
df_access = pd.read_csv('output/extracted_access_features.csv')

def delete_rows_with_empty_values(df):
    column_to_clean = input("Enter the column name where you want to delete empty values: ")

    if column_to_clean not in df.columns:
        print(f"Error: Column '{column_to_clean}' not found in the DataFrame.")
        return

    original_rows = len(df)
    df.dropna(subset=[column_to_clean], inplace=True)
    affected_rows = original_rows - len(df)

    print(f"\n{affected_rows} rows with empty values in '{column_to_clean}' deleted. {len(df)} rows remaining.")
    
    # Save the cleaned DataFrame (if changes were made)
    if affected_rows:
        df.to_csv('output/extracted_access_features.csv', index=False)
        print("File updated.")
    else:
        print("No changes made to the file.")

    return affected_rows  # Indicates if changes were made

# Main code execution
modified = delete_rows_with_empty_values(df_access.copy())


