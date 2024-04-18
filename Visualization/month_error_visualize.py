import pandas as pd
import matplotlib.pyplot as plt

# Sample data with different error levels
df = pd .read_csv('output/extracted_error_features.csv')

# Count the number of occurrences of each error level
error_level_counts = df['error_level_encoded'].value_counts()

# Create a bar chart to visualize the number of occurrences
plt.figure(figsize=(8, 6))
error_level_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Error Level')
plt.ylabel('Number of Occurrences')
plt.title('Number of Errors by Level')
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

####################

# Specify the error levels to display
error_levels_to_display = ['1','2']

# Filter the data for the chosen error levels
filtered_df = df[df['error_level_encoded'].isin(error_levels_to_display)]

# Visualization
plt.figure(figsize=(10, 6))

# Bar chart for error level counts
filtered_df['error_level_encoded'].value_counts().plot(kind='bar', color='orange')
plt.xlabel('Error Level')
plt.ylabel('Number of Occurrences')
plt.title('Number of Errors by Selected Levels')
plt.xticks(rotation=0)
plt.tight_layout()

# Print the error messages
print("Error Messages:")
for index, row in filtered_df.iterrows(): 
    print(f"* {row['error_level_encoded']}: {row['error_message']}") 

plt.show()