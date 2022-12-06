import pyowm

OWM_API_key = pyowm.OWM('YOUR_KEY')

my_city = input()

manager = OWM_API_key.weather_manager()

observe = manager.weather_at_place(my_city)
w = observe.weather

temperature = w.temperature('celsius')

print(temperature['feels_like'])
