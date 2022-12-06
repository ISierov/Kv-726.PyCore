import pyowm

OWM_API_key = pyowm.OWM('26ba7b8ee9b16c72a279e4b785a5ff02')

my_city = input()

manager = OWM_API_key.weather_manager()

observe = manager.weather_at_place(my_city)
w = observe.weather

temperature = w.temperature('celsius')

print(temperature['feels_like'])
