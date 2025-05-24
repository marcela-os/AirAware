"""
Moduł zawiera klase reprezentującą miasto.
"""
class City:
    """
    Klasa reprezentująca miasto.
    Zwraca string z nazwą miasta oraz id miasta.
    """
    def __init__(self, name, id, commune):
        self.__name = name
        self.__id = id
        self.__commune = commune

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def commune(self):
        return self.__commune

    def __str__(self):
        return f'{self.name}, City ID: {self.id}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.id}, {self.commune!r})"

    def __eq__(self, other):
        return isinstance(other, City) and (
            self.name, self.id
        ) == (other.name, other.id)

    def __hash__(self):
        return hash((self.name, self.id))