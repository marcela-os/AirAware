import pytest
from air_monitor.models.stations.model import Station, City, Commune
from air_monitor.models.stations.convert.converter import converter_station

@pytest.fixture
def sample_commune():
    return Commune("Gmina Testowa", "Powiat Testowy", "województwo testowe")

@pytest.fixture
def sample_city(sample_commune):
    return City("Miasto Testowe", 999, "Ulica Testowa", sample_commune)

@pytest.fixture
def sample_station(sample_city):
    return Station("Stacja Testowa", 123, "ST123", 51.123, 17.456, sample_city)


def test_station_properties(sample_station, sample_city):
    assert sample_station.name == "Stacja Testowa"
    assert sample_station.id == 123
    assert sample_station.code == "ST123"
    assert sample_station.lat == 51.123
    assert sample_station.lon == 17.456
    assert sample_station.city == sample_city
    assert sample_station.city.commune.name == "Gmina Testowa"


def test_station_str(sample_station):
    result = str(sample_station)
    assert "Station Stacja Testowa" in result
    assert "Station ID: 123" in result
    assert "Geo: (51.123, 17.456)" in result
    assert "City: " in result


def test_station_repr(sample_station):
    result = repr(sample_station)
    assert "Station" in result
    assert "City:" in result


def test_station_equality(sample_city):
    s1 = Station("Stacja A", 1, "ST001", 50.0, 20.0, sample_city)
    s2 = Station("Stacja A", 1, "ST001", 50.0, 20.0, sample_city)
    s3 = Station("Inna Stacja", 2, "ST002", 51.0, 21.0, sample_city)

    assert s1 == s2
    assert s1 != s3


def test_station_hash(sample_city):
    s1 = Station("Stacja A", 1, "ST001", 50.0, 20.0, sample_city)
    s2 = Station("Stacja A", 1, "ST001", 50.0, 20.0, sample_city)
    s3 = Station("Inna", 99, "DIFF", 0.0, 0.0, sample_city)

    assert hash(s1) == hash(s2)
    assert hash(s1) != hash(s3)
    assert hash(s1) != hash(sample_city)

@pytest.fixture
def sample_data():
    return {
        "stations": [
            {
                "station": {
                    "station_name": "Stacja Testowa",
                    "station_id": 101,
                    "station_code": "ST101",
                    "lat": 51.1,
                    "long": 17.0,
                    "city_name": "Miasto Testowe",
                    "city_id": 1001,
                    "street": "Testowa 1",
                    "commune": "Gmina Testowa",
                    "district": "Powiat Testowy",
                    "province": "Testowe"
                }
            }
        ]
    }

def test_converter_returns_station_object(sample_data):
    stations = converter_station(sample_data)
    assert isinstance(stations, list)
    assert len(stations) == 1
    station = stations[0]
    assert isinstance(station, Station)
    assert station.name == "Stacja Testowa"
    assert station.lat == 51.1
    assert station.city.name == "Miasto Testowe"
    assert station.city.commune.province == "Testowe"

def test_converter_empty_list_when_no_stations():
    assert converter_station({"stations": []}) == []

def test_converter_empty_list_when_no_key():
    assert converter_station({}) == []