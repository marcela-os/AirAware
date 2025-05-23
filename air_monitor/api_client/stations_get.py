import requests
from air_monitor.utils.helpers import safe_get


def get_stations_data(session, base_url):
    """
    Funkcja pobiera stacje pomiarowe.
    :param session: requests.Session
    :param base_url: url GIOŚ
    :return: dict
    """
    endpoint = f'{base_url}/pjp-api/v1/rest/station/findAll'
    try:
        response = session.get(endpoint, timeout=5)
        response.raise_for_status()
        stations = response.json().get('Lista stacji pomiarowych')
        # print("Stacje:", stations)
        # print("Typ pierwszej stacji:", type(stations[0]))
        # print("Zawartość pierwszej stacji:", stations[0])
        # return {
        #     'station_id': safe_get(data, 'Identyfikator stacji'),
        #     'station_code': safe_get(data, 'Kod stacji'),
        #     'station_name': safe_get(data, 'Nazwa stacji'),
        #     'lat': safe_get(data,'WGS84 φ N'),
        #     'long': safe_get(data, 'WGS84 λ E'),
        #     'city_name': safe_get(data, 'Nazwa miasta'),
        #     'city_id': safe_get(data, 'Identyfikator miasta'),
        #     'commune': safe_get(data, 'Gmina'),
        #     'district': safe_get(data, 'Powiat'),
        #     'province': safe_get(data, 'Województwo'),
        #     'street': safe_get(data, 'Ulica'),
        #
        # }
        #
        processed_stations = []
        for station in stations:
            station_info = {
                'station_id': safe_get(station, 'Identyfikator stacji'),
                'station_code': safe_get(station, 'Kod stacji'),
                'station_name': safe_get(station, 'Nazwa stacji'),
                'lat': safe_get(station, 'WGS84 φ N'),
                'long': safe_get(station, 'WGS84 λ E'),
                'city_name': safe_get(station, 'Nazwa miasta'),
                'city_id': safe_get(station, 'Identyfikator miasta'),
                'commune': safe_get(station, 'Gmina'),
                'district': safe_get(station, 'Powiat'),
                'province': safe_get(station, 'Województwo'),
                'street': safe_get(station, 'Ulica'),
            }

            processed_stations.append(station_info)

        return processed_stations
    except requests.exceptions.RequestException as e:
        print('Station download error:', e)
        return {}
