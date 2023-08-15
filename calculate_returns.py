import pandas as pd


df = pd.read_csv('historical_stock_data.csv')

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')
df['Daily Return'] = df['Close'].pct_change()

print(df)