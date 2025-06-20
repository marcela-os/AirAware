""" Funkcje mapujące """

from datetime import datetime

def map_detectors_to_stations(stations, detectors):
    """
    Tworzy słownik z stacjami i przypisanymi do nich detektorami.
    :param stations: list
    :param detectors: list
    :return: dict
    """

    station_detector_map = {}
    for station_name, station_id, lat, long in stations:
        station_detector_map[station_name] = [
            {
                "detector_id": detector_id,
                "indicator": indicator,
                "symbol": symbol
            }
            for sid, detector_id, indicator, symbol in detectors
            if sid == station_id
        ]
    return station_detector_map


def get_detector_id_by_indicator(station_name, indicator, station_detector_map):
    """
    Zwraca ID detektora dla danego wskaźnika i stacji.
    :param station_name: str
    :param indicator: str
    :param station_detector_map: dict
    :return: int | None
    """

    detectors = station_detector_map[station_name]
    for d in detectors:
        if d["indicator"] == indicator:
            return d["detector_id"]
    return None

def get_measurements_for_detector(detector_id, measurements):
    """
    Wyszukuje najnowsze pomiary dla danego detektora.
    :param detector_id: int
    :param measurements: list
    :return: list
    """

    # Dane odpowiadające danemu detektorowi
    ms_data = [(date, value) for d_id, date, value in measurements if d_id == detector_id]

    if not ms_data:
        return []

    # Zamiana daty ze stringa
    parsed_data = [(datetime.strptime(dt, "%Y-%m-%d %H:%M:%S"), val) for dt, val in ms_data]
    if not parsed_data:
        return []

    # Dzisiejsza data
    max_date = max(date.date() for date, _ in parsed_data)
    # Dane z najnowszą datą
    new_result = [
        (date, val)
        for date, val in parsed_data
        if date.date() == max_date
    ]
    return new_result