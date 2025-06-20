import requests
from air_monitor.api_client.stations_get import get_stations_data
from air_monitor.api_client.sensors_get import get_sensors_data
from air_monitor.api_client.measurement_get import get_measurement_data
from air_monitor.api_client.aq_index_get import get_aq_index_data

__base_url = 'https://api.gios.gov.pl'
EXCLUDED_STATIONS = {355} #wyrzuca server error podczas pobierania

def fetch_all_data():
    """
    Funkcja pobiera dane z API GIOŚ
    :return: dict
    """

    with requests.Session() as s:
        stations = get_stations_data(s, __base_url)
        if not stations:
            return {}

        all_data = []

        for station in stations:
            station_id = station['station_id']
            if station_id not in EXCLUDED_STATIONS:
                sensors = get_sensors_data(s, station_id, __base_url)
            else:
                print(f"Station {station_id} is excluded from data fetching.")
            # sensors = get_sensors_data(s, station_id, __base_url)

            aq_index = get_aq_index_data(s, station_id, __base_url)

            station_entry = {
                'station': station,
                'aq_index': aq_index,
                'sensors': []
            }

            for sensor in sensors:
                sensor_id = sensor['detector_id']
                measurement = get_measurement_data(s, sensor_id, __base_url)

                sensor_entry = {
                    'sensor': sensor,
                    'measurement': measurement
                }
                station_entry['sensors'].append(sensor_entry)

            all_data.append(station_entry)

        if not all_data:
            return {'stations': []}
        return {'stations': all_data}


if __name__ == '__main__':
    x = fetch_all_data()
    # print(x)
