import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have 'extracted_error_features.csv' and 'extracted_access_features.csv'

# Traffic by Hour (Access Logs)
access_df = pd.read_csv('C:/um/output/extracted_access_features.csv')
access_df.groupby('hour')['timestamp'].count().plot(kind='bar')
plt.xlabel('Hour of Day')
plt.ylabel('Request Count')
plt.title('Access Log Traffic Pattern by Hour')
plt.show()

# Traffic by Day (Error Logs)
error_df = pd.read_csv('C:/um/output/extracted_error_features.csv')
error_df.groupby('day')['timestamp'].count().plot()  # Kind='line' for line chart
plt.xlabel('Day of Month')
plt.ylabel('Error Count')
plt.title('Error Log Traffic Pattern by Day')
plt.show()

# Using Seaborn for enhanced visualization
sns.histplot(access_df, x='hour', bins=24, kde=True) 
plt.title('Access Log Traffic Distribution')
plt.show()
