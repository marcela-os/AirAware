import pytest

import air_monitor.api_client.air_data as air_data

def test_fetch_all_data(monkeypatch):
    print("Start")

    monkeypatch.setattr(air_data, 'get_stations_data', lambda s, url: [
        {'station_id': 1, 'name': 'Station 1'}
    ])
    monkeypatch.setattr(air_data, 'get_sensors_data', lambda s, station_id, url: [
        {'detector_id': 10}
    ])
    monkeypatch.setattr(air_data, 'get_measurement_data', lambda s, sensor_id, url: {
        'value': 42
    })
    monkeypatch.setattr(air_data, 'get_aq_index_data', lambda s, station_id, url: {
        'station_id': station_id,
        'value_index': 1
    })

    result = air_data.fetch_all_data()
    print("Result:", result)


    assert 'stations' in result
    assert len(result['stations']) == 1
    station_data = result['stations'][0]
    assert station_data['station']['station_id'] == 1
    assert station_data['aq_index']['station_id'] == 1
    assert len(station_data['sensors']) == 1
    assert station_data['sensors'][0]['measurement']['value'] == 42
    # assert result['stations'] == []
    print("End")