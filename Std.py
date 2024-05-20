
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'NAME': ['Appl', 'Rel'],
    '2020-01': [10, 30],
    '2023-02': [20, -60],
    '2023-03': [30, 70],
    '2024-01': [40, 47],
    '2024-02': [60, 277],
    '2024-03': [-50, -80]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate standard deviation for each row
df['STD'] = df.loc[:, '2020-01':'2024-03'].std(axis=1)

# Plotting
plt.figure(figsize=(10, 6))

for index, row in df.iterrows():
    plt.plot(df.columns[1:-1], row[1:-1], marker='o', label=row['NAME'])

# Adding title and labels
plt.title('Revenue Over Time')
plt.xlabel('Time')
plt.ylabel('Revenue')
plt.legend()

# Show plot
plt.show()

# Print DataFrame with standard deviations
print(df)
