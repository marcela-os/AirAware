"""
Napisz program, o analogicznej funkcjonalności, jak w ćwiczeniach dodatkowych 2.1, 2.2 i 2.3 z modułu 3
Zamknij zawarty tam kod w funkcjach
Zastąp wyrażenia listowe użyciem wbudowanych funkcji filter oraz map
Tam, gdzie to możliwe, użyj funkcji lambda
"""
stacje = [
    {
        "id": 986,
        "stationName": "Szczecin, ul. Andrzejewskiego",
        "gegrLat": "53.380975",
        "gegrLon": "14.663347",
        "city": {
            "id": 917,
            "name": "Szczecin",
            "commune": {
                "communeName": "Szczecin",
                "districtName": "Szczecin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Andrzejewskiego 23"
    },
    {
        "id": 987,
        "stationName": "Szczecin, ul. Piłsudskiego",
        "gegrLat": "53.432169",
        "gegrLon": "14.553900",
        "city": {
            "id": 917,
            "name": "Szczecin",
            "commune": {
                "communeName": "Szczecin",
                "districtName": "Szczecin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Piłsudskiego 1"
    },
    {
        "id": 989,
        "stationName": "Szczecin, ul. Łączna",
        "gegrLat": "53.470889",
        "gegrLon": "14.556250",
        "city": {
            "id": 917,
            "name": "Szczecin",
            "commune": {
                "communeName": "Szczecin",
                "districtName": "Szczecin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Łączna"
    },
    {
        "id": 966,
        "stationName": "Koszalin, ul. Armii Krajowej",
        "gegrLat": "54.193986",
        "gegrLon": "16.172544",
        "city": {
            "id": 402,
            "name": "Koszalin",
            "commune": {
                "communeName": "Koszalin",
                "districtName": "Koszalin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Armii Krajowej"
    },
    {
        "id": 11336,
        "stationName": "Koszalin, ul. Chopina",
        "gegrLat": "54.194114",
        "gegrLon": "16.211672",
        "city": {
            "id": 402,
            "name": "Koszalin",
            "commune": {
                "communeName": "Koszalin",
                "districtName": "Koszalin",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Chopina 42"
    },
    {
        "id": 961,
        "stationName": "Widuchowa",
        "gegrLat": "53.122325",
        "gegrLon": "14.382245",
        "city": {
            "id": 1025,
            "name": "Widuchowa",
            "commune": {
                "communeName": "Widuchowa",
                "districtName": "gryfiński",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Bulwary Rybackie 1"
    },
    {
        "id": 983,
        "stationName": "Szczecinek, ul. Przemysłowa",
        "gegrLat": "53.698902",
        "gegrLon": "16.704556",
        "city": {
            "id": 918,
            "name": "Szczecinek",
            "commune": {
                "communeName": "Szczecinek",
                "districtName": "szczecinecki",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Przemysłowa 5"
    },
    {
        "id": 10934,
        "stationName": "Kołobrzeg, ul. Żółkiewskiego",
        "gegrLat": "54.179381",
        "gegrLon": "15.596347",
        "city": {
            "id": 386,
            "name": "Kołobrzeg",
            "commune": {
                "communeName": "Kołobrzeg",
                "districtName": "kołobrzeski",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "ul. Żółkiewskiego"
    },
    {
        "id": 20160,
        "stationName": "Świnoujście, ul. Białoruska",
        "gegrLat": "53.903814",
        "gegrLon": "14.279628",
        "city": {
            "id": 952,
            "name": "Świnoujście",
            "commune": {
                "communeName": "Świnoujście",
                "districtName": "Świnoujście",
                "provinceName": "ZACHODNIOPOMORSKIE"
            }
        },
        "addressStreet": "Białoruska"
    }
]

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

dane_pomiarowe = {
    "key": "C6H6",
    "values": [
            {
                "date": "2025-01-08 13:00:00",
                "value": None
            },
            {
                "date": "2025-01-08 12:00:00",
                "value": 0.4
            },
            {
                "date": "2025-01-08 11:00:00",
                "value": 0.36
            },
            {
                "date": "2025-01-08 10:00:00",
                "value": 0.38
            },
            {
                "date": "2025-01-08 09:00:00",
                "value": 0.4
            },
            {
                "date": "2025-01-08 08:00:00",
                "value": 0.45
            },
            {
                "date": "2025-01-08 07:00:00",
                "value": 0.34
            },
            {
                "date": "2025-01-08 06:00:00",
                "value": 0.23
            },
            {
                "date": "2025-01-08 05:00:00",
                "value": 0.22
            },
            {
                "date": "2025-01-08 04:00:00",
                "value": 0.23
            },
            {
                "date": "2025-01-08 03:00:00",
                "value": 0.22
            },
            {
                "date": "2025-01-08 02:00:00",
                "value": 0.22
            },
            {
                "date": "2025-01-08 01:00:00",
                "value": 0.26
            },
            {
                "date": "2025-01-08 00:00:00",
                "value": 0.36
            },
            {
                "date": "2025-01-07 23:00:00",
                "value": 0.48
            },
            {
                "date": "2025-01-07 22:00:00",
                "value": 0.54
            },
            {
                "date": "2025-01-07 21:00:00",
                "value": 0.73
            },
            {
                "date": "2025-01-07 20:00:00",
                "value": 0.76
            },
            {
                "date": "2025-01-07 19:00:00",
                "value": 0.51
            },
            {
                "date": "2025-01-07 18:00:00",
                "value": 0.6
            },
            {
                "date": "2025-01-07 17:00:00",
                "value": 0.8
            },
            {
                "date": "2025-01-07 16:00:00",
                "value": 0.78
            },
            {
                "date": "2025-01-07 15:00:00",
                "value": 0.41
            },
            {
                "date": "2025-01-07 14:00:00",
                "value": 0.38
            },
            {
                "date": "2025-01-07 13:00:00",
                "value": 0.39
            },
            {
                "date": "2025-01-07 12:00:00",
                "value": 0.41
            },
            {
                "date": "2025-01-07 11:00:00",
                "value": 0.49
            },
            {
                "date": "2025-01-07 10:00:00",
                "value": 0.56
            },
            {
                "date": "2025-01-07 09:00:00",
                "value": 0.52
            },
            {
                "date": "2025-01-07 08:00:00",
                "value": 0.33
            },
            {
                "date": "2025-01-07 07:00:00",
                "value": 0.29
            },
            {
                "date": "2025-01-07 06:00:00",
                "value": 0.21
            },
            {
                "date": "2025-01-07 05:00:00",
                "value": 0.22
            },
            {
                "date": "2025-01-07 04:00:00",
                "value": 0.25
            },
            {
                "date": "2025-01-07 03:00:00",
                "value": 0.31
            },
            {
                "date": "2025-01-07 02:00:00",
                "value": 0.28
            },
            {
                "date": "2025-01-07 01:00:00",
                "value": 0.4
            },
            {
                "date": "2025-01-07 00:00:00",
                "value": 0.45
            },
            {
                "date": "2025-01-06 23:00:00",
                "value": 0.52
            },
            {
                "date": "2025-01-06 22:00:00",
                "value": 0.64
            },
            {
                "date": "2025-01-06 21:00:00",
                "value": 0.61
        },
        {
            "date": "2025-01-06 20:00:00",
            "value": 0.66
        },
        {
            "date": "2025-01-06 19:00:00",
            "value": 1.1
        },
        {
            "date": "2025-01-06 18:00:00",
            "value": 1.01
        },
        {
            "date": "2025-01-06 17:00:00",
            "value": 0.62
        },
        {
            "date": "2025-01-06 16:00:00",
            "value": 0.75
        },
        {
            "date": "2025-01-06 15:00:00",
            "value": 0.94
        },
        {
            "date": "2025-01-06 14:00:00",
            "value": 1.3
        },
        {
            "date": "2025-01-06 13:00:00",
            "value": 1.59
        },
        {
            "date": "2025-01-06 12:00:00",
            "value": 2.2
        },
        {
            "date": "2025-01-06 11:00:00",
            "value": 1.37
        },
        {
            "date": "2025-01-06 10:00:00",
            "value": 1.12
        },
        {
            "date": "2025-01-06 09:00:00",
            "value": 1.08
        },
        {
            "date": "2025-01-06 08:00:00",
            "value": 1.07
        },
        {
            "date": "2025-01-06 07:00:00",
            "value": 1.12
        },
        {
            "date": "2025-01-06 06:00:00",
            "value": 1.18
        },
        {
            "date": "2025-01-06 05:00:00",
            "value": 1.23
        },
        {
            "date": "2025-01-06 04:00:00",
            "value": 1.18
        },
        {
            "date": "2025-01-06 03:00:00",
            "value": 1.13
        },
        {
            "date": "2025-01-06 02:00:00",
            "value": 1.07
        },
        {
            "date": "2025-01-06 01:00:00",
            "value": 0.99
        },
        {
            "date": "2025-01-06 00:00:00",
            "value": 0.94
        }
    ]
}

"""
Stacje
"""
# Kryterium: stacje w miecie Koszalin
miejscowosc = "Koszalin"


def stacje_miejscowosc(stacja):
    return stacja["city"]["name"] == miejscowosc


print("Stacje w Koszalin:")
stacja = filter(stacje_miejscowosc, stacje)
print(*stacja, sep='\n')

# Kryterium: stacje w gminie Szczecin
gmina = "Szczecin"
print("\nStacje w Szczecin:")


def stacje_gmina(stacja):
    return stacja["city"]["commune"]["communeName"] == gmina


w_gminie = filter(stacje_gmina, stacje)
print(*w_gminie, sep='\n')

# Kryterium: stacje w określonym zakresie szerokości geograficznej
min_lat = 53.1
max_lat = 53.5


# def coord(stacja):
#     return min_lat <= float(stacja["gegrLat"]) <= max_lat

print("\nStacje w zakresie szerokości geograficznej (53.1 - 53.5):")

zakres = lambda value: min_lat <= float(value["gegrLat"]) <= max_lat
w_zakresie = filter(zakres, stacje)
print(*w_zakresie, sep='\n')


"""
Stanowiska w stacji
"""

# Parametry w danej stacji

# parmametry_w_stacji = filter(lambda value: value['param']['paramName'] and value['param']['paramFormula'], stanowiska)
# print('Parametry w danej stacji:')
# print(*parmametry_w_stacji, sep='\n')
#
# print(*map(lambda s: (s['param']['paramName'], s['param']['paramFormula']), stanowiska), sep='\n')

parametry = map(lambda s: (s['param']['paramName'], s['param']['paramFormula']),
                filter(lambda value: value['param']['paramName'] and value['param']['paramFormula'], stanowiska))

posortowane = sorted(parametry, key=lambda s: s[1])
# print(*parametry, sep='\n')
print('Parametry w danej stacji:')
for nazwa, symbol in posortowane:
    print(nazwa, symbol)

"""
Dane pomiarowe
"""
print("Dane pomiarowe z dnia:", sep='\n')
z_dnia = [pomiar for pomiar in dane_pomiarowe['values']]
print(z_dnia)

def z_dnia(pomiar):
    print("w funkcji", pomiar)
    return [pomiar['value'] for pomiar in dane_pomiarowe['values'] if pomiar['value'] is not None]


wartosci = z_dnia(dane_pomiarowe)
print(wartosci)
print(f'Maxymalna wartość dnia: {max(wartosci)}')
print(f'Minimalna wartosc dnia: {min(wartosci)}')

# max_w_dniu = [pomiar['date'] for pomiar in dane_pomiarowe['values'] if
#               not pomiar['value'] != max(wartosci)]

max_w_dniu = list(filter(lambda pomiar: pomiar['value'] == max(wartosci), dane_pomiarowe['values']))

print(max_w_dniu[0]['date'])

# min_w_dniu = [pomiar['date'] for pomiar in dane_pomiarowe['values'] if
#               not pomiar['value'] != min(wartosci)]

min_w_dniu = list(filter(lambda pomiar: pomiar['value'] == min(wartosci), dane_pomiarowe['values']))
print(min_w_dniu[0]['date'])