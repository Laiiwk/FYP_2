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


# Select errors where the error_file matches the target resource
kpi_errors = error_df[error_df['error_file'] == '/var/www/html/umexpertv3/class/class.KpiHelperTeachingNew.php']

# Count the number of errors (assuming 'error_type_encoded' holds the encoded error types)
error_count = kpi_errors['error_type_encoded'].count()

# Print the results
print(f"Number of errors from /var/www/html/umexpertv3/class/class.KpiHelperTeachingNew.php: {error_count}") 

# Filter for the target resource
kpi_errors = error_df[error_df['error_file'] == '/var/www/html/umexpertv3/class/class.KpiHelperTeachingNew.php']

# Get distribution of error categories
error_category_counts = kpi_errors['error_type_encoded'].value_counts()

# Print the results
print("Error Category Distribution:")
print(error_category_counts)