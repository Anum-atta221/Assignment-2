import requests

response = requests.get('http://localhost:5000/?n=16')

print(response.text)
