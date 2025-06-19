import pytest
import requests

from air_monitor.api_client.measurement_get import get_measurement_data

data = {
    "Lista danych pomiarowych": [
        {
            "Kod stanowiska": "DsCzerStraza-O3-1g",
            "Data": "2025-06-19 19:00:00",
            "Wartość": 94
        }
    ]
}

class MyResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return data

def fake_get(url, *args, **kwargs):
    return MyResponse()

def test_get_sensors_data(monkeypatch):
    monkeypatch.setattr(requests, "get", fake_get)

    class FakeSession:
        def get(self, *args, **kwargs):
            return requests.get(*args, **kwargs)

    session = FakeSession()
    sensor_id = 117
    base_url = "https://fake-api.gov"

    result = get_measurement_data(session, sensor_id, base_url)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["position_code"] == "DsCzerStraza-O3-1g"
    assert result[0]["date"] == "2025-06-19 19:00:00"
    assert result[0]["value"] == 94
