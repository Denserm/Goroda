from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser
import requests


def get_coordinates(city, key):
    global lat, lng
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            currency = results[0]['annotations']['currency']['name']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng}\n Страна: {country}\n Регион: {region}",
                    "map_url": osm_url,
                    "currency": f"Валюта: {currency}"
                        }
            else:
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng}\n Страна: {country}",
                    "map_url": osm_url,
                    "currency": f"Валюта: {currency}"
                }

        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"


def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {result['coordinates']}\n {result['currency']}")
    map_url = result['map_url']


def show_map():
    if map_url:
        webbrowser.open(map_url)


def get_weather(lat, lng):
    answer = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&current_weather=true")
    weather_json = answer.json()
    weather_city = weather_json["current_weather"]
    return weather_city


def show_weather():
    weather_city = get_weather(lat, lng)
    wea_label.config(text=f"Температура воздуха: {weather_city["temperature"]}")

def clear_info():
    entry.delete(0, END)
    label.config(text="Введите город и нажмите кнопку")
    wea_label.config(text="")


key = 'c093d801c6954ea98a7ffc36ff0b5b47'

map_url = ""
lat = ""
lng = ""

window = Tk()
window.title("Координаты городов")


entry = Entry(window, font=('Arial', 16))
entry.pack(pady=5)
entry.bind("<Return>", show_coordinates)

button = Button(window, text="Поиск координат", command=show_coordinates, font=('Arial', 16))
button.pack(pady=5)

label = Label(window, text="Введите город и нажмите кнопку", font=('Arial', 16))
label.pack(pady=5)

map_button = Button(window, text="Показать карту", command=show_map, font=('Arial', 16))
map_button.pack(pady=5)

weather_button = Button(window, text="Показать погоду", command=show_weather, font=('Arial', 16))
weather_button.pack(pady=5)

wea_label = Label(window, font=('Arial', 16))
wea_label.pack(pady=5)

clear_button = Button(window, text="Очистить", command=clear_info, font=('Arial', 16))
clear_button.pack(pady=5)

window.mainloop()