from air_monitor.models.measurment.model.data import Data
from air_monitor.models.measurment.model.value import Value


def convert_dict_to_data(data):
    all_data = []
    if data.get('stations', []):
        for station_entry in data.get('stations', []):
            for detector_entry in station_entry.get('sensors', []):
                detector = detector_entry['sensor']
                measurement_data = detector_entry.get('measurement', [])
                detector_id = detector.get("detector_id")
                if not detector_id or not measurement_data:
                    continue
                values = []
                for v in measurement_data:
                    value_obj = Value(v["date"], v["position_code"], v["value"])
                    values.append(value_obj)
                if values:
                    data_obj = Data(detector_id, values)
                    all_data.append(data_obj)

    return all_data
