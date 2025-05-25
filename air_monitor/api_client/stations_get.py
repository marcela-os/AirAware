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
        try:
            data = response.json()
            if data.get('Lista stacji pomiarowych'):
                stations = data.get('Lista stacji pomiarowych')
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
        except AttributeError:
            print('JSON data is incorrect')
    except requests.exceptions.RequestException as e:
        print('API error:', e)
        return {}


