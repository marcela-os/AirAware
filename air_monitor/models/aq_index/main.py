"""
Moduł testujący aq_index
"""

from air_monitor.api_client.air_data import fetch_all_data
if __name__ == '__main__':
    from convert.converter import converter_aq_index
    data = fetch_all_data()
    aq_index = converter_aq_index(data)
    print("aq_index print", aq_index)
    print(aq_index[0].param['NO2'].cat_name)
    print(data['stations'][0]['aq_index']['param']['NO2']['index_category_name'])

    print('CZY RÓWNE?')
    print(aq_index[0].station_id == data['stations'][0]['aq_index']['station_id'])
    print(aq_index[0].value_index == data['stations'][0]['aq_index']['value_index'])
    print(aq_index[0].param['NO2'].cat_name == data['stations'][0]['aq_index']['param']['NO2']['index_category_name'])



