import taipy as tp
import plotly.graph_objs as go
from gui import callbacks
from types import SimpleNamespace
from chart import generate_map
from air_monitor.utils.datastore import DataStore
from air_monitor.utils.logic import map_detectors_to_stations
from gui.pages import create_gui
from air_monitor.database.data_handler import get_data_handler



# Przypisanie callbacków do global scope wymagane przez Taipy GUI
globals()["on_station_change"] = callbacks.on_station_change
globals()["on_input_change"] = callbacks.on_input_change
globals()["on_station_select"] = callbacks.on_station_select
globals()["on_detector_change"] = callbacks.on_detector_change
globals()["reload_data"] = callbacks.reload_data
globals()["menu_option_selected"] = callbacks.menu_option_selected
globals()["on_slider_change"] = callbacks.on_slider_change

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

# Inicjalizacja danych
km = 20
search_query = ""
filtered_locations = station_names
station_data = ""
nearest_station_list = ""
notification = ""
error_message_location = ""

# Tymczasowy obiekt stanu z domyślnymi wartościami
initial_state = SimpleNamespace(
    selected_station=selected_station,
    selected_detector=selected_detector,
    display_figure=display_figure,
    station_detector_map=station_detector_map,
    measurements=measurements,
    first_station=first_station,
    default_detectors=default_detectors,
    available_detectors=available_detectors,
    map_fig=map_fig,
    search_query=search_query,
    filtered_locations=station_names,
    station_data=station_data,
    nearest_station_list=nearest_station_list,
    notification=notification,
    km=km,
    error_message_location=error_message_location
)

# Generowanie pierwszego wykresu
callbacks.on_detector_change(initial_state)

display_figure = initial_state.display_figure



if __name__ == "__main__":
    # Uruchomienie aplikacji
    get_data_handler()
    # Uruchomienie GUI
    pages = create_gui()
    gui = tp.Gui(pages=pages)

    gui.run(title="Air Monitor",
            use_reloader=False, port="auto", dark_mode=False)