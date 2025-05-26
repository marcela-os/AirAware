"""
Moduł testujący działanie serializacji i deserializacji.
"""

from air_monitor.api_client.air_data import fetch_all_data
if __name__ == '__main__':
    from convert.converter import converter_station

    data = fetch_all_data()

    station = converter_station(data)
    print(station)
    print('CZY RÓWNE?', data['stations'][0]['station'] == station[0]) #False — są to różne typy danych
    print('CZY RÓWNE?', station[0].name == data['stations'][0]['station']['station_name'])

