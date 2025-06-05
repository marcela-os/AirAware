import sqlite3


def create_db(c):
    """
    Funkcja sprawdza czy tabela o podanej nazwie istnieje a jeśli nie to tworzy ją.
    :param c: sqlite3.Cursor
    :return: None
    """

    c.execute("""
        CREATE TABLE IF NOT EXISTS stations (
            station_id INTEGER PRIMARY KEY,
            code TEXT,
            name TEXT,
            lat REAL,
            long REAL,
            city_name TEXT,
            city_id INTEGER,
            commune_name TEXT,
            district_name TEXT,
            province_name TEXT,
            street_name TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS detectors (
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
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            position_code TEXT,
            date TEXT,
            value REAL,
            detector_id INTEGER,
            FOREIGN KEY (detector_id) REFERENCES detector(id) ON DELETE CASCADE,
            UNIQUE(date, detector_id)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS aq_index (
            station_id INTEGER,
            index_id INTEGER,
            indexLevelName TEXT,
            stCalcDate TEXT,
            stSourceDataDate TEXT,
            stIndexCrParam TEXT,
            FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE,
            UNIQUE(stSourceDataDate, station_id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS aq_indexParam (
            station_id INTEGER,
            param_name TEXT,
            calc_date TEXT,
            source_date TEXT,
            index_level_id INTEGER,
            index_level_name TEXT,
            FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE,
            UNIQUE(source_date, station_id)
        )
    """)

    print("The database has been created.")


def save_to_db(stations, detectors, measurements, aq_index, cursor):
    """
    Zapisuje dane pobrane z API do bazy SQLite.
    :param stations: list[Stations]
    :param detectors: list[Detectors]
    :param measurements: list[Measurements]
    :param aq_index: list[AQIndex]
    :param cursor: sqlite3.Cursor
    :return: None
    """

    #--- Wstawianie stacji ---
    save_stations(cursor, stations)
    # --- Wstawianie indeksu jakości powietrza ---
    save_aq_index(cursor, aq_index)
    # --- Wstawianie parametrów indeksu jakości powietrza ---
    save_aq_index_param(cursor, aq_index)
    # --- Wstawianie sensorów ---
    save_detectors_and_measurements(cursor, detectors, measurements)

    print('The data was saved to the database.')


def save_stations(cursor, stations):
    """
    Funkcja zapisuje dane pojedynczej stacji do tabeli `stations`.
    :param cursor: sqlite3.Cursor
    :param stations: list zawierający dane stacji
    :return: None
    """
    for station in stations:
        cursor.execute("""
                    INSERT OR REPLACE INTO stations
                    (station_id, code, name, lat, long, city_name, city_id, commune_name, district_name, province_name, street_name)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
            station.id,
            station.code,
            station.name,
            station.lat,
            station.lon,
            station.city.name,
            station.city.id,
            station.city.commune.name,
            station.city.commune.district,
            station.city.commune.province,
            station.city.street,
        ))

def save_aq_index(cursor, aq_data):
    """
    Funkcja zapisuje indeks jakości powietrza do tabeli `aq_index`.
    :param cursor: sqlite3.Cursor
    :param aq_data: list zawierający dane indeksu jakości powietrza
    :return: None
    """
    for aq_index in aq_data:
        cursor.execute("""
            INSERT OR IGNORE INTO aq_index
            (station_id, index_id, indexLevelName, stCalcDate, stSourceDataDate, stIndexCrParam)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            aq_index.station_id,
            aq_index.value_index,
            aq_index.name,
            aq_index.calc_date,
            aq_index.source_data_date,
            aq_index.critical_pollution_code
        ))

def save_aq_index_param(cursor, aq_data):
    """
    Funkcja zapisuje parametry indeksu jakości powietrza do tabeli `aq_indexParam`.
    :param cursor: sqlite3.Cursor
    :param aq_data: list zawierający dane indeksu jakości powietrza
    :return: None
    """
    for aq_index in aq_data:
        for key, value in aq_index.param.items():
            cursor.execute("""
                  INSERT OR IGNORE INTO aq_indexParam (station_id, param_name, calc_date, source_date, index_level_id, index_level_name)
                  VALUES (?, ?, ?, ?, ?, ?)
                  """, (
                aq_index.station_id,
                value.name,
                value.calc_date,
                value.source_date,
                value.index_value,
                value.cat_name
            ))

def save_detectors_and_measurements(cursor, detectors, measurements):
    """
    Funkcja zapisuje parametry czujników oraz odpowiadającym im pomiarom do tabel `detector`. i `measurement`.
    :param cursor: sqlite3.Cursor
    :param detectors: list zawierający dane czujników
    :param measurements: list zawierający dane pomiarowe z czujników
    :return: None
    """
    detector_ids = set()
    for detector in detectors:
        cursor.execute("""
            INSERT OR REPLACE INTO detectors
            (detector_id, station_id, indicator, symbol, code, factor_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            detector.sensor_id,
            detector.station_id,
            detector.param.name,
            detector.param.formula,
            detector.param.code,
            detector.param.param_id,
        ))
        detector_ids.add(detector.sensor_id)

    for measurement in measurements:
        if measurement.key not in detector_ids:
            print(f"Detector ID {measurement.key} not found in detectors — skipping")
            continue
        for value in measurement.values:
            cursor.execute("""
                INSERT OR IGNORE INTO measurements (position_code, date, value, detector_id)
                VALUES (?, ?, ?, ?)
            """, (
                value.code,
                value.date_value,
                value.value,
                measurement.key
            ))


# if __name__ == '__main__':
#     # create_stations()
#     with sqlite3.connect("air.db") as connection:
#         c = connection.cursor()
#         tables = ['measurement']
#
#         for table in tables:
#             c.execute(f'DROP TABLE IF EXISTS "{table}"')