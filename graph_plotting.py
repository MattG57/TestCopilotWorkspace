import pandas as pd
import matplotlib.pyplot as plt

# Read data from shampoo.csv file and parse date column
data = pd.read_csv('shampoo.csv', parse_dates=['Date'])

# Draw scatter plot with date on x-axis and sales on y-axis
plt.figure(figsize=(10, 6))
plt.scatter(data['Date'], data['Sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Shampoo Sales Trend')

# Save the plot to shampoo.png file
plt.savefig('shampoo.png')
