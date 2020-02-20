import pprint
import json
import requests
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDk0w4XvG8kRvRQdmDsgpT1D9quvQEtPKU')


def read_places_json():
    with open('places.json') as placesFile:
        data = json.load(placesFile)

    return data


def write_places_json(data):
    with open('places.json', 'w') as placesFile:
        json.dump(data, placesFile)


data = read_places_json()
towns = []
for place, values in data.items():
    towns.append(values['town'])

towns.sort()
print(list(towns))


def get_adress(place, lat, lng):
    # Geocoding an address
    geocode_result = gmaps.geocode(place)
    if geocode_result == []:
        geocode_result = gmaps.reverse_geocode((float(lat), float(lng)))

    address_components = geocode_result[0]['address_components']
    for component in address_components:
        if component['types'][0] == "administrative_area_level_1":
            city = component['long_name']
        if component['types'][0] == "administrative_area_level_2":
            town = component['long_name']

    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']

    result = {
        "city": city,
        "town": town,
        "latitude": str(latitude),
        "longitude": str(longitude)
    }

    return result


def event_place_details(events):
    places = read_places_json()

    for event in events:
        place = event['place']
        lat = event['latitude']
        lng = event['longitude']
        if place in places:
            adress = places[place]
            event.update(adress)
            continue

        adress = get_adress(place, lat, lng)
        places[place] = adress
        event.update(adress)

    write_places_json(places)

    return events
