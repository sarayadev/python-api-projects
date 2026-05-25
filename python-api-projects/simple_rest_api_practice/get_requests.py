import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# Send GET request
response = requests.get(f"{BASE_URL}/posts")

# Convert response to JSON
data = response.json()

# Print first 3 posts
for post in data[:3]:
    print(post["title"])