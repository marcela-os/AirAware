import requests
from air_monitor.utils.helpers import safe_get


def get_aq_index_data(session, station_id, base_url):
    endpoint = f'{base_url}/pjp-api/v1/rest/aqindex/getIndex/{station_id}'
    try:
        response = session.get(endpoint, timeout=10)
        response.raise_for_status()

        raw_data = response.json()
        data = raw_data.get('AqIndex', {})
        try:
            aq_index = {
                'station_id': safe_get(data, 'Identyfikator stacji pomiarowej'),
                'value_index': safe_get(data, 'Wartość indeksu'),
                'category_name': safe_get(data, 'Nazwa kategorii indeksu'),
                'calc_date': safe_get(data, 'Data wykonania obliczeń indeksu'),
                'source_data_date': safe_get(data,
                                             'Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika st'),
                'critical_pollution_code': safe_get(data, 'Kod zanieczyszczenia krytycznego'),
                'param': {
                    'SO2': {
                        'source_date': safe_get(data,
                                                'Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika SO2'),
                        'calcs_date': safe_get(data, 'Data wykonania obliczeń indeksu dla wskaźnika SO2'),
                        'index_value': safe_get(data, 'Wartość indeksu dla wskaźnika SO2'),
                        'index_category_name': safe_get(data, 'Nazwa kategorii indeksu dla wskażnika SO2')
                    },
                    'NO2': {
                        'source_date': safe_get(data,
                                                'Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika NO2'),
                        'calcs_date': safe_get(data, 'Data wykonania obliczeń indeksu dla wskaźnika NO2'),
                        'index_value': safe_get(data, 'Wartość indeksu dla wskaźnika NO2'),
                        'index_category_name': safe_get(data, 'Nazwa kategorii indeksu dla wskażnika NO2')
                    },
                    'PM10': {
                        'source_date': safe_get(data,
                                                'Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika PM10'),
                        'calcs_date': safe_get(data, 'Data wykonania obliczeń indeksu dla wskaźnika PM10'),
                        'index_value': safe_get(data, 'Wartość indeksu dla wskaźnika PM10'),
                        'index_category_name': safe_get(data, 'Nazwa kategorii indeksu dla wskażnika PM10')
                    },
                    'PM2.5': {
                        'source_date': safe_get(data,
                                                'Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika PM2.5'),
                        'calcs_date': safe_get(data, 'Data wykonania obliczeń indeksu dla wskaźnika PM2.5'),
                        'index_value': safe_get(data, 'Wartość indeksu dla wskaźnika PM2.5'),
                        'index_category_name': safe_get(data, 'Nazwa kategorii indeksu dla wskażnika PM2.5')
                    },
                    'O3': {
                        'source_date': safe_get(data,
                                                'Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika O3'),
                        'calcs_date': safe_get(data, 'Data wykonania obliczeń indeksu dla wskaźnika O3'),
                        'index_value': safe_get(data, 'Wartość indeksu dla wskaźnika O3'),
                        'index_category_name': safe_get(data, 'Nazwa kategorii indeksu dla wskażnika O3')
                    }
                }
            }

            return aq_index
        except (ValueError, TypeError, KeyError) as data_err:
            print(f"API data error while processing AQ index: {data_err}")
            return {}

    except requests.exceptions.RequestException as e:
        print(f'Air quality index download error for station {station_id}:', e)
        return {}
