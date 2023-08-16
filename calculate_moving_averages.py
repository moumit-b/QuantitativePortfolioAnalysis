import pandas as pd


df = pd.read_csv('historical_stock_data.csv')

df['20-day MA'] = df['Close'].rolling(window = 20).mean()
df['50-day MA'] = df['Close'].rolling(window = 50).mean()

print(df)