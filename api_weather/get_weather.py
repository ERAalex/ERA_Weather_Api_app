import requests
import json
from pprint import pprint
from config.config_tokens import weather_api_token

weather_api = weather_api_token

def get_city_weather(city_name):
    # получаем координаты по названию города
    complete_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid='+weather_api
    response = requests.get(complete_url)
    result = response.json()
    # городов много в разных странах с одинаковым именем, берем первый, самый галвный
    try:
        lon = result[0]['lon']
        lat = result[0]['lat']

        # по координатам пробиваем погоду местности
        complete_url_city = 'https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) +\
                            '&appid=' + weather_api
        response_city = requests.get(complete_url_city)
        result_city = response_city.json()

        diccionary = {}
        diccionary['city'] = result_city['name']
        # внимание данные в json приходят в кельвинах и надо перевести в цельсии + округлим
        diccionary['temperature'] = round(result_city['main']['temp'] - 273.15, 1)

        return diccionary

    except:
        return None

#
# pprint(get_city_weather('Berliasdasdasn'))