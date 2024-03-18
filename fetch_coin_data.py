import requests


class CoinData:
    def __init__(self):

        self.__api_key = 'fe99a86b-ceb8-45a8-b238-cf1972ae9853'
        self.__url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    def request(self):

        # parameters = {
        #     'limit': fetch_limit,  # Limit the number of results to 10 (top 10)
        #     'convert': 'USD'  # Convert prices to USD
        # }


        # Set up the request with API key
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.__api_key
        }

        data= None

        response = requests.get(self.__url, headers=headers)

        if response.status_code == 200:
            data = response.json()

        else:

            print(f"Error: {response.status_code} - {response.text}")

        return data

