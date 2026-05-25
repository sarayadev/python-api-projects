from api import get_stock_price
from config import API_KEY, STOCK


def main():

    # Fetch stock data
    data = get_stock_price(STOCK, API_KEY)

    # Display stock price
    if data:

        price = data["Global Quote"]["05. price"]

        print(f"{STOCK} Price: ${price}")


if __name__ == "__main__":
    main()