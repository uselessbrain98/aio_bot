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


def get_weather(what):
    if what == 'current':
        try:
            r = requests.get(url=base_url + current_weather, params=params)
            return r.json()
        except Exception:
            return "Что-то пошло не так: 1"
    elif what == 'forecast':
        try:
            r = requests.get(url=base_url + forecast_weather, params=params)
            return r.json()
        except Exception:
            return "Что-то пошло не так: 2"
    else:
        return "Что-то пошло не так: 3"
