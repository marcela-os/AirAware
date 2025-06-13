"""
Napiszfunkcję,któradladwóchpodanychlokalizacji,określonych przez szerokość i
 długość geograficzną (wyrażone w stopniach) obliczy odległość pomiędzy nimi (w km)
Spróbuj zadanie zrealizować w kilku wariantach:
– załóż, że powierzchnia Ziemi ma kształt sfery o promieniu 6371.009 km
(możesz też tę wartość odczytać po zaimportowaniu biblioteki geopy) i
oblicz odległość pomiędzy dwoma punktami na sferze, stosując podane wzory (p. algorytm wykonania),
– użyj biblioteki geopy i odszukaj funkcję, która oblicza odległość sferyczną,
– użyj biblioteki geopy i odszukaj funkcję, która oblicza odległość geodezyjną,
Porównaj otrzymane wyniki
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

from geopy import distance
import math

R = distance.EARTH_RADIUS
lok1 = (wszystkie_stacje_pomiarowe[0]['gegrLat'], wszystkie_stacje_pomiarowe[0]['gegrLon'])
lok2 = (wszystkie_stacje_pomiarowe[8]['gegrLat'], wszystkie_stacje_pomiarowe[8]['gegrLon'])


def f1(a, b):
    szer1 = math.radians(float(a[0]))
    dlug1 = math.radians(float(a[1]))
    szer2 = math.radians(float(b[0]))
    dlug2 = math.radians(float(b[1]))
    a = math.sin((szer2 - szer1) / 2) ** 2 + math.cos(szer1) * math.cos(szer2) * math.sin((dlug2 - dlug1) / 2) ** 2
    odlegosc = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return odlegosc * R

odleglosc = f1(lok1, lok2)
print(f'1. Odległość między lokalizacjami: {odleglosc:.2f} km')


def f2(a, b):
    return distance.great_circle(a, b).km

odleglosc = f2(lok1, lok2)
print(f'2. Odległość między lokalizacjami: {odleglosc:.2f} km')


def f3(a, b):
    return distance.geodesic(a, b).km

odleglosc = f3(lok1, lok2)
print(f'3. Odległość między lokalizacjami: {odleglosc:.2f} km')
