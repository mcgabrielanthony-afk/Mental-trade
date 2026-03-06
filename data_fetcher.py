import requests

class DataFetcher:
    def __init__(self, crypto_api_url, forex_api_url):
        self.crypto_api_url = crypto_api_url
        self.forex_api_url = forex_api_url

    def fetch_crypto_data(self):
        try:
            response = requests.get(self.crypto_api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON data
        except requests.RequestException as e:
            print(f"Error fetching crypto data: {e}")
            return None

    def fetch_forex_data(self):
        try:
            response = requests.get(self.forex_api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON data
        except requests.RequestException as e:
            print(f"Error fetching forex data: {e}")
            return None

# Example usage:
# crypto_api = 'https://api.cryptocurrency.com/data'
# forex_api = 'https://api.forex.com/data'
# fetcher = DataFetcher(crypto_api, forex_api)
# print(fetcher.fetch_crypto_data())
# print(fetcher.fetch_forex_data())