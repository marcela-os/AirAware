import requests


def get_measurement_data(session, sensor_id, base_url):
    """
    Funkcja pobiera dane pomiarowe z sensora.
    :param session: requests.Session
    :param sensor_id: id sensora
    :param base_url: url GIOŚ
    :return: dict
    """
    endpoint = f'{base_url}/pjp-api/v1/rest/data/getData/{sensor_id}'
    try:
        response = session.get(endpoint, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Measurement download error for sensor {sensor_id}:', e)
        return None