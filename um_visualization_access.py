import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Traffic by Hour (Access Logs)
access_df = pd.read_csv('output/extracted_access_features.csv')
access_df.groupby('hour')['timestamp'].count().plot(kind='bar')
plt.xlabel('Hour of Day')
plt.ylabel('Request Count')
plt.title('Access Log Traffic Pattern by Hour')
plt.show()

pivot_df = access_df.pivot_table(index='hour', columns='day', values='timestamp', aggfunc='count')
sns.heatmap(pivot_df, cmap='coolwarm') # Choose a colormap
plt.title('Traffic Density Heatmap: Hour vs. Day')
plt.show()

access_df['request_method'].value_counts().plot(kind='bar') 
plt.title('Distribution of Request Methods')
plt.show()

top_resources = access_df['request_path'].value_counts().head(10) # Adjust the number
top_resources.plot(kind='bar')
plt.title('Top 10 Requested Resources')
plt.show() 

access_df['referer'].value_counts().head(15).plot(kind='pie') # Adjust number 
plt.title('Referrer Distribution')
plt.show()

