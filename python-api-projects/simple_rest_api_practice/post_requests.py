import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# Example post data
new_post = {
    "title": "My First API Post",
    "body": "Learning APIs with Python",
    "userId": 1
}

# Send POST request
response = requests.post(
    f"{BASE_URL}/posts",
    json=new_post
)

# Print API response
print(response.json())