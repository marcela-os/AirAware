from typing import List, Dict
from air_monitor.models.sensors.model.sensor import Sensor
from air_monitor.models.sensors.model.parameters import Param


def converter_sensors(data):
    all_data = []
    parametry = {}

    if data.get('stations', []):
        for station_entry in data.get('stations', []):
            for detector_entry in station_entry.get('sensors', []):
                param = detector_entry['sensor']
                data = (param["indicator"], param["symbol"], param["code"], param["factor_id"])
                if data in parametry:
                    param_instancja = parametry[data]
                else:
                    param_instancja = Param(param["indicator"], param["symbol"], param["code"], param["factor_id"])
                    parametry[data] = param_instancja
                sensor = Sensor(param["detector_id"], param["station_id"], param_instancja)
                all_data.append(sensor)
    return all_data
