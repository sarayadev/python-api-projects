import requests
from config import BASE_URL


# Fetch top headlines
def get_news(api_key):

    params = {
        "country": "us",
        "apiKey": api_key
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error fetching news:", e)
        return None