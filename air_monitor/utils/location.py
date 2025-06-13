"""
Napisz dwie funkcje, z których:
– pierwsza – na podstawie podanego słownie opisu lokalizacji zwróci jej współrzędne
geograficzne (szerokość i długość geograficzną)
– druga – odwrotnie, na podstawie współrzędnych geograficznych, zwróci opis słowny podanej lokalizacji
Wykorzystaj do tego możliwości biblioteki geopy
"""

wszystkie_stacje_pomiarowe = [
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
    }
]

import ssl
import certifi
from geopy.geocoders import Nominatim

# Kontekst SSL z użyciem certyfikatów z certifi
ctx = ssl.create_default_context(cafile=certifi.where())
geolocator = Nominatim(user_agent="air_quality_app_Marcelina", ssl_context=ctx)

# Geolokator z ręcznie podanym user_agent i ssl_context
def get_coordinates(value):
    return geolocator.geocode(value)


location = get_coordinates("Poznań, Ogród Botaniczny Uniwersytetu im. Adama Mickiewicza")
print(location.address)
print("Szerokość:", location.latitude)
print("Długość:", location.longitude)
print(location.raw)

def get_name(value):
    return geolocator.reverse(value, timeout=10)

coordinates = wszystkie_stacje_pomiarowe[0]['gegrLat'], wszystkie_stacje_pomiarowe[0]['gegrLon']
location = get_name(coordinates)
print(location.address)
print("Szerokość:", location.latitude)
print("Długość:", location.longitude)
print(location.raw)