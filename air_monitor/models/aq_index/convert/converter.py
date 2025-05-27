from air_monitor.models.aq_index.model.aq_index import AqIndex
from air_monitor.models.aq_index.model.value_aq import ValueAQ


def converter_aq_index(data):
    """
    Funkcja umożliwiająca konwersję danych indeksu jakości powietrza do modelu obiektowego.
    :param data: dict
    :return: list[AqIndex]
    """
    aq_index_list = []
    parameters = {}

    stations = data.get('stations', [])
    for station_entry in stations:
        aq_entry = station_entry['aq_index']
        key = (
            aq_entry['station_id'],
            aq_entry['value_index'],
            aq_entry['category_name'],
            aq_entry['calc_date'],
            aq_entry['source_data_date'],
            aq_entry['critical_pollution_code']
        )

        if key in parameters:
            param = parameters[key]
        else:
            param = {}
            raw_params = aq_entry.get('param', {})
            for p, values in raw_params.items():
                try:
                    value_obj = ValueAQ(
                        p,
                        values['source_date'],
                        values['calcs_date'],
                        values['index_value'],
                        values['index_category_name']
                    )
                except Exception as e:
                    print(f"Error creating ValueAQ for {p}: {e}")
                    continue
                param[p] = value_obj
            parameters[key] = param

        try:
            aq_index_obj = AqIndex(
                aq_entry['station_id'],
                aq_entry['value_index'],
                aq_entry['category_name'],
                aq_entry['calc_date'],
                aq_entry['source_data_date'],
                aq_entry['critical_pollution_code'],
                param
            )
            aq_index_list.append(aq_index_obj)
        except Exception as e:
            print(f"Error creating AqIndex: {e}")

    return aq_index_list
