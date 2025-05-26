from air_monitor.models.measurment.model.data import Data
from air_monitor.models.measurment.model.value import Value


def converter_measurment(data):
    """
    Funkcja umożliwiająca konwersję danych do modelu obiektowego.
    :param data: dict
    :return: list[Value]
    """

    measurment = []
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
                    value_obj = Value(
                        v["date"],
                        v["position_code"],
                        v["value"]
                    )
                    values.append(value_obj)
                if values:
                    data_obj = Data(
                        detector_id,
                        values
                    )
                    measurment.append(data_obj)

    return measurment
