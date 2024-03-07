import re
import pandas as pd

def read_and_preprocess_access_log(input_path, output_path):
    """Reads access logs, extracts relevant fields, and saves a processed DataFrame.

    Args:
        input_path (str): Path to the access input_data file.
        output_path (str): Path to save the processed DataFrame.
    """

    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (.*?) (.*?) \[(.*?)\] "(.*?)" (\d{3}) (\d+) "(.*?)" "(.*?)"'
    logs = []

    with open(input_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                logs.append({
                    "client_ip": match.group(1),
                    "server_ip": match.group(2),
                    "user_identifier": match.group(3),
                    "userid": match.group(4),
                    "timestamp": match.group(5),
                    "request": match.group(6),
                    "status_code": match.group(7),
                    "size": match.group(8),
                    "referer": match.group(9),
                    "user_agent": match.group(10)
                })

    log_df = pd.DataFrame(logs)
    log_df.to_csv(output_path + 'processed_access_logs.csv', index=False)

if __name__ == '__main__':
    input_path = 'C:/um/input_data/umexpert_access_log.txt'
    output_path = 'C:/um/output/'
    read_and_preprocess_access_log(input_path, output_path)
