import pytest
from air_monitor.models.measurement.model import Data, Value
from air_monitor.models.measurement.model.value import DateFormat
from air_monitor.models.measurement.convert.converter import converter_measurement

@pytest.fixture
def sample_value():
    return Value("2025-06-19 19:00:00", "DsCzerStraza-O3-1g", 94)

@pytest.fixture
def sample_data(sample_value):
    return Data(11, [sample_value])


def test_data_property(sample_data):
    assert sample_data.key == 11
    assert isinstance(sample_data.values, tuple)
    assert len(sample_data.values) == 1
    assert isinstance(sample_data.values[0], Value)


def test_data_str(sample_data):
    result = str(sample_data)
    assert "key=11" in result
    assert "2025-06-19 19:00:00" in result
    assert "DsCzerStraza-O3-1g" in result
    assert "94.0" in result


def test_data_repr(sample_data):
    result = repr(sample_data)
    assert result.startswith("Key: 11")
    assert "2025-06-19 19:00:00" in result
    assert "DsCzerStraza-O3-1g" in result
    assert "94.0" in result

def test_value_with_invalid_date():
    with pytest.raises(DateFormat):
        Value("19-06-2025", "ABC", 10)


def test_converter_measurement():
    input_data = {
        "stations": [
            {
                "sensors": [
                    {
                        "sensor": {"detector_id": 101},
                        "measurement": [
                            {"date": "2025-06-19 12:00:00", "position_code": "XYZ-1", "value": 42.5}
                        ]
                    }
                ]
            }
        ]
    }

    result = converter_measurement(input_data)
    assert len(result) == 1
    assert isinstance(result[0], Data)
    assert result[0].key == 101
    assert len(result[0].values) == 1
    assert isinstance(result[0].values[0], Value)
    assert result[0].values[0].value == 42.5


def test_converter_measurement_ignores_missing_measurements_or_detector_id():
    input_data = {
        "stations": [
            {
                "sensors": [
                    {"sensor": {}, "measurement": []},  # brak detector_id i pomiarów
                    {"sensor": {"detector_id": 102}}    # brak measurement
                ]
            }
        ]
    }

    result = converter_measurement(input_data)
    assert result == []