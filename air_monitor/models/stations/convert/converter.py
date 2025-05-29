from air_monitor.models.stations.model.stations import Station
from air_monitor.models.stations.model.city import City
from air_monitor.models.stations.model.commune import Commune


def converter_station(data):
    """
    Funkcja umożliwiająca konwersję danych do modelu obiektowego.
    :param data: dict
    :return: list[Station]
    """

    stations = []
    if data.get('stations', []):
        for station_entry in data.get('stations', []):
            station_data = station_entry['station']
            commune = Commune(
                station_data['commune'],
                station_data['district'],
                station_data['province']
            )
            city = City(
                station_data['city_name'],
                station_data['city_id'],
                station_data['street'],
                commune)
            station = Station(
                station_data['station_name'],
                station_data['station_id'],
                station_data['station_code'],
                station_data['lat'],
                station_data['long'],
                city)
            stations.append(station)
    return stations
