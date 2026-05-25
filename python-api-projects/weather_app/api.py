import requests
from config import BASE_URL


# Fetch weather data from OpenWeather API
def get_weather(city, api_key):

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error fetching weather:", e)
        return None