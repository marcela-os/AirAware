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
print(database_path)
# def main():
#     data = fetch_all_data()  # pobierasz dane z API
#     stations = converter_station(data) # konwertujesz na obiekty
#     sensors = converter_sensors(data)
#     measurements = converter_measurement(data)
#     aq_index = converter_aq_index(data)
#
#
#     with sqlite3.connect("air.db") as c:
#         create_tables(c)  # utwórz tabele
#         save_stations_to_db(c, stations)  # zapisz dane
#
#     print(f"✔ Zapisano {len(stations)} stacji do bazy danych.")

def get_data():
    """
    Pobiera dane pomiarowe jakości powietrza zgodnie z następującą logiką:

    1. Próbuje połączyć się z lokalną bazą danych SQLite (air2.db).
    2. Tworzy wymagane tabele, jeśli jeszcze nie istnieją.
    3. Próbuje pobrać dane z zewnętrznego API (GIOŚ):
       - Jeśli dane są dostępne i poprawne, zapisuje je do bazy i zwraca.
       - Jeśli wystąpi błąd połączenia lub danych, zgłasza odpowiedni komunikat.
    4. W przypadku błędu połączenia z bazą zwraca komunikat o błędzie.

    Returns:
        dict | str:
            - Dane pobrane z API jako słownik, jeśli wszystko się powiedzie.
            - Komunikat błędu jako string, jeśli wystąpi problem z połączeniem lub przetwarzaniem danych.

    Raises:
        Brak bezpośredniego rzucania wyjątków — wszystkie obsługiwane wewnętrznie.
    :return:
    """
    try:
        with sqlite3.connect(database_path) as connection:
            c = connection.cursor()
            create_db(c)
            try:
                data = fetch_all_data()

                if not isinstance(data, dict):
                    raise TypeError("The API returned an incorrect data type - a dictionary was expected.")

                stations = converter_station(data)
                sensors = converter_sensors(data)
                measurements = converter_measurement(data)
                aq_index = converter_aq_index(data)
                # if not isinstance(data, dict):
                #     raise TypeError("The API returned an incorrect data type - a dictionary was expected.")


                save_to_db(stations, sensors, measurements, aq_index, c)
                connection.commit()
                print('Data downloaded from the API and saved.')
                return stations, sensors, measurements, aq_index
                # else:
                #     raise ValueError('Stations not found in the data')
            except (ValueError, KeyError, TypeError) as data_err:
                print(f'API data error: {data_err}')
                return f'API data processing error: {data_err}'

    except sqlite3.Error as db_err:
        return f'Database error: {db_err}'
