import taipy as tp
import plotly.graph_objs as go
from datetime import datetime
from types import SimpleNamespace
from chart import generate_map
from air_monitor.utils.datastore import DataStore
from air_monitor.utils.logic import map_detectors_to_stations
from gui.callbacks import on_detector_change
from gui.pages import create_gui

data = DataStore()
stations = data.stations
detectors = data.detectors
measurements = data.measurements
aq_index = data.aq_index


# Początkowy pusty wykres
display_figure = go.Figure()

station_detector_map = map_detectors_to_stations(stations, detectors)

# Inicjalizacja danych globalnych
# Lista stacji do dropdowna
station_names = [name for name, *_ in stations]
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
# Inicjalizacja mapy
map_fig = generate_map(stations, aq_index)

# Tymczasowy obiekt stanu z domyślnymi wartościami
initial_state = SimpleNamespace(
    selected_station=selected_station,
    selected_detector=selected_detector,
    display_figure=display_figure,
    station_detector_map=station_detector_map,
    measurements=measurements,
)

# Generowanie pierwszego wykresu
on_detector_change(initial_state)

display_figure = initial_state.display_figure

# Inicjalizacja danych
search_query = ""
filtered_locations = station_names
selected_station = ""
station_data = ""
nearest_station_list = ""
notification = ""

if __name__ == "__main__":
    # Uruchomienie GUI
    pages = create_gui()
    gui = tp.Gui(pages=pages)

    gui.run(title="Air Monitor",
            use_reloader=True, port="auto", dark_mode=False)