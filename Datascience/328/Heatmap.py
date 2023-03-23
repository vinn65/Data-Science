import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('data.csv')

# Create a pivot table that counts the occurrences of each sales type
pivot_table = data.pivot_table(index='type_name', values='sales_type_id', aggfunc='count')

# Plot the pivot table as a heatmap
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='d')
plt.title('Sales Type Count')
plt.xlabel('Sales Type ID')
plt.ylabel('Sales Type Name')

# Display the heatmap
plt.show()
