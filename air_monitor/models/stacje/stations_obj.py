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


class Commune:
    def __init__(self, name, district, province):
        self.__name = name
        self.__district = district
        self.__province = province

    @property
    def name(self):
        return self.__name

    @property
    def district(self):
        return self.__district

    @property
    def province(self):
        return self.__province

    def __str__(self):
        return f'{self.name}, District: {self.district}, Province: {self.province.capitalize()}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.district}', '{self.province}')"

    def __eq__(self, other):
        return isinstance(other, Commune) and (
            self.name, self.district, self.province
        ) == (other.name, other.district, other.province)

    def __hash__(self):
        return hash((self.name, self.district, self.province))


class City:
    def __init__(self, name, id, commune):
        self.__name = name
        self.__id = id
        self.__commune = commune

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def commune(self):
        return self.__commune

    def __str__(self):
        return f'{self.name}, City ID: {self.id}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.id})"

    def __eq__(self, other):
        return isinstance(other, City) and (
            self.name, self.id
        ) == (other.name, other.id)

    def __hash__(self):
        return hash((self.name, self.id))


class Station:
    def __init__(self, name, id, lat, lon, city):
        self.__name = name
        self.__id = id
        self.__lat = lat
        self.__lon = lon
        self.__city = city

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def lat(self):
        return self.__lat

    @property
    def lon(self):
        return self.__lon

    @property
    def city(self):
        return self.__city

    def __str__(self):
        return f'Station {self.name}, Station ID: {self.id}, ({self.lat}, {self.lon}), City: {self.city}, Commune: {self.city.commune} '

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.id}, {self.lat}, {self.lat}, City: {self.city!r}, Commune: {self.city.commune!r})"

    def __eq__(self, other):
        return isinstance(other, Station) and (
            self.name, self.id, self.lat, self.lon, self.city, self.city.commune
        ) == (other.name, other.id, other.lat, other.lon, other.city, other.city.commune)

    def __hash__(self):
        return hash((self.name, self.id, self.lat, self.lon, self.city, self.city.commune))

stations = []
for data in wszystkie_stacje_pomiarowe:
    commune_data = data['city']['commune']
    commune = Commune(commune_data['communeName'], commune_data['districtName'], commune_data['provinceName'])
    city = City(data['city']['name'], data['city']['id'], commune)
    station = Station(data['stationName'], data['id'], data['gegrLat'], data['gegrLon'], city)
    stations.append(station)

for station in stations:
    print(station)

# Stacje w Poznaniu
poznan_stations = [station for station in stations if station.city.name == 'Poznań']

print("\nStacje w Poznaniu:")
for station in poznan_stations:
    print(station)

# Stacje w określonym zakresie szerokości geograficznej
min_lat = 52.20
max_lat = 52.25
stations_in_lat = [
    station for station in stations
    if min_lat <= float(station.lat) <= max_lat
]
print("\nStacje w zakresie szerokości geograficznej (52.2 - 52.25):")
for station in stations_in_lat:
    print(station)


print(repr(stations[0]))
print(stations[0] == stations[1])
commune1 = stations[0].city.commune
commune2 = stations[1].city.commune
print(commune1 == commune2)

target_commune = Commune('Poznań', 'Poznań', 'WIELKOPOLSKIE')
print(target_commune in [station.city.commune for station in stations])

#wszystkie unikalne gminy
unique_communes = list(set(station.city.commune for station in stations))
for commune in unique_communes:
    print(repr(commune))

#wszystkie unikalne miasta
unique_cities = set(station.city for station in stations)
print(f"\nLiczba unikalnych miejscowości: {len(unique_cities)}")
for city in unique_cities:
    print(repr(city))