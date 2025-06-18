""" Dostęp do bazy danych (fetch functions)"""

import sqlite3
import pandas as pd

def fetch_stations():
    """
    Pobiera wszystkie stacje z bazy danych.
    :return: list
    """

    with sqlite3.connect("air_monitor/database/air.db") as conn:
        all_stations = pd.read_sql_query("SELECT name, station_id, lat, long FROM stations", conn)
    return all_stations.values.tolist()


def fetch_detectors():
    """
    Pobiera wszystkie detektory z bazy danych.
    :return: list
    """

    with sqlite3.connect("air_monitor/database/air.db") as conn:
        all_detectors = pd.read_sql_query("SELECT station_id, detector_id, indicator, symbol FROM detectors", conn)
        return all_detectors.values.tolist()


def fetch_measurements():
    """
    Pobiera wszystkie pamiary z bazy danych.
    :return: list
    """

    with sqlite3.connect("air_monitor/database/air.db") as conn:
        all_measurements = pd.read_sql_query("SELECT detector_id, date, value  FROM measurements", conn)
        return all_measurements.values.tolist()


def fetch_latest_or_today_aq_index():
    """
    Pobiera pomiar indexLevelName dla każdej stacji:
    - z dzisiejszej daty i najpóźniejszej godziny, jeśli jest,
    - lub jeśli nie ma, to z najnowszej dostępnej daty i godziny.
    """
    query = """
    WITH today_data AS (
        SELECT station_id, MAX(stCalcDate) as max_date
        FROM aq_index
        WHERE DATE(stCalcDate) = DATE('now')
        GROUP BY station_id
    ),
    latest_data AS (
        SELECT station_id, MAX(stCalcDate) as max_date
        FROM aq_index
        GROUP BY station_id
    ),
    preferred_dates AS (
        SELECT
            latest_data.station_id,
            COALESCE(today_data.max_date, latest_data.max_date) as chosen_date
        FROM latest_data
        LEFT JOIN today_data ON latest_data.station_id = today_data.station_id
    )
    SELECT a.station_id, a.index_id, a.indexLevelName
    FROM aq_index a
    JOIN preferred_dates p ON a.station_id = p.station_id AND a.stCalcDate = p.chosen_date
    """

    with sqlite3.connect("air_monitor/database/air.db") as conn:
        df = pd.read_sql_query(query, conn)
        return df.values.tolist()

