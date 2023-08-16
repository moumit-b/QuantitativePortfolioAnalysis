import pandas as pd


df = pd.read_csv('processed_data.csv')

df['20-day MA'] = df['Close'].rolling(window = 20).mean()
df['50-day MA'] = df['Close'].rolling(window = 50).mean()

df.to_csv('processed_data.csv', index=False)

print(df)