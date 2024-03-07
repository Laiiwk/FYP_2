import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Load your data (assuming it's the enhanced access log DataFrame)
log_df = pd.read_csv('C:/um/output/extracted_access_features.csv') 

# Traffic Patterns Over Time (Line Plots)
sns.lineplot(x='hour', y='request_method', hue='day', data=log_df)
plt.title("Request Count by Method and Hour of Day")  
plt.show()

sns.lineplot(x='month', y='request_method', hue='year', data=log_df)
plt.title("Request Count by Method and Month")
plt.show()

# Heatmap (Density of Requests)
df_heatmap = log_df.pivot_table(index='hour', columns='day', values='request_method', aggfunc='count')
sns.heatmap(df_heatmap)
plt.title("Request Density - Hour vs Day of Week")
plt.show()
