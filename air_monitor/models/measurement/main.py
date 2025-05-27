"""
Moduł testowy
"""

from air_monitor.api_client.air_data import fetch_all_data

if __name__ == '__main__':
    from convert.converter import converter_measurement
    data = fetch_all_data()
    data_instance = converter_measurement(data)
    print(data_instance)