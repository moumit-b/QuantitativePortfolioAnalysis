import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('processed_data.csv')

# Plot stock prices and moving averages
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Stock Price', color='blue')
plt.plot(df['Date'], df['20-day MA'], label='20-day MA', color='orange')
plt.plot(df['Date'], df['50-day MA'], label='50-day MA', color='green')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price and Moving Averages')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
