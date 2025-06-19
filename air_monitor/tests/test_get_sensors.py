import pytest
import requests

from air_monitor.api_client.sensors_get import get_sensors_data

data = {
    "Lista stanowisk pomiarowych dla podanej stacji": [
        {
            "Identyfikator stanowiska": 652,
            "Identyfikator stacji": 117,
            "Wskaźnik": "arsen w PM10",
            "Wskaźnik - wzór": "As(PM10)",
            "Wskaźnik - kod": "As(PM10)",
            "Id wskaźnika": 60
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
    station_id = 101
    base_url = "https://fake-api.gov"

    result = get_sensors_data(session, station_id, base_url)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["detector_id"] == 652
    assert result[0]["station_id"] == 117
    assert result[0]["indicator"] == "arsen w PM10"
