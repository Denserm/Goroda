from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            return lat, lng
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"



key = 'c093d801c6954ea98a7ffc36ff0b5b47'
city = "Волжский"
coordinates = get_coordinates(city, key)
print(city, coordinates)