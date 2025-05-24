"""
Moduł umożliwiający konwersję danych do modelu obiektowego
"""

# from ..model.stations import stations
# from python07.extra.modul.model import stations as stations_model
from python07.extra.stacje.model import Station
from python07.extra.stacje.model import City
from python07.extra.stacje.model import Commune



def convert_station(data_dict):
    print("Type of input:", type(data_dict))

    print('data_dict', data_dict)
    stations = []
    for data in data_dict:
        commune_data = data['city']['commune']
        commune = Commune(commune_data['communeName'], commune_data['districtName'], commune_data['provinceName'])
        city = City(data['city']['name'], data['city']['id'], commune)
        station = Station(data['stationName'], data['id'], data['gegrLat'], data['gegrLon'], city)
        stations.append(station)

    for station in stations:
        print('station',station)

    return [station for station in stations]
    # return Station(data_dict['stationName'], data_dict['id'], data_dict['latitude'], data_dict['longitude'] )


# return f'Station {self.name}, Station ID: {self.id}, ({self.lat}, {self.lon}), City: {self.city}, Commune: {self.city.commune} '
