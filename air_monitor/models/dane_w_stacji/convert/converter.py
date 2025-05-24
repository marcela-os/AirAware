from python07.extra.dane_w_stacji.model import Value
from python07.extra.dane_w_stacji.model import Data

def convert_dict_to_data(data_dict):
    key = data_dict["key"]
    value_objs = [Value(v["date"], v["value"]) for v in data_dict["values"]]
    return Data(key, value_objs)