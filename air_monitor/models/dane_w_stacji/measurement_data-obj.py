"""
 Zaprojektuj zestaw współpracujących klas koniecznych do opisania danych pomiarowych
– klasę Value reprezentującą pojedynczy pomiar
– klasę Data reprezentującą zestaw danych pomiarowych
W klasach atrybuty zdefiniuj jako właściwości (properties)
Dokonaj odpowiedniej konwersji typów danych, np.
– wartości pomiarowe powinny być liczbami
– rozważ także, czy nie zdefiniować osobnych właściwości dla daty (możesz użyć typu date) i czasu (typ time)
Podobnie, jak w poprzednim ćwiczeniu, instancje, po ich utworzeniu, powinny być niemodyfikowalne
Utwórz funkcję, która przeniesie dane pomiarowe znajdujące się w tej chwili w słownikach do instancji klas
Pamiętaj także o zdefiniowaniu metody str , aby w czytelny sposób przedstawić dane pomiarowe
Przetestuj działanie modelu obiektowego
Zrealizuj analogiczne zapytania, jak w ćwiczeniu dodatkowym 2.3 z modułu PYTH DANE
wykorzystując teraz model obiektowy
"""
from datetime import datetime, date, time

dane_pomiarowe = {
    "key": "C6H6",
    "values": [
            {
                "date": "2025-01-08 13:00:00",
                "value": None
            },
            {
                "date": "2025-01-08 12:00:00",
                "value": 0.4
            },
            {
                "date": "2025-01-08 11:00:00",
                "value": 0.36
            },
            {
                "date": "2025-01-08 10:00:00",
                "value": 0.38
            },
            {
                "date": "2025-01-08 09:00:00",
                "value": 0.4
            },
            {
                "date": "2025-01-08 08:00:00",
                "value": 0.45
            },
            {
                "date": "2025-01-08 07:00:00",
                "value": 0.34
            },
            {
                "date": "2025-01-08 06:00:00",
                "value": 0.23
            },
            {
                "date": "2025-01-08 05:00:00",
                "value": 0.22
            },
            {
                "date": "2025-01-08 04:00:00",
                "value": 0.23
            },
            {
                "date": "2025-01-08 03:00:00",
                "value": 0.22
            },
            {
                "date": "2025-01-08 02:00:00",
                "value": 0.22
            },
            {
                "date": "2025-01-08 01:00:00",
                "value": 0.26
            },
            {
                "date": "2025-01-08 00:00:00",
                "value": 0.36
            },
            {
                "date": "2025-01-07 23:00:00",
                "value": 0.48
            },
            {
                "date": "2025-01-07 22:00:00",
                "value": 0.54
            },
            {
                "date": "2025-01-07 21:00:00",
                "value": 0.73
            },
            {
                "date": "2025-01-07 20:00:00",
                "value": 0.76
            },
            {
                "date": "2025-01-07 19:00:00",
                "value": 0.51
            },
            {
                "date": "2025-01-07 18:00:00",
                "value": 0.6
            },
            {
                "date": "2025-01-07 17:00:00",
                "value": 0.8
            },
            {
                "date": "2025-01-07 16:00:00",
                "value": 0.78
            },
            {
                "date": "2025-01-07 15:00:00",
                "value": 0.41
            },
            {
                "date": "2025-01-07 14:00:00",
                "value": 0.38
            },
            {
                "date": "2025-01-07 13:00:00",
                "value": 0.39
            },
            {
                "date": "2025-01-07 12:00:00",
                "value": 0.41
            },
            {
                "date": "2025-01-07 11:00:00",
                "value": 0.49
            },
            {
                "date": "2025-01-07 10:00:00",
                "value": 0.56
            },
            {
                "date": "2025-01-07 09:00:00",
                "value": 0.52
            },
            {
                "date": "2025-01-07 08:00:00",
                "value": 0.33
            },
            {
                "date": "2025-01-07 07:00:00",
                "value": 0.29
            },
            {
                "date": "2025-01-07 06:00:00",
                "value": 0.21
            },
            {
                "date": "2025-01-07 05:00:00",
                "value": 0.22
            },
            {
                "date": "2025-01-07 04:00:00",
                "value": 0.25
            },
            {
                "date": "2025-01-07 03:00:00",
                "value": 0.31
            },
            {
                "date": "2025-01-07 02:00:00",
                "value": 0.28
            },
            {
                "date": "2025-01-07 01:00:00",
                "value": 0.4
            },
            {
                "date": "2025-01-07 00:00:00",
                "value": 0.45
            },
            {
                "date": "2025-01-06 23:00:00",
                "value": 0.52
            },
            {
                "date": "2025-01-06 22:00:00",
                "value": 0.64
            },
            {
                "date": "2025-01-06 21:00:00",
                "value": 0.61
        },
        {
            "date": "2025-01-06 20:00:00",
            "value": 0.66
        },
        {
            "date": "2025-01-06 19:00:00",
            "value": 1.1
        },
        {
            "date": "2025-01-06 18:00:00",
            "value": 1.01
        },
        {
            "date": "2025-01-06 17:00:00",
            "value": 0.62
        },
        {
            "date": "2025-01-06 16:00:00",
            "value": 0.75
        },
        {
            "date": "2025-01-06 15:00:00",
            "value": 0.94
        },
        {
            "date": "2025-01-06 14:00:00",
            "value": 1.3
        },
        {
            "date": "2025-01-06 13:00:00",
            "value": 1.59
        },
        {
            "date": "2025-01-06 12:00:00",
            "value": 2.2
        },
        {
            "date": "2025-01-06 11:00:00",
            "value": 1.37
        },
        {
            "date": "2025-01-06 10:00:00",
            "value": 1.12
        },
        {
            "date": "2025-01-06 09:00:00",
            "value": 1.08
        },
        {
            "date": "2025-01-06 08:00:00",
            "value": 1.07
        },
        {
            "date": "2025-01-06 07:00:00",
            "value": 1.12
        },
        {
            "date": "2025-01-06 06:00:00",
            "value": 1.18
        },
        {
            "date": "2025-01-06 05:00:00",
            "value": 1.23
        },
        {
            "date": "2025-01-06 04:00:00",
            "value": 1.18
        },
        {
            "date": "2025-01-06 03:00:00",
            "value": 1.13
        },
        {
            "date": "2025-01-06 02:00:00",
            "value": 1.07
        },
        {
            "date": "2025-01-06 01:00:00",
            "value": 0.99
        },
        {
            "date": "2025-01-06 00:00:00",
            "value": 0.94
        }
    ]
}

class Value:
    def __init__(self, date_value, value):
        self.__datetime = datetime.strptime(date_value, "%Y-%m-%d %H:%M:%S")
        self.__value = float(value) if value is not None else None

    @property
    def date(self):
        return self.__datetime.date()

    @property
    def time(self):
        return self.__datetime.time()

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return f'Date: {self.__datetime}, Value: {self.__value}'

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

def convert_dict_to_data(data_dict):
    key = data_dict["key"]
    value_objs = [Value(v["date"], v["value"]) for v in data_dict["values"]]
    return Data(key, value_objs)


# TEST
data_instance = convert_dict_to_data(dane_pomiarowe)
print(data_instance)
