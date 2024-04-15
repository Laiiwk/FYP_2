import pandas as pd

# Define the date range of interest
start_date = '2023-03-01'
end_date = '2023-05-31'

# Filtering Function
def filter_by_date_range(df, date_column, start_date, end_date):
    """Filters a DataFrame by a date column within a specified range."""
    return df[(df[date_column] >= start_date) & (df[date_column] <= end_date)]

# --- Access Log Filtering ---
# Load the access log
df_access = pd.read_csv('output/extracted_access_features.csv', 
                        parse_dates=['timestamp'])  # Ensure correct type parsing
# Assuming your date information is within the 'timestamp' column
filtered_df_access = filter_by_date_range(df_access, 'timestamp', start_date, end_date)
filtered_df_access.to_csv('output/reduced_access_Mar_May_2023.csv', index=False)

# --- Error Log Filtering ---
# Load the error log
df_error = pd.read_csv('output/extracted_error_features.csv',
                       parse_dates=['timestamp'])  # Replace 'timestamp' if needed
# Assuming your  date is also in the 'timestamp' column
filtered_df_error = filter_by_date_range(df_error, 'timestamp', start_date, end_date) 
filtered_df_error.to_csv('output/reduced_error_Mar_May_2023.csv', index=False)