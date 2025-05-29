"""
Moduł zawiera klase reprezentującą miasto.
"""
class City:
    """
    Klasa reprezentująca miasto.
    Zwraca string z nazwą miasta oraz id miasta.
    """
    def __init__(self, name, id, street, commune):
        self.__name = name
        self.__id = id
        self.__street = street
        self.__commune = commune

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def street(self):
        return self.__street

    @property
    def commune(self):
        return self.__commune

    def __str__(self):
        return f'{self.name}, City ID: {self.id}, City Street: {self.street} Commune: {self.commune}'

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.id}, {self.street}, {self.commune!r})"

    def __eq__(self, other):
        return isinstance(other, City) and (
            self.name, self.id, self.street
        ) == (other.name, other.id, other.street)

    def __hash__(self):
        return hash((self.name, self.id, self.street))