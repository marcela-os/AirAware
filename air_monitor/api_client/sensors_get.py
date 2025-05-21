import requests


def get_sensors_data(session, station_id, base_url):
    """
    Funkcja pobiera sensory pomiarowe dla konkretnej stacji.
    :param session: requests.Session
    :param station_id: id stacji
    :param base_url: url GIOŚ
    :return: dict
    """
    endpoint = f'{base_url}/pjp-api/v1/rest/station/sensors/{station_id}'
    try:
        response = session.get(endpoint, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Sensor download error for stations {station_id}:', e)
        return {}
