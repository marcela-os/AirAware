"""
Napisz dwie funkcje, z których:
– pierwsza – na podstawie podanego słownie opisu lokalizacji zwróci jej współrzędne
geograficzne (szerokość i długość geograficzną)
– druga – odwrotnie, na podstawie współrzędnych geograficznych, zwróci opis słowny podanej lokalizacji
Wykorzystaj do tego możliwości biblioteki geopy
"""

wszystkie_stacje_pomiarowe = [
    {
        'id': 16493,
        'stationName': 'Poznań ul. Szwajcarska',
        'gegrLat': '52.390960',
        'gegrLon': '16.998048',
        'city': {
            'id': 729,
            'name': 'Poznań',
            'commune': {
                'communeName': 'Poznań',
                'districtName': 'Poznań',
                'provinceName': 'WIELKOPOLSKIE'
            }
        },
        'addressStreet': 'ul. Szwajcarska'
    },
    {
        'id': 530,
        'stationName': 'Warszawa, al. Niepodległości',
        'gegrLat': '52.219298',
        'gegrLon': '21.004724',
        'city': {
            'id': 1006,
            'name': 'Warszawa',
            'commune': {
                'communeName': 'Warszawa',
                'districtName': 'Warszawa',
                'provinceName': 'MAZOWIECKIE'
            }
        },
        'addressStreet': 'al. Niepodległości 227/233'
    },
    {
        'id': 10956,
        'stationName': 'Warszawa, ul. Bajkowa',
        'gegrLat': '52.188474',
        'gegrLon': '21.176233',
        'city': {
            'id': 1006,
            'name': 'Warszawa',
            'commune': {
                'communeName': 'Warszawa',
                'districtName': 'Warszawa',
                'provinceName': 'MAZOWIECKIE'
            }
        },
        'addressStreet': 'ul. Bajkowa 17/21'
    },
    {
        'id': 550,
        'stationName': 'Warszawa, ul. Wokalna',
        'gegrLat': '52.160772',
        'gegrLon': '21.033819',
        'city': {
            'id': 1006,
            'name': 'Warszawa',
            'commune': {
                'communeName': 'Warszawa',
                'districtName': 'Warszawa',
                'provinceName': 'MAZOWIECKIE'
            }
        },
        'addressStreet': 'ul. Wokalna 1'
    },
    {
        'id': 552,
        'stationName': 'Warszawa, ul. Kondratowicza',
        'gegrLat': '52.290864',
        'gegrLon': '21.042458',
        'city': {
            'id': 1006,
            'name': 'Warszawa',
            'commune': {
                'communeName': 'Warszawa',
                'districtName': 'Warszawa',
                'provinceName': 'MAZOWIECKIE'
            }
        },
        'addressStreet': 'ul. Kondratowicza 8'
    },
    {
        'id': 538,
        'stationName': 'Warszawa, ul. Tołstoja',
        'gegrLat': '52.285073',
        'gegrLon': '20.933018',
        'city': {
            'id': 1006,
            'name': 'Warszawa',
            'commune': {
                'communeName': 'Warszawa',
                'districtName': 'Warszawa',
                'provinceName': 'MAZOWIECKIE'
            }
        },
        'addressStreet': 'ul. Tołstoja 2'
    },
    {
        'id': 10955,
        'stationName': 'Warszawa, ul. Chrościckiego',
        'gegrLat': '52.207742',
        'gegrLon': '20.906073',
        'city': {
            'id': 1006,
            'name': 'Warszawa',
            'commune': {
                'communeName': 'Warszawa',
                'districtName': 'Warszawa',
                'provinceName': 'MAZOWIECKIE'
            }
        },
        'addressStreet': 'ul. Chrościckiego 16/18'
    },
    {
        'id': 16533,
        'stationName': 'Warszawa, IMiGW',
        'gegrLat': '52.281472',
        'gegrLon': '20.963361',
        'city': {
            'id': 1006,
            'name': 'Warszawa',
            'commune': {
                'communeName': 'Warszawa',
                'districtName': 'Warszawa',
                'provinceName': 'MAZOWIECKIE'
            }
        },
        'addressStreet': 'ul. Podleśna 61'
    },
    {
        'id': 944,
        'stationName': 'Poznań, ul. Dąbrowskiego',
        'gegrLat': '52.420319',
        'gegrLon': '16.877289',
        'city': {
            'id': 729,
            'name': 'Poznań',
            'commune': {
                'communeName': 'Poznań',
                'districtName': 'Poznań',
                'provinceName': 'WIELKOPOLSKIE'
            }
        },
        'addressStreet': 'ul. Dąbrowskiego 169'
    },
    {
        "id": 986,
        "stationName": "Szczecin, ul. Andrzejewskiego",
        "gegrLat": "53.380975",
        "gegrLon": "14.663347",
        "city": {
            "id": 917,
            "name": "Szczecin",
            "commune": {
                "communeName": "Szczecin",
                "districtName": "Szczecin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Andrzejewskiego 23"
    },
    {
        "id": 987,
        "stationName": "Szczecin, ul. Piłsudskiego",
        "gegrLat": "53.432169",
        "gegrLon": "14.553900",
        "city": {
            "id": 917,
            "name": "Szczecin",
            "commune": {
                "communeName": "Szczecin",
                "districtName": "Szczecin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Piłsudskiego 1"
    },
    {
        "id": 989,
        "stationName": "Szczecin, ul. Łączna",
        "gegrLat": "53.470889",
        "gegrLon": "14.556250",
        "city": {
            "id": 917,
            "name": "Szczecin",
            "commune": {
                "communeName": "Szczecin",
                "districtName": "Szczecin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Łączna"
    },
    {
        "id": 966,
        "stationName": "Koszalin, ul. Armii Krajowej",
        "gegrLat": "54.193986",
        "gegrLon": "16.172544",
        "city": {
            "id": 402,
            "name": "Koszalin",
            "commune": {
                "communeName": "Koszalin",
                "districtName": "Koszalin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Armii Krajowej"
    },
    {
        "id": 11336,
        "stationName": "Koszalin, ul. Chopina",
        "gegrLat": "54.194114",
        "gegrLon": "16.211672",
        "city": {
            "id": 402,
            "name": "Koszalin",
            "commune": {
                "communeName": "Koszalin",
                "districtName": "Koszalin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Chopina 42"
    },
    {
        "id": 961,
        "stationName": "Widuchowa",
        "gegrLat": "53.122325",
        "gegrLon": "14.382245",
        "city": {
            "id": 1025,
            "name": "Widuchowa",
            "commune": {
                "communeName": "Widuchowa",
                "districtName": "gryfiński",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Bulwary Rybackie 1"
    },
    {
        "id": 983,
        "stationName": "Szczecinek, ul. Przemysłowa",
        "gegrLat": "53.698902",
        "gegrLon": "16.704556",
        "city": {
            "id": 918,
            "name": "Szczecinek",
            "commune": {
                "communeName": "Szczecinek",
                "districtName": "szczecinecki",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Przemysłowa 5"
    },
    {
        "id": 10934,
        "stationName": "Kołobrzeg, ul. Żółkiewskiego",
        "gegrLat": "54.179381",
        "gegrLon": "15.596347",
        "city": {
            "id": 386,
            "name": "Kołobrzeg",
            "commune": {
                "communeName": "Kołobrzeg",
                "districtName": "kołobrzeski",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Żółkiewskiego"
    },
    {
        "id": 20160,
        "stationName": "Świnoujście, ul. Białoruska",
        "gegrLat": "53.903814",
        "gegrLon": "14.279628",
        "city": {
            "id": 952,
            "name": "Świnoujście",
            "commune": {
                "communeName": "Świnoujście",
                "districtName": "Świnoujście",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "Białoruska"
    }
]

import ssl
import certifi
from geopy.geocoders import Nominatim
from geopy import distance

# Kontekst SSL z użyciem certyfikatów z certifi
ctx = ssl.create_default_context(cafile=certifi.where())
geolocator = Nominatim(user_agent="air_quality_app_Marcelina", ssl_context=ctx)


def get_stations(description, max_distance_km, stations_data):
    """
    Returns a list of measuring stations within a specified distance from the specified location.

    :param description: Description of location (e.g. ‘Poznań, market square’)
    :param max_distance_km: Maximum distance in kilometres (float)
    :param stations_data: List of dict with stations, each containing ‘gegrLat’, ‘gegrLon’ and ‘stationName’
    :return: List of tuples (distance_km, station_name) sorted in ascending order of distance
    """

    location = geolocator.geocode(description, timeout=10)

    if not location:
        raise ValueError(f"No location found for the description: {description}")

    data = [(float(item['gegrLat']), float(item['gegrLon']), item['stationName']) for item in stations_data]
    stations = [(round(distance.geodesic((location.latitude, location.longitude), (item[0], item[1])).km, 2), item[2])
                for item in data]

    stations = list(filter(lambda item: (item[0] <= max_distance_km), stations))

    return sorted(stations, key=lambda value: value[0])


new = get_stations("Poznań, dworzec główny", 200, wszystkie_stacje_pomiarowe)
print(new)
