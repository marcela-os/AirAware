import pytest
import requests

from air_monitor.api_client.aq_index_get import get_aq_index_data

data = {
    "AqIndex": {
        "Identyfikator stacji pomiarowej": 52,
        "Data wykonania obliczeń indeksu": "2025-06-19 10:20:45",
        "Wartość indeksu": 1,
        "Nazwa kategorii indeksu": "Dobry",
        "Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika st": "2025-06-19 09:00:00",
        "Data wykonania obliczeń indeksu dla wskaźnika SO2": "2025-06-19 10:20:45",
        "Wartość indeksu dla wskaźnika SO2": 0,
        "Nazwa kategorii indeksu dla wskażnika SO2": "Bardzo dobry",
        "Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika SO2": "2025-06-19 10:00:00",
        "Data wykonania obliczeń indeksu dla wskaźnika NO2": "2025-06-19 10:20:45",
        "Wartość indeksu dla wskaźnika NO2": 0,
        "Nazwa kategorii indeksu dla wskażnika NO2": "Bardzo dobry",
        "Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika NO2": "2025-06-19 10:00:00",
        "Data wykonania obliczeń indeksu dla wskaźnika PM10": "2025-06-19 10:20:45",
        "Wartość indeksu dla wskaźnika PM10": 1,
        "Nazwa kategorii indeksu dla wskażnika PM10": "Dobry",
        "Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika PM10": "2025-06-19 09:00:00",
        "Data wykonania obliczeń indeksu dla wskaźnika PM2.5": "2025-06-19 10:20:45",
        "Wartość indeksu dla wskaźnika PM2.5": None,
        "Nazwa kategorii indeksu dla wskażnika PM2.5": None,
        "Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika PM2.5": None,
        "Data wykonania obliczeń indeksu dla wskaźnika O3": "2025-06-19 10:20:45",
        "Wartość indeksu dla wskaźnika O3": 0,
        "Nazwa kategorii indeksu dla wskażnika O3": "Bardzo dobry",
        "Data danych źródłowych, z których policzono wartość indeksu dla wskaźnika O3": "2025-06-19 10:00:00",
        "Status indeksu ogólnego dla stacji pomiarowej": True,
        "Kod zanieczyszczenia krytycznego": "OZON"
    }
}


class MyResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return data

def fake_get(url, *args, **kwargs):
    return MyResponse()

def test_get_aq_index_data(monkeypatch):
    monkeypatch.setattr(requests, "get", fake_get)

    class FakeSession:
        def get(self, *args, **kwargs):
            return requests.get(*args, **kwargs)

    session = FakeSession()
    station_id = 52
    base_url = "https://fake-api.gov"

    result = get_aq_index_data(session, station_id, base_url)

    assert isinstance(result, dict)
    assert result["station_id"] == 52
    assert result["value_index"] == 1
    assert result["category_name"] == "Dobry"
    assert result["calc_date"] == "2025-06-19 10:20:45"
    assert result["source_data_date"] == "2025-06-19 09:00:00"
    assert result["critical_pollution_code"] == "OZON"
    assert result["param"]["SO2"]["source_date"] == "2025-06-19 10:00:00"
    assert result["param"]["SO2"]["calcs_date"] == "2025-06-19 10:20:45"
    assert result["param"]["SO2"]["index_value"] == 0
    assert result["param"]["SO2"]["index_category_name"] == "Bardzo dobry"
    assert result["param"]["PM2.5"]["source_date"] is None
    assert result["param"]["PM2.5"]["calcs_date"] == "2025-06-19 10:20:45"
    assert result["param"]["PM2.5"]["index_value"] is None
    assert result["param"]["PM2.5"]["index_category_name"] is None

