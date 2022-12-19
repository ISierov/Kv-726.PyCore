import tkinter as tk
from urllib.request import urlopen
from PIL import ImageTk
from pyowm import OWM

API_KEY = '26dca5c36782d57cf580280619b7c203'
HEIGHT = 450
WIDTH = 650


def weather_icon_status(w):
    data = urlopen(w.weather_icon_url(size="2x"))
    weather_icon = ImageTk.PhotoImage(data=data.read())

    icon_frame = tk.Frame(root, bg="#009999", bd=5)
    icon_frame.place(relx=0.5, rely=0.4, relwidth=0.15, relheight=0.2, anchor='n')

    icon = tk.Label(icon_frame, bg="#009999")
    icon.place(relx=0, rely=0, relwidth=1, relheight=1)
    icon.image = weather_icon
    icon['image'] = icon.image
    icon.pack()


def weather_response():
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather

    weather_icon_status(w)

    label1.config(text=f"{entry_field.get().capitalize()}\n{int(w.temperature('celsius')['temp'])}°C")
    label2.config(text=w.detailed_status.capitalize())
    label3.config(text=f"Wind speed is {w.wind()['speed']} km/hours\n" f"Humidity of the air is {w.humidity}")


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#009999")
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="#009999", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.8, relheight=1)

img = tk.PhotoImage(file="search-icon.png")

button = tk.Button(frame, image=img, bg="white", command=lambda: weather_response())
button.place(relx=0.835, rely=0, relwidth=0.15, relheight=1)

city_frame = tk.Frame(root, bg="#009999", bd=5)
city_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.2, anchor='n')

label1 = tk.Label(city_frame, font=("Comic Sans MS", 24, "bold"), bg="#009999", fg="white")
label1.place(relx=0, rely=0, relwidth=1, relheight=1)

status_frame = tk.Frame(root, bg="#009999", bd=5)
status_frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.1, anchor='n')

label2 = tk.Label(status_frame, font=("Comic Sans MS", 20, "bold"), bg="#009999", fg="white")
label2.place(relx=0, rely=0, relwidth=1, relheight=1)

footer_frame = tk.Frame(root, bg="#009999", bd=5)
footer_frame.place(relx=0.5, rely=0.75, relwidth=0.77, relheight=0.2, anchor='n')

label3 = tk.Label(footer_frame, font=("Comic Sans MS", 14, "bold"), bg="#009999", fg="white")
label3.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
