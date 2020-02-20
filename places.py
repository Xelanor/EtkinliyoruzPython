import pprint
import json

data = {
    "kozzy": {
        "town": "kadıköy",
        "latitude": "15161",
        "longitude": "11651"
    },
    "asdasd": {
        "town": "asdasd",
        "latitude": "15161",
        "longitude": "11651"
    }
}

with open('places.json', 'w') as placesFile:
    json.dump(data, placesFile)

with open('places.json') as placesFile:
    data = json.load(placesFile)

print("kozzy" in data)
