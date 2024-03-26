import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Load your data 
log_df = pd.read_csv('output/extracted_access_features.csv') 

# Traffic Patterns Over Time (Line Plots)
sns.lineplot(x='hour', y='request_method', hue='day', data=log_df)
plt.title("Request Count by Method and Hour of Day")  
plt.show()

# Heatmap (Density of Requests)
df_heatmap = log_df.pivot_table(index='hour', columns='day', values='request_method', aggfunc='count')
sns.heatmap(df_heatmap)
plt.title("Request Density - Hour vs Day of Week")
plt.show()
