import requests
from air_monitor.utils.helpers import safe_get


def get_measurement_data(session, sensor_id, base_url):
    """
    Funkcja pobiera dane pomiarowe z sensora.
    :param session: requests.Session
    :param sensor_id: id sensora
    :param base_url: url GIOŚ
    :return: dict
    """
    endpoint = f'{base_url}/pjp-api/v1/rest/data/getData/{sensor_id}?size=20'
    try:
        response = session.get(endpoint, timeout=5)
        if response.json():
            raw_data = response.json()
            measurements = raw_data.get('Lista danych pomiarowych', {})
            processed_measurement = []
            for measurement in measurements:
                measurement_info = {
                    'position_code': safe_get(measurement, 'Kod stanowiska'),
                    'date': safe_get(measurement, 'Data'),
                    'value': safe_get(measurement, 'Wartość'),
                }

                processed_measurement.append(measurement_info)

            return processed_measurement
        else:
            raise ValueError("Response from API is not valid")
    except requests.exceptions.RequestException as e:
        print(f'Measurement download error for sensor {sensor_id}:', e)
        return {}
