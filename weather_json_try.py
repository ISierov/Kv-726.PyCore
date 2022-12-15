import requests
import json
import os

CITY = "kyiv"                             # input('My city is: ')
NUMBER_OF_DAYS = 1                        # input('For how many days ahead you want to see forecast? ')
API_KEY = 'your_API'

# print(response_API.json())
def main():
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/forecast",
        params={"q": CITY, "cnt": NUMBER_OF_DAYS, "appid": API_KEY, "units": "metric"})
    response.raise_for_status()
    print("temperature is: ", response.json()['list'][0]['main']['temp'])
    print("feels_like: ", response.json()['list'][0]['main']['feels_like'])
    print("pressure: ", response.json()['list'][0]['main']['pressure'])
    print("humidity: ", response.json()['list'][0]['main']['humidity'])
    print("weather description: ", response.json()['list'][0]['weather'][0]['description'])
    print("date: ", response.json()['list'][0]['dt_txt'])


main()
"""
{'cod': '200', 'message': 0, 'cnt': 2,
'list': [{'dt': 1671105600,
'main': {'temp': -0.44, 'feels_like': -5.89, 'temp_min': -0.44, 'temp_max': 0.09, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 996, 'humidity': 94, 'temp_kf': -0.53}, 
'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'clouds': {'all': 100}, 
'wind': {'speed': 5.77, 'deg': 178, 'gust': 14.76}, 
'visibility': 121, 'pop': 1, 'snow': {'3h': 1.3}, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-15 12:00:00'}], 
'city': {'id': 703448, 'name': 'Kyiv', 
'coord': {'lat': 50.4333, 'lon': 30.5167}, 'country': 'UA', 'population': 2514227, 'timezone': 7200, 'sunrise': 1671083509, 'sunset': 1671112454}}
"""