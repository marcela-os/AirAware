import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import Icon
from taipy import Config
import datetime
import sqlite3

dates = [
    datetime.datetime(2024, 1, 1),
    datetime.datetime(2025, 1, 1),
]

company = "10"


def fetch_stations():
    c = sqlite3.connect("air_monitor/database/air.db")
    cursor = c.cursor()
    cursor.execute("SELECT name, station_id FROM stations")
    all_tabels = cursor.fetchall()
    names = [row for row in all_tabels]
    c.close()
    return names

def fetch_detectors():
    c = sqlite3.connect("air_monitor/database/air.db")
    cursor = c.cursor()
    cursor.execute("SELECT station_id, detector_id, indicator,symbol FROM detectors")
    all_tabels = cursor.fetchall()
    detectors = [row for row in all_tabels]
    c.close()
    return detectors

detectors = fetch_detectors()
stations = fetch_stations()

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
# Lista stacji do dropdowna
station_names = [name for name, _ in stations]
# Domyślna stacja
first_station = station_names[0]
# Lista detektorów dla domyślnej stacji
default_detectors = station_detector_map[first_station]

selected_station = first_station
available_detectors = [d["indicator"] for d in default_detectors]
selected_detector = available_detectors[0] if available_detectors else None

def on_station_change(state):
    print(state)
    station_name = state.selected_station
    state.available_detectors = [d["indicator"] for d in station_detector_map[station_name]]
    state.selected_detector = state.available_detectors[0] if state.available_detectors else None

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
                         dropdown=True)
        tgb.chart()
        with tgb.layout("5 5 5 5 5"):
            tgb.image("assets/logo.png", width="3vw")
            tgb.text("{company}")


if __name__ == "__main__":
    gui = tp.Gui(page)

    gui.run(title = "Data Sceince Dashboard",
            use_reloader=True)
