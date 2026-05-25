from api import get_weather
from config import API_KEY


def main():
    # Get city from user
    city = input("Enter city name: ")

    # Request weather data
    data = get_weather(city, API_KEY)

    # Display weather information
    if data:

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        print(f"\nCity: {city}")
        print(f"Weather: {weather}")
        print(f"Temperature: {temp}°C")


if __name__ == "__main__":
    main()