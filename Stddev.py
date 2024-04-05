import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('revenue_data.csv')

# Convert the date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date
df = df.sort_values(by='Date')

# Calculate the rolling 30-day standard deviation of revenue
rolling_std = df['Revenue'].rolling(window=30).std()

# Plot the rolling standard deviation
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], rolling_std, color='blue')
plt.title('30-Day Sales Revenue Standard Deviation')
plt.xlabel('Date')
plt.ylabel('Standard Deviation')
plt.grid(True)
plt.show()
