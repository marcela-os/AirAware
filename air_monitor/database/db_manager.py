import sqlite3
from air_monitor.api_client.air_data import fetch_all_data


def create_db(c):
    """Tworzy tabele stacji pomiarowych. Jesli istnieja, usuwa je przed stworzeniem nowych."""
    c.execute("DROP TABLE IF EXISTS air_monitor")
    c.execute("DROP TABLE IF EXISTS measurement")
    c.execute("DROP TABLE IF EXISTS sensor")
    c.execute("DROP TABLE IF EXISTS aq_index_param")
    c.execute("DROP TABLE IF EXISTS aq_index")
    c.execute("DROP TABLE IF EXISTS stations")

    c.execute("""
        CREATE TABLE stations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        CREATE TABLE sensor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            sensor_id INTEGER,
            date TEXT,
            value REAL,
            FOREIGN KEY (sensor_id) REFERENCES sensor(id) ON DELETE CASCADE
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
        )
    """)

    c.execute("""
        CREATE TABLE aq_indexParam (
            station_id INTEGER,
            calc_date TEXT,
            index_level_id INTEGER,
            index_level_name TEXT,
            FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE
        )
    """)

    print("Baza danych zostala utworzona.")


def save_to_db(data, cursor):
    """
    Zapisuje dane pobrane z API do bazy SQLite.
    :param data: dict zwrócony przez fetch_all_data()
    """

    for station_entry in data.get('stations', []):
        station = station_entry['station']
        aq_index = station_entry.get('aq_index', {})
        # cursor.execute("""DELETE FROM stations""")
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
        # cursor.execute("""DELETE FROM aq_index""")
        # Pobranie id z tabeli stations
        # c.execute("SELECT id FROM stations WHERE station_id = ?", (station['Identyfikator stacji'],))
        # station_db_id = c.fetchone()[0]
        cursor.execute("""
            INSERT OR REPLACE INTO aq_index
            (station_id, index_id, indexLevelName, stCalcDate, stSourceDataDate, stIndexCrParam)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            station['station_id'],
            aq_index['value_index'],
            aq_index['category_name'],
            aq_index['calc_date'],
            aq_index['source_data_date'],
            aq_index['critical_pollution_code']
        ))

    print("Dane zostały zapisane do bazy.")


if __name__ == "__main__":
    with sqlite3.connect("air2.db") as connection:
        c = connection.cursor()
        # create_db(c)
        data = fetch_all_data()
        # conn = sqlite3.connect("air2.db")
        save_to_db(data, c)
