import hashlib
import requests
import time

response = requests.get('http://127.0.0.1:8000/get_asserts/',
                        headers={'OpenKey': 'a5fa7a3af312a4add3ba0f6e15a5c92a|1514905354.8494847'})
print(response.text)
