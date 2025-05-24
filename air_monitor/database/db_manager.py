import sqlite3
from air_monitor.api_client.air_data import fetch_all_data


def create_db(c):
    """
    Tworzy tabele stacji pomiarowych. Jesli istnieja, usuwa je przed stworzeniem nowych.
    :param c: sqlite3.Cursor
    :return: None
    """

    c.execute("DROP TABLE IF EXISTS air_monitor")
    c.execute("DROP TABLE IF EXISTS measurement")
    c.execute("DROP TABLE IF EXISTS detector")
    c.execute("DROP TABLE IF EXISTS aq_index_param")
    c.execute("DROP TABLE IF EXISTS aq_index")
    c.execute("DROP TABLE IF EXISTS stations")

    c.execute("""
        CREATE TABLE stations (
            station_id INTEGER PRIMARY KEY,
            code TEXT NOT NULL,
            name TEXT NOT NULL,
            lat REAL,
            long REAL,
            city_name TEXT NOT NULL,
            city_id INTEGER,
            commune_name TEXT NOT NULL,
            district_name TEXT NOT NULL,
            province_name TEXT NOT NULL,
            street_name TEXT NOT NULL
        )
    """)
    c.execute("""
        CREATE TABLE detector (
            detector_id INTEGER PRIMARY KEY AUTOINCREMENT,
            station_id INTEGER,
            indicator TEXT NOT NULL,
            symbol TEXT NOT NULL,
            code TEXT NOT NULL,
            factor_id INTEGER NOT NULL,
            FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE
        )
    """)
    c.execute("""
        CREATE TABLE measurement (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            position_code TEXT NOT NULL,
            date TEXT NOT NULL,
            value REAL,
            detector_id INTEGER NOT NULL,
            FOREIGN KEY (detector_id) REFERENCES detector(id) ON DELETE CASCADE
            UNIQUE(date, detector_id)
        )
    """)
    c.execute("""
        CREATE TABLE aq_index (
            station_id INTEGER,
            index_id INTEGER,
            indexLevelName TEXT NOT NULL,
            stCalcDate TEXT NOT NULL,
            stSourceDataDate TEXT NOT NULL,
            stIndexCrParam TEXT NOT NULL,
            FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE
            UNIQUE(stSourceDataDate, station_id)
        )
    """)

    c.execute("""
        CREATE TABLE aq_indexParam (
            station_id INTEGER,
            param_name TEXT,
            calc_date TEXT,
            source_date TEXT,
            index_level_id INTEGER,
            index_level_name TEXT,
            FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE
            UNIQUE(source_date, station_id)
        )
    """)

    print("Baza danych zostala utworzona.")


def save_to_db(data, cursor):
    """
    Zapisuje dane pobrane z API do bazy SQLite.
    :param data: dict z danych pobranych z API
    :param cursor: sqlite3.Cursor
    :return: None
    """

    for station_entry in data.get('stations', []):
        station = station_entry['station']
        aq_index = station_entry.get('aq_index', {})
        # cursor.execute("""DELETE FROM stations""")

        # --- Wstawianie stacji ---
        save_stations(cursor, station)
        # --- Wstawianie indeksu jakości powietrza ---
        save_aq_index(cursor, aq_index)
        # --- Wstawianie parametrów indeksu jakości powietrza ---
        save_aq_index_param(cursor, aq_index)
        # --- Wstawianie sensorów ---
        detectors = station_entry.get('sensors', [])
        save_detectors_and_measurements(cursor, detectors)
    print("Dane zostały zapisane do bazy.")


def save_stations(cursor, station):
    """
    Funkcja zapisuje dane pojedynczej stacji do tabeli `stations`.
    :param cursor: sqlite3.Cursor
    :param station: dict zawierający dane stacji
    :return: None
    """

    cursor.execute("""
                INSERT OR REPLACE INTO stations
                (station_id, code, name, lat, long, city_name, city_id, commune_name, district_name, province_name, street_name)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
        station['station_id'],
        station['station_code'],
        station['station_name'],
        station['lat'],
        station['long'],
        station['city_name'],
        station['city_id'],
        station['commune'],
        station['district'],
        station['province'],
        station['street'],
    ))


def save_aq_index(cursor, aq_index):
    """
    Funkcja zapisuje indeks jakości powietrza do tabeli `aq_index`.
    :param cursor: sqlite3.Cursor
    :param aq_index: dict zawierający dane indeksu jakości powietrza
    :return: None
    """

    cursor.execute("""
        INSERT OR IGNORE INTO aq_index
        (station_id, index_id, indexLevelName, stCalcDate, stSourceDataDate, stIndexCrParam)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        aq_index['station_id'],
        aq_index['value_index'],
        aq_index['category_name'],
        aq_index['calc_date'],
        aq_index['source_data_date'],
        aq_index['critical_pollution_code']
    ))


def save_aq_index_param(cursor, aq_index):
    """
    Funkcja zapisuje parametry indeksu jakości powietrza do tabeli `aq_indexParam`.
    :param cursor: sqlite3.Cursor
    :param aq_index: dict zawierający dane indeksu jakości powietrza
    :return: None
    """

    for param_name, param_data in aq_index['param'].items():
        cursor.execute("""
              INSERT OR IGNORE INTO aq_indexParam (station_id, param_name, calc_date, source_date, index_level_id, index_level_name)
              VALUES (?, ?, ?, ?, ?, ?)
              """, (
            aq_index['station_id'],
            param_name,
            param_data['calcs_date'],
            param_data['source_date'],
            param_data['index_value'],
            param_data['index_category_name']
        ))


def save_detectors_and_measurements(cursor, detectors):
    """
    Funkcja zapisuje parametry czujników oraz odpowiadającym im pomiarom do tabel `detector`. i `measurement`.
    :param cursor: sqlite3.Cursor
    :param detectors: list zawierający dane czujników oraz `measurement`
    :return: None
    """

    for detector_entry in detectors:
        detector = detector_entry['sensor']
        measurement_data = detector_entry['measurement']

        cursor.execute("""
            INSERT OR REPLACE INTO detector
            (detector_id, station_id, indicator, symbol, code, factor_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            detector['detector_id'],
            detector['station_id'],
            detector['indicator'],
            detector['symbol'],
            detector['code'],
            detector['factor_id'],
        ))

        # --- Wstawianie pomiarów ---
        if isinstance(measurement_data, list):
            for measurement in measurement_data:
                c.execute("""
                    INSERT OR IGNORE INTO measurement (position_code, date, value, detector_id)
                    VALUES (?, ?, ?, ?)
                """, (
                    measurement['position_code'],
                    measurement['date'],
                    measurement['value'],
                    detector['detector_id']
                ))


if __name__ == "__main__":
    with sqlite3.connect("air2.db") as connection:
        c = connection.cursor()
        # create_db(c)
        data = fetch_all_data()
        # # # conn = sqlite3.connect("air2.db")
        save_to_db(data, c)
        connection.commit()

    # # usuwanie kolumn z db
    #  tables = ['aq_indexParam', 'stations', 'detector', 'measurement', 'aq_index']
    #
    #  for table in tables:
    #      c.execute(f'DROP TABLE IF EXISTS "{table}"')
