import sqlite3


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
            station_id INTEGER,
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
            sensor_id INTEGER,
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
            FOREIGN KEY (station_id) REFERENCES AirQualityIndex(station_id)
        )
    """)


    print("Baza danych zostala utworzona.")

if __name__ == "__main__":
    with sqlite3.connect("baza.db") as connection:
        c = connection.cursor()
        create_db(c)
