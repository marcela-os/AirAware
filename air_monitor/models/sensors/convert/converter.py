from air_monitor.models.sensors.model.sensor import Sensor
from air_monitor.models.sensors.model.parameters import Param


def converter_sensors(data):
    """
    Funkcja umożliwiająca konwersję danych do modelu obiektowego.
    :param data: dict
    :return: list[Sensor]
    """

    sensors = []
    parametry = {}

    if data.get('stations', []):
        for station_entry in data.get('stations', []):
            for detector_entry in station_entry.get('sensors', []):
                param = detector_entry['sensor']
                data = (param["indicator"], param["symbol"], param["code"], param["factor_id"])
                if data in parametry:
                    param_inst = parametry[data]
                else:
                    param_inst = Param(
                        param["indicator"],
                        param["symbol"],
                        param["code"],
                        param["factor_id"]
                    )
                    parametry[data] = param_inst
                sensor = Sensor(
                    param["detector_id"],
                    param["station_id"],
                    param_inst
                )
                sensors.append(sensor)
    return sensors
