import pandas as pd

# Load processed data
df = pd.read_csv('processed_data.csv')

# Calculate ATR
def calculate_atr(data, period=14):
    tr = data[['High', 'Low', 'Close']].apply(lambda row: max(row) - min(row), axis=1)
    atr = tr.rolling(window=period).mean()
    return atr

# Calculate ATR and add to DataFrame
df['ATR'] = calculate_atr(df)

# Save processed data
df.to_csv('processed_data.csv', index=False)

print(df)