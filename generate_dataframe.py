import requests
import pandas as pd
import fetch_coin_data as coindata
from importlib import reload
reload(coindata)

coins = coindata.CoinData
# Function to fetch data for the top 10 cryptocurrencies from the CoinMarketCap API
def fetch_top_10_data(response):
    data = response
    top_10_data = []
    for crypto in data['data']:
        top_10_data.append({
            'Name': crypto['name'],
            'Symbol': crypto['symbol'],
            'Price (USD)': crypto['quote']['USD']['price'],
            'Market Cap (USD)': crypto['quote']['USD']['market_cap']
        })
    df = pd.DataFrame(top_10_data)

    return df

if __name__ == '__main__':
    coin = coins().request()
    data=fetch_top_10_data(coin)
    data.index +=1
    data = data.head(5)
    # price = []
    # for index, row in data.iterrows():
    #     for col,val in row.items():
    #         if col == 'Price (USD)':
    #             price.append(val)
    print(data)