#################################################################################################
#Задача 1

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

text = int(input('Сколько песен выбрать?: '))
counter = 0

for i in range(1, text + 1):
    song = input(f'Название {i} песни:')
    counter += violator_songs[song]

print(f'Общее время звучания песен: {round(counter, 2)} минуты')

#################################################################################################
#Задача 2

text = int(input('Количество стран: '))
countries_dict = {}
countries_list = []
for _ in range(text):
    countries_list.append(input(f'Введите страну:').split())

countries_dict[countries_list[0][0]] = countries_list[0]
countries_dict[countries_list[1][0]] = countries_list[1]
countries_dict[countries_list[0][0]].pop(0)
countries_dict[countries_list[1][0]].pop(0)

for _ in range(3):
    city = input(f'Введите город:')
    for k, v in countries_dict.items():
        if city in v:
            print(f'Город {city} расположен в стране {k}.')


# Россия Москва Петербург Новгород
# Германия Берлин Лейпциг Мюнхен

#################################################################################################
#################################################################################################

import json

text = int(input('Количество стран: '))
countries_dict = dict()

for _ in range(text):
    data_from_user = input(f'Введите страну и гороДА:').split()
    for data in data_from_user[1:]:
        countries_dict[data] = data_from_user[0]

print(countries_dict)

for _ in range(3):
    city = input(f'Введите город:')
    country = countries_dict.get(city)
    if country is not None:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'Город {city} мы не нашли.')


# Россия Москва Петербург Новгород
# Германия Берлин Лейпциг Мюнхен


#################################################################################################
#Задача 3

import json

data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

key_list = list(data.keys())
value_list = list(data.values())
print(f'{key_list}\n{value_list}')      # Вывести списки ключей и значений словаря.

data['ETH']['total_diff'] = 100     # В “ETH” добавить ключ “total_diff” со значением 100.

data['tokens'][0]["fst_token_info"]['name'] = 'doge'
print(data['tokens'][0]["fst_token_info"])                  # Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.

x = data['tokens'][0].pop("total_out")
data['ETH']['total_out'] = x
print(data['ETH']['total_out'])                 # Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.



data['tokens'][1]["sec_token_info"]['total_price'] = data['tokens'][1]["sec_token_info"]["price"]
data['tokens'][1]["sec_token_info"].pop('price')
print(json.dumps(data['tokens'][1]["sec_token_info"], indent=4))            # Внутри "sec_token_info" изменить название ключа “price” на “total_price”.


#################################################################################################
#Задача 4


