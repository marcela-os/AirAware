class Sensor:
    """
    Klasa reprezentuje sensor przypisany do stacji i parametru pomiarowego.
    """

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

    def __repr__(self):
        return f'{self.__class__.__name__}({self.sensor_id}, {self.station_id}, {self.param!r})'

    def __eq__(self, other):
        return self.sensor_id == other.sensor_id and self.station_id == other.station_id and self.param == other.param

    def __hash__(self):
        return hash((self.sensor_id, self.station_id, self.param))