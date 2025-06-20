import pytest
from air_monitor.models.sensors.model import Sensor, Param
from air_monitor.models.sensors.convert.converter import converter_sensors

@pytest.fixture
def sample_param():
    return Param("arsen w PM10", "As(PM10)", "As(PM10)", 60)

@pytest.fixture
def sample_sensor(sample_param):
    return Sensor(652, 117, sample_param)


def test_sensor_property(sample_sensor):
    assert sample_sensor.sensor_id == 652
    assert sample_sensor.station_id == 117


def test_sensor_str(sample_sensor):
    result = str(sample_sensor)
    assert "Sensor ID: 652" in result
    assert "Station ID: 117" in result
    assert "arsen w PM10" in result
    assert "As(PM10)" in result
    assert "60" in result

def test_sensor_repr(sample_sensor):
    result = repr(sample_sensor)
    assert result.startswith("Sensor(652, 117,")
    assert "Param(arsen w PM10, As(PM10), As(PM10), 60)" in result


def test_sensor_equality(sample_param):
    s1 = Sensor(652, 117, sample_param)
    s2 = Sensor(652, 117, sample_param)
    s3 = Sensor(3, 11, sample_param)

    assert s1 == s2
    assert s1 != s3


def test_sensor_hash(sample_param):
    s1 = Sensor(652, 117, sample_param)
    s2 = Sensor(652, 117, sample_param)
    s3 = Sensor(3, 11, sample_param)

    assert hash(s1) == hash(s2)
    assert hash(s1) != hash(s3)
    assert hash(s1) != hash(sample_param)


@pytest.fixture
def sample_data():
    return {
        "stations": [
            {
                "sensors": [
                    {
                        "sensor": {
                            "detector_id": 101,
                            "station_id": 202,
                            "indicator": "PM10",
                            "symbol": "PM10",
                            "code": "PM10_code",
                            "factor_id": 1
                        }
                    }
                ]
            }
        ]
    }


def test_converter_returns_sensor_list(sample_data):
    sensors = converter_sensors(sample_data)

    assert isinstance(sensors, list)
    assert len(sensors) == 1

    sensor = sensors[0]
    assert isinstance(sensor, Sensor)
    assert sensor.sensor_id == 101
    assert sensor.station_id == 202

    param = sensor.param
    assert isinstance(param, Param)
    assert param.name == "PM10"
    assert param.formula == "PM10"
    assert param.code == "PM10_code"
    assert param.param_id == 1


def test_converter_empty_input():
    sensors = converter_sensors({})
    assert sensors == []


def test_converter_missing_sensors_key():
    data = {"stations": [{}]}  # brak klucza 'sensors'
    sensors = converter_sensors(data)
    assert sensors == []
