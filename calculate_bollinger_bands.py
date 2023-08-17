import pandas as pd


df = pd.read_csv('processed_data.csv')

# Calculate the standard deviation of the Close prices
df['Std Deviation'] = df['Close'].rolling(window=20).std()

# Calculate the upper and lower Bollinger Bands
df['Upper Bollinger'] = df['20-day MA'] + (2 * df['Std Deviation'])
df['Lower Bollinger'] = df['20-day MA'] - (2 * df['Std Deviation'])

df.to_csv('processed_data.csv', index=False)

print(df)