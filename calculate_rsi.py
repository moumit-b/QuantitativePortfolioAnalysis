import pandas as pd

# Load processed data
df = pd.read_csv('processed_data.csv')

# Calculate RSI
def calculate_rsi(data, period=14):
    # Calculate the difference between consecutive closing prices
    delta = data['Close'].diff()

    # Calculate the gain and loss
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate the average gain and average loss
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    # Calculate the relative strength (RS)
    rs = avg_gain / avg_loss

    # Calculate RSI
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

# Calculate RSI and add to DataFrame
df['RSI'] = calculate_rsi(df)

# Save processed data
df.to_csv('processed_data.csv', index=False)

print(df)