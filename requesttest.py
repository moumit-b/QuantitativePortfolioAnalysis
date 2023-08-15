import requests
import json
import pandas as pd

# Replace with your Alpha Vantage API key
api_key = 'CBP69ER5QF1IGEW5'

# Specify the API endpoint and parameters
function = 'TIME_SERIES_DAILY'
symbol = 'AAPL'

# Construct the API URL
base_url = 'https://www.alphavantage.co/query'
params = {
    'function': function,
    'symbol': symbol,
    'apikey': api_key
}

# Send the API request
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the time series data (daily prices)
    time_series = data['Time Series (Daily)']

    # Convert data to DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.reset_index(inplace=True)
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

    # Convert date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Save DataFrame to CSV file
    df.to_csv('historical_stock_data.csv', index=False)

    print("Data saved to historical_stock_data.csv")
else:
    print("Error:", response.status_code)
