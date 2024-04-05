
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from CSV file
data = pd.read_csv('revenue_data.csv')

# Assuming the CSV file has columns 'Date' and 'Revenue'
dates = pd.to_datetime(data['Date'])
revenue = data['Revenue']

# Calculate the standard deviation
std_dev = np.std(revenue)

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(dates, revenue, color='blue', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.title('30 Days Sales Revenue with Standard Deviation')
plt.axhline(y=np.mean(revenue), color='r', linestyle='-', linewidth=1, label='Mean Revenue')
plt.axhline(y=np.mean(revenue) + std_dev, color='g', linestyle='--', linewidth=1, label='Mean + Std Dev')
plt.axhline(y=np.mean(revenue) - std_dev, color='g', linestyle='--', linewidth=1, label='Mean - Std Dev')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
