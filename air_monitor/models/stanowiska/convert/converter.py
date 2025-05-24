from typing import List, Dict
from python07.extra.stanowiska.model import Param
from python07.extra.stanowiska.model import Sensor


def przeksztalc_dane(stanowiska: List[Dict]) -> List[Sensor]:
    lista_sensorow = []
    parametry = {}

    for sensor in stanowiska:
        p = sensor["param"]
        data = (p["paramName"], p["paramFormula"], p["paramCode"], p["idParam"])

        if data in parametry:
            param_instancja = parametry[data]
        else:
            param_instancja = Param(p["paramName"], p["paramFormula"], p["paramCode"], p["idParam"])
            parametry[data] = param_instancja

        sensor = Sensor(sensor["id"], sensor["stationId"], param_instancja)
        lista_sensorow.append(sensor)
        # print(lista_sensorow)

    return lista_sensorow