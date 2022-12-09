import requests
import json

city_is = "kyiv"           # input('My city is: ')
number_of_days = 2         # input('For how many days ahead you want to see forecast? ')
apiKey = 'ee230d2c39e18a68e88b6aaa434f6adb'
response_API = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=kyiv&cnt=2&appid=ee230d2c39e18a68e88b6aaa434f6adb&units=metric")  # apiUrl
"""
why this one doesn't work:
"""
# response = requests.get("https://api.openweathermap.org/data/2.5/forecast?q={city_is}&cnt={number_of_days}&appid={apiKey}&units=metric")
# print(response.status_code)
print(response_API.json())

"""can't extract data:"""
data = response_API.text
parse_json = json.loads(data)
weather = parse_json['main']['temp']
print("temperature is: ", weather)
"""
what is wrong? how to extract data like 'temp', 'wind'... ?
"""

"""
    document.querySelector("#humidity").innerHTML = response.data.main.humidity;
    document.querySelector("#wind").innerHTML = response.data.wind.speed;
це з JS, але завдання було таке саме, той самий апі і т.д. Тут зрозуміло, що прописуєш шлях до параметру, який тебе цікавить, як відкриваю коробку і заглиблююсь в наступну папку.

А в python не розумію де дивитись ці данні і як їх вивести.
Порадьте, як розібратись 
"""