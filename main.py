import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import Icon
from taipy import Config
import datetime
import sqlite3
import pandas as pd
import plotly.graph_objs as go

dates = [
    datetime.datetime(2024, 1, 1),
    datetime.datetime(2025, 1, 1),
]




def fetch_stations():
    with sqlite3.connect("air_monitor/database/air.db") as conn:
        all_stations = pd.read_sql_query("SELECT name, station_id FROM stations", conn)
    return all_stations.values.tolist()  # jeśli potrzebujesz listy tak jak wcześniej

def fetch_detectors():
    with sqlite3.connect("air_monitor/database/air.db") as conn:
        all_detectors = pd.read_sql_query("SELECT station_id, detector_id, indicator, symbol FROM detectors", conn)
        return all_detectors.values.tolist()

def fetch_measurements():
    with sqlite3.connect("air_monitor/database/air.db") as conn:
        all_measurements = pd.read_sql_query("SELECT detector_id, date, value  FROM measurement", conn)
        return all_measurements.values.tolist()

detectors = fetch_detectors()
stations = fetch_stations()
measurements = fetch_measurements()

def map_detectors_to_stations(stations, detectors):
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
    detectors = station_detector_map[station_name]
    print(detectors)
    for d in detectors:
        if d["indicator"] == indicator:
            print("get:", d["detector_id"])
            return d["detector_id"]
    return None



# Lista stacji do dropdowna
station_names = [name for name, _ in stations]
# Domyślna stacja
first_station = station_names[0] if station_names else None
# Lista detektorów dla domyślnej stacji
default_detectors = station_detector_map[first_station]

selected_station = first_station
available_detectors = [d["indicator"] for d in default_detectors]
selected_detector = available_detectors[0] if available_detectors else None


def on_station_change(state):
    # print(state)
    station_name = state.selected_station
    state.available_detectors = [d["indicator"] for d in station_detector_map[station_name]]
    state.selected_detector = state.available_detectors[0] if state.available_detectors else None
    print("state.selected_station", state.selected_station)
    print("state.available_detectors", state.available_detectors)
    print("state.selected_detector", state.selected_detector)
    #1. sprawdz ktory detektor zostal klikniety i wybrany jesli zostala kliknieta stacja
    #
    #2. klikniety detektor przekaz do fukcji get_detector_id_by_indicator(wybrany detektor)

    print("Zmieniono stację:", station_name)
    print("Detektory:", state.available_detectors)

    # Zaktualizuj wykres po zmianie stacji
    on_detector_change(state)

def on_detector_change(state):
    station_name = state.selected_station
    selected_indicator = state.selected_detector
    print("Station:", station_name, "| Selected Indicator:", selected_indicator)

    detector_id = get_detector_id_by_indicator(station_name, selected_indicator)
    print(detector_id)



# create page
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
        tgb.chart()
        with tgb.layout("5 5 5 5 5"):
            tgb.image("assets/logo.png", width="3vw")
            tgb.text("Test")


if __name__ == "__main__":
    gui = tp.Gui(page)

    gui.run(title = "Air Monitor",
            use_reloader=True)
