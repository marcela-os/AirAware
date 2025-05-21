import requests


def get_aq_index_data(session, station_id, base_url):
    endpoint = f'{base_url}/pjp-api/v1/rest/aqindex/getIndex/{station_id}'
    try:
        response = session.get(endpoint, timeout=5)
        response.raise_for_status()

        raw_data = response.json()
        data = raw_data.get('AqIndex', {})

        def safe_get(field):
            value = data.get(field)
            # print(f"Field '{field}' = {value} ({type(value)})")
            return value if value not in (None, [], '', {}) else 'None'

        return {
            'value_index': safe_get('Wartość indeksu'),
            'category_name': safe_get('Nazwa kategorii indeksu'),
            'calc_date': safe_get('Data wykonania obliczeń indeksu'),
            'source_data_date': safe_get(
                'Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika st'),
            'critical_pollution_code': safe_get('Kod zanieczyszczenia krytycznego'),
        }

    except requests.exceptions.RequestException as e:
        print(f'Air quality index download error for station {station_id}:', e)
        return {}
