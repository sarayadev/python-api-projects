import requests
from config import BASE_URL


# Get current stock price data
def get_stock_price(stock, api_key):

    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": stock,
        "apikey": api_key
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error fetching stock data:", e)
        return None