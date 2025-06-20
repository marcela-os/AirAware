import requests
from air_monitor.utils.helpers import safe_get


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
        try:
            raw_data = response.json()
            sensors = raw_data.get('Lista stanowisk pomiarowych dla podanej stacji', {})
            processed_sensors = []
            for sensor in sensors:
                sensor_info = {
                    'detector_id': safe_get(sensor, 'Identyfikator stanowiska'),
                    'station_id': safe_get(sensor, 'Identyfikator stacji'),
                    'indicator': safe_get(sensor, 'Wskaźnik'),
                    'symbol': safe_get(sensor, 'Wskaźnik - wzór'),
                    'code': safe_get(sensor, 'Wskaźnik - kod'),
                    'factor_id': safe_get(sensor, 'Id wskaźnika'),
                }

                processed_sensors.append(sensor_info)

            return processed_sensors
        except (ValueError, TypeError, KeyError) as data_err:
            print(f"API data error while processing Sensors: {data_err}")
            return {}
    except requests.exceptions.RequestException as e:
        print(f'Sensor download error for stations {station_id}:', e)
        return {}
