import requests
import json

BASE_URL = 'https://fakestoreapi.com'

new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(f"{BASE_URL}/products", data=json.dumps(new_product), headers=headers)
print(response.json())