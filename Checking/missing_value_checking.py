import pandas as pd
import numpy as np

#Error Log
print("BELOW ARE ERROR LOG CHECKING")
df_error = pd.read_csv('output/extracted_error_features.csv')

print(df_error.isnull().sum())

print(df_error.isnull().sum() * 100 / len(df_error))

print(df_error.isnull())

#Access Log
print("BELOW ARE ACCESS LOG CHECKING")
df_access = pd.read_csv('output/extracted_access_features.csv')

print(df_access.isnull().sum())

print(df_access.isnull().sum() * 100 / len(df_access))

print(df_access.isnull())
