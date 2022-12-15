import pyowm
from pyowm import OWM
from pyowm.utils import timestamps
from pyowm.owm import OWM

owm_API = OWM('your_API')
CITY = "Kyiv"


def main():
    """AIR POLLUTION CONCENTRATIONS:"""
    air_mgr = owm_API.airpollution_manager()
    air_status = air_mgr.air_quality_at_coords(50.450001, 30.523333)  # ('Kyiv')
    air_status.co                                                  # concentrations of carbon
    air_status.o3                                                  # concentrations of ozone
    air_status.no                                                  # nitric oxide
    air_status.no2                                                 # nitrogen dioxide
    air_status.so2                                                 # sulfur dioxide
    air_status.pm2_5                                               # dust particles of PM2.5
    air_status.pm10                                                # dust particles of both PM10
    air_status.nh3                                                 # gaseous ammonia
    air_status.aqi                                                 # air quality index

    """WEATHER DETAILS:"""
    w_mgr = owm_API.weather_manager()
    observation = w_mgr.weather_at_place(CITY)
    weather = w_mgr.weather_at_place(CITY).weather
    temp_dict_celsius = weather.temperature('celsius')
    temp_dict_celsius['temp_min']
    temp_dict_celsius['temp_max']
    temp_dict_celsius['feels_like']
    wind_dict_in_meters_per_sec = observation.weather.wind()
    wind_dict_in_meters_per_sec['speed']
    weather.detailed_status
    sunrise_date = weather.sunrise_time(timeformat='date')
    sunset_date = weather.sunset_time(timeformat='date')

    print(
        f"AIR POLLUTION CONCENTRATIONS ARE: \nAir quality index: {air_status.aqi} \nConcentrations of carbon {air_status.co} \nConcentrations of ozone: {air_status.o3}\nNitric oxide: {air_status.no}\nNitrogen dioxide: {air_status.no2} \nSulfur dioxide: {air_status.so2}\nDust particles of PM2.5: {air_status.pm2_5} \nDust particles of PM10: {air_status.pm10} \nGaseous ammonia: {air_status.nh3}\n")
    print(
        f"WEATHER DETAILS ARE: \nTemperature min: {temp_dict_celsius['temp_min']}°C and max {temp_dict_celsius['temp_max']}°C \nFeels like: {temp_dict_celsius['feels_like']}°C \nWind speed: {wind_dict_in_meters_per_sec['speed']} m/s \nDetails: {weather.detailed_status}\nSunrise time: {sunrise_date} AM \nSunset time:{sunset_date} PM")


main()