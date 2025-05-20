import requests


def get_aq_index_data(session, station_id, base_url):
    """
    Funkcja pobiera indeks jakości powietrza w danej stacji.
    :param session: requests.Session
    :param station_id: id stacji
    :param base_url: url GIOŚ
    :return: dict
    """
    endpoint = f'{base_url}/pjp-api/v1/rest/aqindex/getIndex/{station_id}'
    try:
        response = session.get(endpoint, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Air quality index download error for stations {station_id}:', e)
        return None
