import sqlite3
import pandas as pd

# Create or connect to database file 
conn = sqlite3.connect('my_merged_data.db') 

df_access = pd.read_csv('output/extracted_access_features.csv')
df_error = pd.read_csv('output/extracted_error_features.csv')

df_access.to_sql('access_data', conn, if_exists='replace')  
df_error.to_sql('error_data', conn, if_exists='replace')  

# Chunking parameters
chunk_size = 100000 
offset = 0

# Initialize an empty DataFrame to store chunks
result_df = pd.DataFrame()  

while True:  # Loop to fetch chunks
    sql_query = f"""  
    SELECT access_data.*, error_data.* FROM access_data  
    INNER JOIN error_data ON
    access_data.client_ip = error_data.client_ip AND 
    access_data.day = error_data.day AND
    access_data.month = error_data.month AND
    access_data.year = error_data.year
    LIMIT {chunk_size} OFFSET {offset} 
    """

    chunk_df = pd.read_sql_query(sql_query, conn)

    if chunk_df.empty:  # Stop when a query returns no more rows
        break

    result_df = pd.concat([result_df, chunk_df])
    offset += chunk_size

# Save the final, combined result
result_df.to_csv('output/combined_data.csv', index=False) 