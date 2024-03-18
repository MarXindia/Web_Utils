import requests


class CoinData:
    def __init__(self):
        self.__api_key = 'aa27d520-3a5b-4005-8c67-f8013e69d104'

    def request(self):

        # API endpoint URL
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

        # Set up the request headers with your API key
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.__api_key
        }

        # Make the API request
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code} - {response.text}")

        return response
