import requests
from air_monitor.api_client.stations_get import get_stations_data
from air_monitor.api_client.sensors_get import get_sensors_data
from air_monitor.api_client.measurement_get import get_measurement_data
from air_monitor.api_client.aq_index_get import get_aq_index_data

__base_url = 'https://api.gios.gov.pl'


def fetch_all_data():
    """
    Funkcja pobiera dane z API GIOŚ
    :return: dict
    """
    with requests.Session() as s:
        stations_response = get_stations_data(s, __base_url)
        stations = stations_response.get('Lista stacji pomiarowych', [])

        if not stations:
            return []

        all_data = []

        for station in stations:
            station_id = station['Identyfikator stacji']
            sensors_response = get_sensors_data(s, station_id, __base_url)
            sensors = sensors_response.get('Lista stanowisk pomiarowych dla podanej stacji', [])

            aq_index_response = get_aq_index_data(s, station_id, __base_url)
            aq_index = aq_index_response.get('AqIndex', {})

            station_entry = {
                'station': station,
                'aq_index': aq_index,
                'sensors': []
            }

            for sensor in sensors:
                sensor_id = sensor['Identyfikator stanowiska']
                measurement = get_measurement_data(s, sensor_id, __base_url)

                if 'Lista danych pomiarowych' in measurement:
                    measurement_data = measurement['Lista danych pomiarowych']
                elif 'error_result' in measurement:
                    measurement_data = measurement['error_result']
                else:
                    measurement_data = None

                sensor_entry = {
                    'sensor': sensor,
                    'measurement': measurement_data
                }
                station_entry['sensors'].append(sensor_entry)

            all_data.append(station_entry)

        return {'stations': all_data}


if __name__ == '__main__':
    x = fetch_all_data()
    print(x)
