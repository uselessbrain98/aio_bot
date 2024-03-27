import requests
from settings import WEATHER_TOKEN

base_url = 'http://api.weatherapi.com/v1'
current_weather = '/current.json'
forecast_weather = '/forecast.json'
params = {
    'key': WEATHER_TOKEN,
    'q': 'Kazan',
    'lang': 'ru',
}

response = requests.get(url=base_url+current_weather, params=params)

print(response.json())
