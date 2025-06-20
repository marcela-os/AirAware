import pytest
from air_monitor.models.aq_index.model.value_aq import ValueAQ, DateFormat
from air_monitor.models.aq_index.model.aq_index import AqIndex
from air_monitor.models.aq_index.model.aq_index import DateFormat as DFormat
from air_monitor.models.aq_index.convert.converter import converter_aq_index


@pytest.fixture
def sample_value():
    return ValueAQ("SO2", "2025-06-19 09:00:00",
                   "2025-06-19 10:00:00", 0, "Bardzo dobry")

@pytest.fixture
def sample_aqindex(sample_value):
    return AqIndex( 52, 1, "Dobry", "2025-06-19 10:20:45",
                    "2025-06-19 09:00:00", "OZON", sample_value
    )


def test_aqindex_properties(sample_aqindex):
    assert sample_aqindex.station_id == 52
    assert sample_aqindex.name == "Dobry"
    assert sample_aqindex.value_index == 1
    assert sample_aqindex.critical_pollution_code == "OZON"
    assert isinstance(sample_aqindex.param, ValueAQ)
    assert sample_aqindex.param.name == "SO2"


def test_aqindex_invalid_date():
    with pytest.raises(DFormat):
        AqIndex(52, 1, "Dobry",  "invalid-date"
,
                "2025-06-19 09:00:00", "OZON", "Param")


def test_valueaq_properties(sample_value):
    assert sample_value.name == "SO2"
    assert sample_value.index_value == 0
    assert sample_value.cat_name == "Bardzo dobry"

def test_valueaq_invalid_date():
    with pytest.raises(DateFormat):
        ValueAQ("SO2", "invalid-date", "2025-06-19 10:00:00", 0, "Bardzo dobry")

def test_valueaq_invalid_value():
    with pytest.raises(ValueError):
        ValueAQ("SO2", "2025-06-19 09:00:00", "2025-06-19 10:00:00", "not-a-number", "Bardzo dobry")

def test_converter_aq_index():
    sample_data = {
        "stations": [
            {
                "aq_index": {
                    "station_id": 1,
                    "value_index": 5.5,
                    "category_name": "Dobry",
                    "calc_date": "2025-06-19 10:20:45",
                    "source_data_date": "2025-06-19 09:00:00",
                    "critical_pollution_code": "PM10",
                    "param": {
                        "PM10": {
                            "source_date": "2025-06-19 09:00:00",
                            "calcs_date": "2025-06-19 10:20:45",
                            "index_value": 5.5,
                            "index_category_name": "Dobry"
                        }
                    }
                }
            }
        ]
    }

    result = converter_aq_index(sample_data)
    assert isinstance(result, list)
    assert len(result) == 1
    aq_index_obj = result[0]
    assert isinstance(aq_index_obj, AqIndex)
    assert aq_index_obj.station_id == 1
    assert aq_index_obj.value_index == 5.5
    assert aq_index_obj.name == "Dobry"
    assert "PM10" in aq_index_obj.param
    value_obj = aq_index_obj.param["PM10"]
    assert isinstance(value_obj, ValueAQ)
    assert value_obj.name == "PM10"
    assert value_obj.index_value == 5.5
