import pandas as pd
from tqdm import tqdm

def process_in_chunks(df1, df2, chunksize=100000):
    """
    Processes DataFrames in chunks and merges them.

    Args:
        df1 (pd.DataFrame): First DataFrame.
        df2 (pd.DataFrame): Second DataFrame.
        chunksize (int, optional): Chunk size for processing. Defaults to 100000.

    Returns:
        pd.DataFrame: Merged DataFrame.
    """

    all_merged_df = []
    num_chunks = int((len(df1) - 1) // chunksize) + 1
    for i in tqdm(range(num_chunks), desc="Processing Chunks"):
        start_idx = i * chunksize
        end_idx = min((i + 1) * chunksize, len(df1))
        chunk_df1 = df1.iloc[start_idx:end_idx]
        chunk_df2 = df2.iloc[start_idx:end_idx]

        # Merge chunks
        merged_df = pd.merge(chunk_df1, chunk_df2, on=['hour', 'day', 'month'], how='inner', suffixes=('_access', '_error'))

        all_merged_df.append(merged_df)

    # Concatenate all merged chunks
    return pd.concat(all_merged_df)


# Load the DataFrames (replace with your actual loading logic)
df_access = pd.read_csv('output/filtered_access_features.csv')
df_error = pd.read_csv('output/filtered_error_features.csv')

# Process and merge in chunks
df_combined = process_in_chunks(df_access, df_error)

# Save the combined DataFrame 
df_combined.to_csv('output/combined_data.csv', index=False) 
print("Combined data saved to 'combined_data.csv'")
