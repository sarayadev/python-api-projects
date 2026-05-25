from api import get_news
from config import API_KEY


def main():

    # Request news data
    data = get_news(API_KEY)

    # Display headlines
    if data:

        articles = data["articles"][:5]

        print("\nTop Headlines:\n")

        for article in articles:
            print("-", article["title"])


if __name__ == "__main__":
    main()