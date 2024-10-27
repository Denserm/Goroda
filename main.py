from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"


key = 'c093d801c6954ea98a7ffc36ff0b5b47'
city = "Moscow"
coordinates = get_coordinates(city, key)
print(city, coordinates)