import pandas as pd

# Load processed data
df = pd.read_csv('processed_data.csv')

# Calculate MACD
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = data['Close'].ewm(span=short_window, min_periods=1, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, min_periods=1, adjust=False).mean()
    
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal_window, min_periods=1, adjust=False).mean()
    
    return macd, signal_line

# Calculate MACD and Signal Line, add to DataFrame
df['MACD'], df['Signal Line'] = calculate_macd(df)

# Save processed data
df.to_csv('processed_data.csv', index=False)

print(df)