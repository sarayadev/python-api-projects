from api import get_bitcoin_price


def main():

    # Fetch crypto data
    data = get_bitcoin_price()

    # Display Bitcoin price
    if data:

        price = data["bitcoin"]["usd"]

        print(f"Bitcoin Price: ${price}")


if __name__ == "__main__":
    main()
