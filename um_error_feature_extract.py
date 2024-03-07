import pandas as pd
from sklearn.preprocessing import LabelEncoder

def extract_error_features(input_path, output_path):
    """Reads processed error logs, extracts features, and saves the enhanced DataFrame.

    Args:
        input_path (str): Path to the processed error input_data CSV file.
        output_path (str): Path to save the DataFrame with extracted features.
    """

    log_df = pd.read_csv(input_path)

    # Convert timestamp to datetime format
    log_df['timestamp'] = pd.to_datetime(log_df['timestamp'], format='%a %b %d %H:%M:%S.%f %Y')

    # Extract time-based features
    log_df['hour'] = log_df['timestamp'].dt.hour
    log_df['day'] = log_df['timestamp'].dt.day
    log_df['month'] = log_df['timestamp'].dt.month
    log_df['year'] = log_df['timestamp'].dt.year

    # Feature engineering
    le = LabelEncoder()
    log_df['error_level_encoded'] = le.fit_transform(log_df['error_level'])
    log_df['error_type_encoded'] = le.fit_transform(log_df['error_type'])
    log_df['error_message_length'] = log_df['error_message'].apply(len)

    # Drop redundant columns
    log_df = log_df.drop(columns=['timestamp', 'error_level', 'error_type', 'error_message'])

    log_df.to_csv(output_path + 'extracted_error_features.csv', index=False)

if __name__ == '__main__':
    input_path = 'C:/um/output/processed_error_logs.csv'
    output_path = 'C:/um/output/'
    extract_error_features(input_path, output_path)
