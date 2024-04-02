import pandas as pd
import numpy as np

def handle_missing_values(df, df_name):
    missing_counts = df.isnull().sum()
    print(f"\nMissing Value Counts for '{df_name}':\n{missing_counts}")

    if missing_counts.any():  # Only prompt if missing values exist
        delete_choice = input("Delete rows with missing values (Y/N)? ").lower()
        if delete_choice == 'y':
            before_deletion = len(df)
            df.dropna(inplace=True)  # Delete rows with missing values in-place
            after_deletion = len(df)
            affected_rows = before_deletion - after_deletion
            print(f"{affected_rows} rows were deleted.")
            print(f"{after_deletion} rows remain.")
        else:
            print("Rows with missing values will be kept.")

# Error Log Handling
print("ERROR LOG CHECKING")
df_error = pd.read_csv('output/extracted_error_features.csv')
handle_missing_values(df_error, 'Error Log')

# Access Log Handling
print("\nBELOW ARE FOR ACCESS LOG CHECKING")
df_access = pd.read_csv('output/extracted_access_features.csv')
handle_missing_values(df_access, 'Access Log')
