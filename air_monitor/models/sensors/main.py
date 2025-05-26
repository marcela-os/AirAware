"""
Moduł testujący stanowiska
"""

from air_monitor.api_client.air_data import fetch_all_data
if __name__ == '__main__':
    from convert.converter import converter_sensors
    data = fetch_all_data()
    sensors = converter_sensors(data)

    print('CZY RÓWNE?')
    print(sensors[0].sensor_id == data['stations'][0]['sensors'][0]['sensor']['detector_id'])
    print(sensors[0].station_id == data['stations'][0]['sensors'][0]['sensor']['station_id'])
    print(sensors[0].param.name == data['stations'][0]['sensors'][0]['sensor']['indicator'])
    print(sensors[0].param.code == data['stations'][0]['sensors'][0]['sensor']['code'])
    print(sensors[0].param.param_id == data['stations'][0]['sensors'][0]['sensor']['factor_id'])



