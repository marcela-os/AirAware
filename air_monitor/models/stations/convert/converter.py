"""
Moduł umożliwiający konwersję danych do modelu obiektowego
"""
from air_monitor.models.stations.model.stations import Station
from air_monitor.models.stations.model.city import City
from air_monitor.models.stations.model.commune import Commune


def converter_station(data):
    # print("Type of input:", type(data))

    # print('data_dict', data)
    stations = []
    if data.get('stations', []):
        for station_entry in data.get('stations', []):
            station = station_entry['station']
            commune = Commune(station['commune'], station['district'], station['province'])
            city = City(station['city_name'], station['city_id'], commune)
            station = Station(station['station_name'], station['station_id'], station['station_code'], station['lat'], station['long'], city)
            stations.append(station)

            # print(station)
        #     for data in data:
        #         commune_data = data['city']['commune']
        #         commune = Commune(commune_data['communeName'], commune_data['districtName'], commune_data['provinceName'])
        #         city = City(data['city']['name'], data['city']['id'], commune)
        #         station = Station(data['stationName'], data['id'], data['gegrLat'], data['gegrLon'], city)
        #         stations.append(station)
        #
        #     for station in stations:
        #         print('station',station)
    return stations

    # return [station for station in stations]
    # return Station(data_dict['stationName'], data_dict['id'], data_dict['latitude'], data_dict['longitude'] )


# return f'Station {self.name}, Station ID: {self.id}, ({self.lat}, {self.lon}), City: {self.city}, Commune: {self.city.commune} '
#     stations = []
#     parametry = {}
#
#     if data.get('stations', []):
#         for station_entry in data.get('stations', []):
#             for detector_entry in station_entry.get('sensors', []):
#                 param = detector_entry['sensor']
#                 data = (param["indicator"], param["symbol"], param["code"], param["factor_id"])
#                 if data in parametry:
#                     param_instancja = parametry[data]
#                 else:
#                     param_instancja = Param(param["indicator"], param["symbol"], param["code"], param["factor_id"])
#                     parametry[data] = param_instancja
#                 sensor = Sensor(param["detector_id"], param["station_id"], param_instancja)
#                 all_data.append(sensor)
#     return all_data