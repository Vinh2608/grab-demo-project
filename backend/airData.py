import requests
import json

API_KEY = 'a52a17bde8ce5aecda9cf37ef79748ce'

url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&appid={API_KEY}'
response = requests.get(url)
response = response.json()
print(json.dumps(response, indent=4))
