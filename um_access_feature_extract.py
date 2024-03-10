import re
import pandas as pd

def extract_access_features(input_path, output_path):
  """Reads processed access logs, extracts features, and saves the enhanced DataFrame.

  Args:
      input_path (str): Path to the processed access log CSV file.
      output_path (str): Path to save the DataFrame with extracted features.
  """ 

  log_df = pd.read_csv(input_path) # Assuming a processed CSV already exists

  # Convert timestamp to datetime format
  log_df['timestamp'] = pd.to_datetime(log_df['timestamp'], format='%d/%b/%Y:%H:%M:%S %z') 

  # Extract features from timestamp
  log_df['hour'] = log_df['timestamp'].dt.hour
  log_df['day'] = log_df['timestamp'].dt.day
  log_df['month'] = log_df['timestamp'].dt.month
  log_df['year'] = log_df['timestamp'].dt.year

  # Request Categorization
  log_df['request_method'] = log_df['request'].apply(lambda x: x.split()[0])
  log_df['request_path'] = log_df['request'].apply(lambda x: x.split()[1]) 

  # Ensure data type conversions (if necessary)
  try:
      log_df['status_code'] = log_df['status_code'].astype(int) 
      log_df['size'] = log_df['size'].astype(int)
  except ValueError:
      pass  # Handle potential errors if conversions are not possible

  # Drop unnecessary columns (adjust if you want to keep some)
  log_df = log_df.drop(columns=['request'])

  log_df.to_csv(output_path + 'extracted_access_features.csv', index=False)

if __name__ == '__main__':
  input_path = 'output/processed_access_logs.csv'
  output_path = 'output/'
  extract_access_features(input_path, output_path)
