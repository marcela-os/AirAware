import requests


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
        return response.json()
    except requests.exceptions.RequestException as e:
        print('Station download error:', e)
        return {}
