""" Funkcja tworząca strony gui"""

import taipy.gui.builder as tgb
from taipy.gui import Icon
from gui.callbacks import (on_input_change, on_station_change,
                           on_station_select,on_detector_change,
                           reload_data, menu_option_selected)

def create_gui():
    # Tworzenie strony GUI
    # Strona Home
    with tgb.Page(route="/") as home:
        with tgb.part(class_name="container text-center"):
            tgb.image("assets/logo.png", width="10vw")
            tgb.text("# Wybierz lokalizacje",
                     mode="md")
            tgb.html("br")
            with tgb.layout("50 50"):
                with tgb.part(class_name="container text-center"):
                    tgb.input(label="Wpisz lokalizację (np. 'Dworzec Poznań')", value="{search_query}",
                              on_change=on_input_change, width=500)
                    tgb.html("br")
                    tgb.selector(value="{selected_station}", lov="{filtered_locations}", dropdown=False,
                                 on_change=on_station_select, width="500px")
                with tgb.part(class_name="container text-center"):
                    tgb.text("{station_data}")
                    tgb.html("br")
                    tgb.text("Stacje w promieniu 100 km:")
                    tgb.html("br")
                    tgb.text("{nearest_station_list}")
                    # GUI
                    tgb.button("🔁 Odśwież dane", on_action=reload_data)
                    tgb.text("{notification}")

    # Strona 1
    with tgb.Page(route="/page1") as page1:
        # with tgb.Page(name="Chart", label="Chart", route="/"):
        with tgb.part(class_name="container text-center"):
            tgb.image("assets/logo.png", width="10vw")
            tgb.text("# Statystyki",
                     mode="md")
            with tgb.layout("20 80"):
                tgb.selector(label="Stacja",
                             class_name="fullwidth",
                             value="{selected_station}",
                             lov="{station_names}",
                             on_change=on_station_change,
                             dropdown=True)
                tgb.selector(label="detectors",
                             class_name="fullwidth",
                             value="{selected_detector}",
                             lov="{available_detectors}",
                             on_change=on_detector_change,
                             dropdown=True)
            tgb.chart(figure="{display_figure}")
            with tgb.layout("5 5 5 5 5"):
                tgb.image("assets/logo.png", width="3vw")
                tgb.text("Test")
    # Strona 2
    with tgb.Page(route="/page2") as page2:
        with tgb.part(class_name="container text-center"):
            tgb.image("assets/logo.png", width="10vw")
            tgb.text("# Indeks jakości powietrza", mode="md")
            tgb.chart(figure="{map_fig}")

    # Menu
    with tgb.Page() as root_page:
        tgb.menu(
            label="Menu",
            lov=[
                ("home", Icon("assets/house.png", "Home")),
                ("page1", Icon("assets/chart.png", "Statystyki")),
                ("page2", Icon("assets/map.png", "Mapa")),
            ],
            on_action=menu_option_selected,
        )
    pages = {"/": root_page, "home": home, "page1": page1, "page2": page2}
    return pages