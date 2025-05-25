"""
Funkcje pomocnicze
"""


def safe_get(data, field):
    """
    Funkcja sprawdza wartość z obiektu typu dict czy nie jest None, pustą listą,
    pustym stringiem lub pustym słownikiem i zwraca tę wartość, w przeciwnym wypadku zwraca string 'None'.
    :param data: dict
    :param field: klucz, którego wartość ma zostać pobrana
    :return: value lub 'None'
    """
    value = data.get(field)
    return value if value not in (None, [], '', {}) else 'None'

