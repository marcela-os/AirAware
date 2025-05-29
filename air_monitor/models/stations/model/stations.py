"""
Moduł zawiera klase reprezentującą daną stację.
"""
class Station:
    """
    Klasa reprezentująca stację.
    Zwraca string z nazwą stacji, id, szerokością geograficzną oraz informacjami o mieście i gminie.
    """
    def __init__(self, name, id, code, lat, lon, city):
        self.__name = name
        self.__id = id
        self.__code = code
        self.__lat = lat
        self.__lon = lon
        self.__city = city

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def code(self):
        return self.__code

    @property
    def lat(self):
        return self.__lat

    @property
    def lon(self):
        return self.__lon

    @property
    def city(self):
        return self.__city

    def __str__(self):
        return (f'Station {self.name}, Station ID: {self.id}, Station code: {self.code} Geo: ({self.lat}, {self.lon}), '
                f'City: {self.city}')

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.id}, {self.code}, {self.lat}, {self.lon}, City: {self.city!r})"

    def __eq__(self, other):
        return isinstance(other, Station) and (
            self.name, self.id, self.code, self.lat, self.lon, self.city, self.city.commune
        ) == (other.name, other.id, other.code, other.lat, other.lon, other.city)

    def __hash__(self):
        return hash((self.name, self.id, self.code, self.lat, self.lon, self.city))