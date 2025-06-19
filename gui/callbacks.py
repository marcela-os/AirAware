""" Funkcje reagujące na zmiany stanu GUI """

import plotly.graph_objs as go
import pandas as pd
import numpy as np

from air_monitor.utils.datastore import DataStore
from air_monitor.utils.nearest_stations import get_nearest_stations
from air_monitor.utils.logic import get_detector_id_by_indicator, get_measurements_for_detector
from taipy.gui import navigate


# Zmiana inputa
def on_input_change(state):
    """
    Aktualizuje dane na podstawie wpisanej stacji.
    :param state: Obiekt stanu GUI.
    :return: None
    """


    if not state.search_query.strip():
        state.filtered_locations = []
        state.nearest_station_list = ""
        return

    nearest = get_nearest_stations(state.search_query, 100, state.stations)

    # Lista podpowiedzi do selektora
    state.filtered_locations = [entry[1] for entry in nearest]

    # Pokazuj najbliższych stacji
    state.nearest_station_list = "\n".join([f"{dist:.1f} km - {name}" for dist, name in nearest[:5]])

# Zmiana selektora
def on_station_select(state):
    """
    Aktualizuje dane na podstawie wybranej stacji.
    :param state: Obiekt stanu GUI.
    :return: None
    """

    selected_name = state.selected_station
    query = state.search_query.strip()
    # Dopisz pierwsze słowo z nazwy stacji jeśli nie ma query
    if not state.search_query.strip():
        query = selected_name.strip().split()[0]

    if query:
        nearest = get_nearest_stations(query, 100, state.stations)
        match = next(((dist, name) for dist, name in nearest if name == selected_name), None)
        if match:
            dist, name = match
            for s_name, s_id, lat, long in state.stations:
                if s_name == name:
                    state.station_data = f"Wybrana stacja: {name}\n Odległość od '{query}': {dist:.2f} km\nWspółrzędne: {lat}, {long}"
                    state.filtered_locations = [entry[1] for entry in nearest]

                    # Pokazuj najbliższe stacje
                    state.nearest_station_list = [f"{dist:.1f} km - {name}" for dist, name in nearest[:5]]
                    return
        # Fallback: bez query albo nie znaleziono dystansu
    for s_name, s_id, lat, long in state.stations:
        if s_name == selected_name:
            state.station_data = f"Wybrana stacja: {s_name}\n Współrzędne: {lat}, {long}\n(Brak danych o odległości – wpisz lokalizację)"
            return

    state.station_data = "Nie znaleziono danych."

def on_station_change(state):
    """
    Obsługuje zmianę wybranej stacji.
    :param state: Obiekt stanu GUI.
    :return: None
    """
    station_name = state.selected_station
    # state.available_detectors = [d["indicator"] for d in station_detector_map[station_name]]
    state.available_detectors = [d["indicator"] for d in state.station_detector_map.get(station_name, [])]

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
    station_detector_map = state.station_detector_map
    # Pobierz odpowiedni detector_id
    detector_id = get_detector_id_by_indicator(station_name, selected_indicator, station_detector_map)

    # Pobierz dane pomiarowe dla tego detektora
    data = get_measurements_for_detector(detector_id, state.measurements)

    # Jeśli brak danych, zwróć pusty wykres -> TO DO zwróć info o braku danych lub załaduj starsza dane
    if not data:
        state.display_figure = go.Figure().add_annotation(
            text="Brak danych w danym dniu",
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=16)
        )
        return
    df = pd.DataFrame(data, columns=["time", "value"])

    max_row = df.loc[df['value'].idxmax()]
    min_row = df.loc[df['value'].idxmin()]
    srednia = df["value"].mean()

    # Trend z numpy.polyfit
    x = df["time"].astype("int64") // 10 ** 9  # timestamp w sekundach
    y = df["value"].values

    slope, intercept = np.polyfit(x, y, deg=1)
    trend_line = slope * x + intercept

    figure = go.Figure()
    # Wszystkie wartości
    figure.add_trace(go.Scatter(
        x=df["time"],
        y=df["value"],
        name=str(detector_id),
        # showlegend=False,

    ))
    # Min
    figure.add_trace(go.Scatter(
        x=[min_row["time"]],
        y=[min_row["value"]],
        mode="markers",
        marker=dict(color="#00a05d", size=14, symbol="triangle-down"),
        name="Min"
    ))
    # Max
    figure.add_trace(go.Scatter(
        x=[max_row["time"]],
        y=[max_row["value"]],
        mode="markers",
        marker=dict(color="#d00000", size=14, symbol="triangle-up"),
        name="Max"
    ))
    # Średnia
    figure.add_trace(go.Scatter(
        x=[df["time"].min(), df["time"].max()],
        y=[srednia, srednia],
        mode="lines",
        line=dict(color="orange", dash="dash"),
        name="Średnia"
    ))
    # Linia trendu
    figure.add_trace(go.Scatter(
        x=df["time"],
        y=trend_line,
        mode="lines",
        opacity=0.75,
        line=dict(color="brown", dash="dot"),
        name="Trend"
    ))
    figure.update_layout(title=f"Wykres dla detektora: {selected_indicator} ({detector_id})")
    figure.update_xaxes(title_text="Data pomiaru")
    figure.update_yaxes(title_text="Wartość")

    state.display_figure = figure


def menu_option_selected(state, id, payload):
    page_name = payload["args"][0]
    navigate(state, to=page_name)

def reload_data(state):
    DataStore().reload()
    state.notification = "Dane zostały przeładowane."