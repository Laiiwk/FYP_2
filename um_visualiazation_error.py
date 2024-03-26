import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

error_df = pd.read_csv('output/extracted_error_features.csv') 

# Group errors by day and error type
daily_error_breakdown = error_df.groupby(['day', 'error_type_encoded']).size().unstack()

# Plot with multiple lines (one for each error type)
daily_error_breakdown.plot() 
plt.xlabel('Day of Month')
plt.ylabel('Error Count')
plt.title('Errors by Day and Error Type')
plt.show()

# Assuming you have a 'user_agent' column (if not, disregard this example)
error_df['client_ip'].value_counts().head(10).plot(kind='bar')
plt.xlabel('Client IP')
plt.ylabel('Error Count')
plt.title('Top 10 Client IPs with Errors')
plt.show()

error_df['error_file'].value_counts().head(15).plot(kind='bar')
plt.xlabel('Error File')
plt.ylabel('Error Count')
plt.title('Top 15 Error-Prone Resources')
plt.xticks(rotation=90)  # Rotate labels if they overlap
plt.show()

ct = pd.crosstab(error_df['error_file'], error_df['error_type_encoded'])
sns.heatmap(ct, cmap='viridis', annot=True)  # annot=True to display counts in cells 
plt.title('Heatmap of Error Distribution')
plt.show()

#testing