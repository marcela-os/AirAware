"""
Moduł zawiera klase reprezentującą gminę.
"""


class Commune:
    """
    Klasa reprezentująca gminę.
    Zwraca string z nazwą gminy, powiatem i województwem.
    """

    def __init__(self, name, district, province):
        self.__name = name
        self.__district = district
        self.__province = province

    @property
    def name(self):
        return self.__name

    @property
    def district(self):
        return self.__district

    @property
    def province(self):
        return self.__province

    def __str__(self):
        return f'{self.name}, District: {self.district}, Province: {self.province.capitalize()}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.district}', '{self.province}')"

    def __eq__(self, other):
        return isinstance(other, Commune) and (
            self.name, self.district, self.province
        ) == (other.name, other.district, other.province)

    def __hash__(self):
        return hash((self.name, self.district, self.province))

