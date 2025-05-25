"""
Moduł testowy
"""

from air_monitor.api_client.air_data import fetch_all_data

if __name__ == '__main__':
    from convert.converter import convert_dict_to_data
    data = fetch_all_data()
    data_instance = convert_dict_to_data(data)
    print(data_instance)