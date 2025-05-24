"""
Moduł testujący stanowiska
"""
stanowiska = [
    {
        "id": 6236,
        "stationId": 966,
        "param": {
            "paramName": "dwutlenek azotu",
            "paramFormula": "NO2",
            "paramCode": "NO2",
            "idParam": 6
        }
    },
    {
        "id": 6238,
        "stationId": 966,
        "param": {
            "paramName": "pył zawieszony PM10",
            "paramFormula": "PM10",
            "paramCode": "PM10",
            "idParam": 3
        }
    },
    {
        "id": 20586,
        "stationId": 966,
        "param": {
            "paramName": "tlenek węgla",
            "paramFormula": "CO",
            "paramCode": "CO",
            "idParam": 8
        }
    },
    {
        "id": 20587,
        "stationId": 966,
        "param": {
            "paramName": "benzen",
            "paramFormula": "C6H6",
            "paramCode": "C6H6",
            "idParam": 10
        }
    }
]

if __name__ == '__main__':
    from python07.extra.stanowiska.convert.converter import przeksztalc_dane as converter

    def main(data):
        sensors = converter(data)
        print(sensors)
        print(sensors[0])
        print(stanowiska[0])

        print('CZY RÓWNE?')
        print(sensors[0].sensor_id == stanowiska[0]['id'])
        print(sensors[0].station_id == stanowiska[0]['stationId'])
        print(sensors[0].param.name == stanowiska[0]['param']['paramName'])


    main(stanowiska)
