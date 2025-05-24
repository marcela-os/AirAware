"""
Measuring points
Zaprojektuj zestaw współpracujących klas koniecznych do opisania stanowisk pomiarowych
– klasę Param reprezentującą parametr pomiarowy
– klasę Sensor reprezentującą stanowisko pomiarowe (czujnik w danej stacji)
W klasach atrybuty zdefiniuj jako właściwości (properties)
Podobnie jak w poprzednim ćwiczeniu instancje, po ich utworzeniu, powinny być niemodyfikowalne
Utwórz funkcję, która przeniesie dane stanowisk pomiarowych znajdujące się w tej chwili w słownikach do instancji klas
Zadbaj o to, aby nie tworzyć wielu instancji o identycznym stanie
Pamiętaj także o zdefiniowaniu metody str , aby w czytelny sposób przedstawić
dane o stanowiskach pomiarowych

Zrealizuj analogiczne zapytania, jak w ćwiczeniu dodatkowym 2.2 z modułu PYTH DANE wykorzystując teraz model obiektowy
"""

stanowiska = [
    {
        "id": 6236,
        "stationId": 966,
        "param": {
            "paramName": "dwutlenek azotu",
            "paramFormula": "NO2",
            "paramCode": "NO2",
            "idParam": 6
        }
    },
    {
        "id": 6238,
        "stationId": 966,
        "param": {
            "paramName": "pył zawieszony PM10",
            "paramFormula": "PM10",
            "paramCode": "PM10",
            "idParam": 3
        }
    },
    {
        "id": 20586,
        "stationId": 966,
        "param": {
            "paramName": "tlenek węgla",
            "paramFormula": "CO",
            "paramCode": "CO",
            "idParam": 8
        }
    },
    {
        "id": 20587,
        "stationId": 966,
        "param": {
            "paramName": "benzen",
            "paramFormula": "C6H6",
            "paramCode": "C6H6",
            "idParam": 10
        }
    }
]

class Param:
    def __init__(self, name, formula, code, param_id):
        self.__name = name
        self.__formula = formula
        self.__code = code
        self.__param_id = param_id

    @property
    def name(self):
        return self.__name
    @property
    def formula(self):
        return self.__formula
    @property
    def code(self):
        return self.__code
    @property
    def param_id(self):
        return self.__param_id

    def __str__(self):
        return f'Name: {self.name}, Formula: {self.formula}, Code: {self.code}, ID: {self.param_id}'

class Sensor:
    def __init__(self, sensor_id, station_id, param):
        self.__sensor_id = sensor_id
        self.__station_id = station_id
        self.__param = param

    @property
    def sensor_id(self):
        return self.__sensor_id
    @property
    def station_id(self):
        return self.__station_id
    @property
    def param(self):
        return self.__param

    def __str__(self):
        return f'Sensor ID: {self.sensor_id}, Station ID: {self.station_id}, Param: ({self.param})'


def przeksztalc_dane(stanowiska):
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

    return lista_sensorow


sensory = przeksztalc_dane(stanowiska)

for s in sensory:
    print(s)

print("\nSensory NO2):")
for sensor in sensory:
    if sensor.param.formula == "NO2":
        print(sensor)