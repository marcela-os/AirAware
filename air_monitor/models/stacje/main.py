"""
Moduł testujący działanie serializacji i deserializacji.
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

if __name__ == '__main__':
    from python07.extra.stacje.convert.converter import convert_station


    def main(data):
        station = convert_station(data)
        print(station)
        print('CZY RÓWNE?', wszystkie_stacje_pomiarowe[0] == station[0]) #False — są to różne typy danych
        print('CZY RÓWNE?', station[0].name == wszystkie_stacje_pomiarowe[0]['stationName'])


    main(wszystkie_stacje_pomiarowe)
