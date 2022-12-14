import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'there is an API key'


def weather_response(input_city):

    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()

        # Search for current weather in city and get details
        observation = mgr.weather_at_place(input_city)
        w = observation.weather
        country = observation.to_dict()['location']['country']
        if country == 'RU':
            return "! Russian warship, go fuck yourself ! \nWE NOT WORKS WITH TERRORISTS\nEnter the city again."
        # w.detailed_status         # 'clouds'
        # w.wind()                  # {'speed': 4.6, 'deg': 330}
        # w.humidity                # 87
        # w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        # w.rain                    # {}
        # w.heat_index              # None
        # w.clouds                  # 75
        return f"City: {input_city.title()}\nConditions: {w.detailed_status }\nTemperature is {round(w.temperature('celsius')['temp'], 2)} C \n Wind speed is {w.wind()['speed']} km/hours\nHumidity of the air is {w.humidity}"
    except:
        return 'Oops!\nThere was a problem\nretrieving that information.\nTry again'


def get_weather(input_city):
    label['text'] = weather_response(input_city)


HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application Nikita")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,
            relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Roboto', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Roboto', 8),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='green', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Roboto', 12))
label.place(relx=0, rely=0, relwidth=1, relheight=1)
root.mainloop()
