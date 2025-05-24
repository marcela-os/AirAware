class Data:
    def __init__(self, key, values):
        self.__key = key
        self.__values = tuple(values)

    @property
    def key(self):
        return self.__key
    @property
    def values(self):
        return self.__values

    def __str__(self):
        values_str = ", ".join([str(value) for value in self.__values])
        return f'Key: {self.__key}, Values: {values_str}'

    def __repr__(self):
        return f'Key: {self.__key}, Values: {self.__values}'