import requests

BASE_URL = 'https://fakestoreapi.com'

query_params = {
    "limit": 3
}

response = requests.get(f"{BASE_URL}/products", params=query_params)
print(response.json())