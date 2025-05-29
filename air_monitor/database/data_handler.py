import sqlite3
from air_monitor.database.db_manager import create_db, save_to_db
from air_monitor.api_client.air_data import fetch_all_data
from air_monitor.models.stations.convert.converter import converter_station
from air_monitor.models.sensors.convert.converter import converter_sensors
from air_monitor.models.measurement.convert.converter import converter_measurement
from air_monitor.models.aq_index.convert.converter import converter_aq_index
import os
file_path = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(file_path, "air.db")

def get_data_handler():
    """
    Funkcja pobiera dane z API, tworzy bazę danych (jeśli nie istnieje) i zapisuje dane.
    :return: tuple[list, list, list, list]
    :raises RuntimeError:
        - Gdy wystąpi błąd połączenia z bazą danych lub problem z danymi z API.
    """
    try:
        with sqlite3.connect(database_path) as connection:
            c = connection.cursor()
            create_db(c)
            try:
                data = fetch_all_data()

                if not isinstance(data, dict):
                    raise TypeError("The API returned invalid format.")

                stations = converter_station(data)
                sensors = converter_sensors(data)
                measurements = converter_measurement(data)
                aq_index = converter_aq_index(data)

                save_to_db(stations, sensors, measurements, aq_index, c)
                connection.commit()
                print('Data downloaded from the API and saved.')
                return stations, sensors, measurements, aq_index

            except Exception as data_err:
                raise RuntimeError(f"Data fetch failed: {data_err}")

    except sqlite3.Error as db_err:
        raise RuntimeError(f"Database error: {db_err}")
