import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
df = pd.read_csv('processed_data.csv')

plt.figure(figsize=(10, 6))

# Plot stock prices
plt.plot(df['Date'], df['Close'], label='Stock Price', color='blue')

# Plot moving averages
plt.plot(df['Date'], df['20-day MA'], label='20-day MA', color='orange')
plt.plot(df['Date'], df['50-day MA'], label='50-day MA', color='green')

# Plot Bollinger Bands
plt.plot(df['Date'], df['Upper Bollinger'], label='Upper Bollinger', color='red', linestyle='dashed')
plt.plot(df['Date'], df['Lower Bollinger'], label='Lower Bollinger', color='red', linestyle='dashed')

# Plot RSI
plt.plot(df['Date'], df['RSI'], label='RSI', color='purple')

# Plot MACD and Signal Line
plt.plot(df['Date'], df['MACD'], label='MACD', color='cyan')
plt.plot(df['Date'], df['Signal Line'], label='Signal Line', color='magenta')

# Plot ATR
plt.plot(df['Date'], df['ATR'], label='ATR', color='brown')

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Technical Indicators and Stock Price')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
