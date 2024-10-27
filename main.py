from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            return f"Широта: {lat}, Долгота: {lng}"
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"


def show_coordinates():
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}: {coordinates}")

key = 'c093d801c6954ea98a7ffc36ff0b5b47'

window = Tk()
window.title("Координаты городов")
window.geometry("200x100")

entry = Entry(window)
entry.pack()

button = Button(window, text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(window, text="Введите город и нажмите кнопку")
label.pack()


window.mainloop()