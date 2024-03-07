import re
import pandas as pd
import re


def read_and_preprocess_error_log(input_path, output_path):
    """Reads error logs, extracts relevant fields, and saves a processed DataFrame.

    Args:
        input_path (str): Path to the error input_data file.
        output_path (str): Path to save the processed DataFrame.
    """

    pattern = r'\[(.*?)\] \[(.*?)\] \[pid (.*?)\] \[client (.*?):(.*?)\] (.*?): (.*?) in (.*?) on line (.*?), referer: (.*?)'
    logs = []

    with open(input_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                logs.append({
                    "timestamp": match.group(1),
                    "error_level": match.group(2),
                    "pid": match.group(3),
                    "client_ip": match.group(4),
                    "client_port": match.group(5),
                    "error_type": match.group(6),
                    "error_message": match.group(7),
                    "error_file": match.group(8),
                    "error_line": match.group(9),
                    "referer": match.group(10)
                })

    log_df = pd.DataFrame(logs)
    log_df.to_csv(output_path + 'processed_error_logs.csv', index=False)

if __name__ == '__main__':
    input_path = 'C:/um/input_data/umexpert_error_log.txt'
    output_path = 'C:/um/output/'
    read_and_preprocess_error_log(input_path, output_path)



