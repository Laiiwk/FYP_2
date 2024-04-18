import pandas as pd

def extract_error_features(input_path, output_path):
    """Reads processed error logs, extracts features, maps error levels, and saves the enhanced DataFrame.

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

    # Error Level Mapping
    error_level_map = {
        "php7:notice": 1,        
        "php7:warn": 2,  
        "php7:error": 3  # Add more mappings if needed
    }

    def map_error_level(error_level):
        return error_level_map.get(error_level, -1)  # -1 for unknown levels

    log_df['error_level_encoded'] = log_df['error_level'].apply(map_error_level) 

    # Feature engineering
    #log_df['error_message_length'] = log_df['error_message'].apply(len)

    # Drop redundant columns
    log_df = log_df.drop(columns=['timestamp','error_level','error_type', 'error_message','referer']) 
    log_df.to_csv(output_path + 'extracted_error_features.csv', index=False)

if __name__ == '__main__':
    input_path = 'output/processed_error_logs.csv'
    output_path = 'output/'
    extract_error_features(input_path, output_path)
