import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import Icon
from taipy import Config
import sqlite3
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime
from types import SimpleNamespace

# Aktualna data
x = datetime.now().date()

dates = [
    datetime(2024, 1, 1),
    datetime(2025, 1, 1),
]
# Początkowy pusty wykres
display_figure = go.Figure()


def fetch_stations():
    """
    Pobiera wszystkie stacje z bazy danych.
    :return: list
    """

    with sqlite3.connect("air_monitor/database/air.db") as conn:
        all_stations = pd.read_sql_query("SELECT name, station_id FROM stations", conn)
    return all_stations.values.tolist()


def fetch_detectors():
    """
    Pobiera wszystkie detektory z bazy danych.
    :return: list
    """

    with sqlite3.connect("air_monitor/database/air.db") as conn:
        all_detectors = pd.read_sql_query("SELECT station_id, detector_id, indicator, symbol FROM detectors", conn)
        return all_detectors.values.tolist()


def fetch_measurements():
    """
    Pobiera wszystkie pamiary z bazy danych.
    :return: list
    """

    with sqlite3.connect("air_monitor/database/air.db") as conn:
        all_measurements = pd.read_sql_query("SELECT detector_id, date, value  FROM measurements", conn)
        return all_measurements.values.tolist()


# Ładowanie danych z bazy
detectors = fetch_detectors()
stations = fetch_stations()
measurements = fetch_measurements()


def map_detectors_to_stations(stations, detectors):
    """
    Tworzy słownik z stacjami i przypisanymi do nich detektorami.
    :param stations: list
    :param detectors: list
    :return: dict
    """

    station_detector_map = {}
    for station_name, station_id in stations:
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


station_detector_map = map_detectors_to_stations(stations, detectors)


def get_detector_id_by_indicator(station_name, indicator):
    """
    Zwraca ID detektora dla danego wskaźnika i stacji.
    :param station_name: str
    :param indicator: str
    :return: int | None
    """

    detectors = station_detector_map[station_name]
    for d in detectors:
        if d["indicator"] == indicator:
            return d["detector_id"]
    return None


def get_measurements_for_detector(detector_id):
    """
    Wyszukuje najnowsze pomiary dla danego detektora.
    :param detector_id: int
    :return: list
    """

    # Dane odpowiadające danemu detektorowi
    ms_data = [(date, value) for d_id, date, value in measurements if d_id == detector_id]
    # Zamiana daty ze stringa
    parsed_data = [(datetime.strptime(dt, "%Y-%m-%d %H:%M:%S"), val) for dt, val in ms_data]
    # Dzisiejsza data
    max_date = max(date.date() for date, _ in parsed_data)
    # Dane z najnowszą datą
    new_result = [
        (date, val)
        for date, val in parsed_data
        if date.date() == max_date
    ]
    return new_result


# Inicjalizacja danych globalnych
# Lista stacji do dropdowna
station_names = [name for name, _ in stations]
# Domyślna stacja
first_station = station_names[0] if station_names else None
# Lista detektorów dla domyślnej stacji
default_detectors = station_detector_map[first_station]
# Wybrana stacja
selected_station = first_station
# Dostępne detektory
available_detectors = [d["indicator"] for d in default_detectors]
# Wybrany detektor
selected_detector = available_detectors[0] if available_detectors else None


# Tymczasowy obiekt stanu z domyślnymi wartościami
initial_state = SimpleNamespace(
    selected_station=selected_station,
    selected_detector=selected_detector,
    display_figure=display_figure
)


def on_station_change(state):
    """
    Obsługuje zmianę wybranej stacji.
    :param state: Obiekt stanu GUI.
    :return: None
    """
    station_name = state.selected_station
    state.available_detectors = [d["indicator"] for d in station_detector_map[station_name]]
    state.selected_detector = state.available_detectors[0] if state.available_detectors else None

    # Aktualizacja wykresu po zmianie stacji
    on_detector_change(state)


def on_detector_change(state):
    """
    Aktualizuje wykres na podstawie wybranego detektora.
    :param state: Obiekt stanu GUI.
    :return: None
    """
    station_name = state.selected_station
    selected_indicator = state.selected_detector
    # Pobierz odpowiedni detector_id
    detector_id = get_detector_id_by_indicator(station_name, selected_indicator)

    # Pobierz dane pomiarowe dla tego detektora
    data = get_measurements_for_detector(detector_id)

    # Jeśli brak danych, zwróć pusty wykres -> TODO zwróć info o braku danych lub załaduj starsza dane
    if not data:
        state.display_figure = go.Figure()
        return

    x = [d[0] for d in data]
    y = [d[1] for d in data]

    figure = go.Figure()
    figure.add_trace(go.Scatter(
        x=x,
        y=y,
        name=str(detector_id),
        # showlegend=False,

    ))
    figure.update_layout(title=f"Wykres dla detektora: {selected_indicator} ({detector_id})")
    # figure.update_layout(legend_title_text="Contestant")
    figure.update_xaxes(title_text="Data pomiaru")
    figure.update_yaxes(title_text="Wartość")

    state.display_figure = figure

# Generowanie pierwszego wykresu
on_detector_change(initial_state)

display_figure = initial_state.display_figure


# Tworzenie strony GUI
with tgb.Page() as page:
    with tgb.part("text-center"):
        tgb.image("assets/logo.png", width="10vw")
        tgb.text("# S&P 500 Stock Value Over Time",
                 mode="md")
        tgb.date_range(
            "{dates}",
            label_start="Start Date",
            label_end="End Date"
        )
        with tgb.layout("20 80"):
            tgb.selector(label="Stacja",
                         class_name="fullwidth",
                         value="{selected_station}",
                         lov="{station_names}",
                         on_change="on_station_change",
                         dropdown=True)
            tgb.selector(label="detectors",
                         class_name="fullwidth",
                         value="{selected_detector}",
                         lov="{available_detectors}",
                         on_change="on_detector_change",
                         dropdown=True)
        tgb.chart(figure="{display_figure}")
        with tgb.layout("5 5 5 5 5"):
            tgb.image("assets/logo.png", width="3vw")
            tgb.text("Test")

if __name__ == "__main__":
    # Uruchomienie GUI
    gui = tp.Gui(page)

    gui.run(title="Air Monitor",
            use_reloader=True, port="auto")
