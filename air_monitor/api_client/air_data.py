import requests
from air_monitor.api_client.stations_get import get_stations_data
from air_monitor.api_client.sensors_get import get_sensors_data
from air_monitor.api_client.measurement_get import get_measurement_data
from air_monitor.api_client.aq_index_get import get_aq_index_data

__base_url = 'https://api.gios.gov.pl'


def main():
    """
    Funkcja pobiera listę stacji pomiarowych z API GIOŚ.
    """
    with requests.Session() as s:
        stations = get_stations_data(s, __base_url)
        stations = stations['Lista stacji pomiarowych']
        if stations:
            for station in stations[:3]:
                station_id = station['Identyfikator stacji']
                sensors = get_sensors_data(s, station_id, __base_url)
                sensors = sensors['Lista stanowisk pomiarowych dla podanej stacji']

                aq_index = get_aq_index_data(s, station_id, __base_url)
                aq_index = aq_index['AqIndex']

                print(f'Stacja {station_id}: {sensors}', sep='\n')
                print(f'Indeks jakości powietrza: {aq_index}')

                for sensor in sensors[:3]:
                    sensor_id = sensor['Identyfikator stanowiska']
                    measurement = get_measurement_data(s, sensor_id, __base_url)
                    measurement = measurement['Lista danych pomiarowych']

                    print(f'Dane pomiarowe: {measurement}')


if __name__ == '__main__':
    main()
