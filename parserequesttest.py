import requests
import json



# Replace with your Alpha Vantage API key
api_key = 'CBP69ER5QF1IGEW5'

# Specify the API endpoint and parameters
function = 'TIME_SERIES_DAILY'  # Choose the API function you need
symbol = 'AMZN'  # Replace with the desired stock symbol

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

    # Loop through the time series data and print each entry
    for date, values in time_series.items():
        open_price = values['1. open']
        high_price = values['2. high']
        low_price = values['3. low']
        close_price = values['4. close']
        volume = values['5. volume']
        
        print(f"Date: {date}")
        print(f"Open: {open_price}")
        print(f"High: {high_price}")
        print(f"Low: {low_price}")
        print(f"Close: {close_price}")
        print(f"Volume: {volume}")
        print("--------------------------")
else:
    print("Error:", response.status_code)
