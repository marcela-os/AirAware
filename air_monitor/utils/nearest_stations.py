import ssl
import certifi
from geopy.geocoders import Nominatim
from geopy import distance

# Kontekst SSL z użyciem certyfikatów z certifi
ctx = ssl.create_default_context(cafile=certifi.where())
geolocator = Nominatim(user_agent="air_quality_app_Marcelina", ssl_context=ctx)


def get_nearest_stations(description, max_distance_km, stations_data):
    """
    Returns a list of measuring stations within a specified distance from the specified location.

    :param description: Description of location (e.g. ‘Poznań, market square’)
    :param max_distance_km: Maximum distance in kilometres (float)
    :param stations_data: List of dict with stations, each containing ‘gegrLat’, ‘gegrLon’ and ‘stationName’
    :return: List of tuples (distance_km, station_name) sorted in ascending order of distance
    """
    try:
        location = geolocator.geocode(description, timeout=10)
    except Exception as e:
        raise RuntimeError(f"Geolocation failed: {e}")


    if not location:
        raise ValueError(f"No location found for the description: {description}")


    data = [(float(item[2]), float(item[3]), item[0]) for item in stations_data]

    stations = [(round(distance.geodesic((location.latitude, location.longitude), (item[0], item[1])).km, 2), item[2])
                for item in data]

    stations = list(filter(lambda item: (item[0] <= max_distance_km), stations))

    return sorted(stations, key=lambda value: value[0])


# new = get_nearest_stations("Kłodzko, ul. Szkolna", 200, wszystkie_stacje_pomiarowe)
# print(new)

def get_nearest_stations_by_coords(location_coords, max_distance_km, stations_data):
    stations = []
    for item in stations_data:
        lat, lon, name = float(item[2]), float(item[3]), item[0]
        dist = distance.distance(location_coords, (lat, lon)).km
        if dist <= max_distance_km:
            stations.append((round(dist, 2), name))
    return sorted(stations, key=lambda x: x[0])