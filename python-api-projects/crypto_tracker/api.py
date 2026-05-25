import requests

def get_bitcoin_price():
    # CoinGecko Bitcoin price endpoint
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    try:
        # Fetch data from API
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Return JSON response
        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error fetching crypto data:", e)
        return None