from air_monitor.utils.database import fetch_stations, fetch_measurements, fetch_detectors, fetch_latest_or_today_aq_index

# Implementacja singletona
# Czy to jest dobre użycie singletona?
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DataStore(metaclass=Singleton):
    def __init__(self):
        self._load_data()

    def _load_data(self):
        self.stations = fetch_stations()
        self.detectors = fetch_detectors()
        self.measurements = fetch_measurements()
        self.aq_index = fetch_latest_or_today_aq_index()

    def reload(self):
        self._load_data()