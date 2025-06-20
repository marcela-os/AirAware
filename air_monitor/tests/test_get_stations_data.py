import pytest
import requests

from air_monitor.api_client.stations_get import get_stations_data

data = {
    "Lista stacji pomiarowych": [
        {
            "Identyfikator stacji": 101,
            "Kod stacji": "ABC123",
            "Nazwa stacji": "Testowa",
            "WGS84 φ N": 50.061,
            "WGS84 λ E": 19.938,
            "Nazwa miasta": "Kraków",
            "Identyfikator miasta": 1001,
            "Gmina": "Kraków",
            "Powiat": "Krakowski",
            "Województwo": "małopolskie",
            "Ulica": "ul. Testowa"
        }
    ]
}


class MyResponse:
    def raise_for_status(self):
        pass

    def json(self):
        print('\nmonkeypatch json')
        return data

def fake_get(url, *args, **kwargs):
    print(f'\nmonkeypatch get called with URL: {url}')
    return MyResponse()

def test_get_stations_data(monkeypatch):
    monkeypatch.setattr(requests, "get", fake_get)

    class FakeSession:
        def get(self, *args, **kwargs):
            return requests.get(*args, **kwargs)

    session = FakeSession()

    base_url = "https://fake-api.gov"
    result = get_stations_data(session, base_url)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["station_name"] == "Testowa"
    assert result[0]["lat"] == 50.061
    assert result[0]["province"] == "małopolskie"


