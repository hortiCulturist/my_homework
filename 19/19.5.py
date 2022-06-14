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

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
for product_name, product_code in goods.items():
    it_quantity = 0
    it_cost = 0
    it_total_quantity = 0
    it_total_cost = 0
    for product in store[product_code]:
        it_quantity = 0
        it_cost = 0
        it_quantity += product['quantity']
        it_cost += product['price']
        it_total_cost += it_quantity * it_cost
        it_total_quantity += it_quantity
    print(f'{product_name} - {it_total_quantity} шт, общая стоимость {it_total_cost} рублей')

#################################################################################################
#Задача 5


#################################################################################################
#Задача 6

inser = int(input('Введите количество пар слов:'))
word_dict = dict()
for i in  range(1, inser + 1):
    text = input(f'{i} пара: ').lower().split(' - ')
    word_dict[text[0]] = text[1]
    word_dict[text[1]] = text[0]

while True:
    word = input('Введите слово: ').lower()
    if word in word_dict:
        print('Синоним:', word_dict[word])
    else:
        print('Такого слова в словаре нет.')

# Привет - Здравствуйте
# Печально - Грустно
# # Весело - Радостно

#################################################################################################
#Задача 7

order = int(input('Введите количество заказов:'))
order_dict = dict()
for i in range(1, order + 1):
    text = input(f'{i} order: ').lower().split()
    if text[0] in order_dict:
        if text[1] in order_dict[text[0]]:
            order_dict[text[0]][text[1]] += int(text[2])
        else:
            order_dict[text[0]][text[1]] = text[2]
    else:
        order_dict[text[0]] = dict({text[1]: int(text[2])})

for j_1 in sorted(order_dict):
    print(f'\n{j_1}')
    for j_2 in sorted(order_dict[j_1]):
        print(f'\n{j_2}: {order_dict[j_1][j_2]}')

#################################################################################################
#Задача 8





#################################################################################################
#Задача 9

def fam_def(name):
    if name not in parents_tree:
        heights[name] = 0
        return 0
    parent = parents_tree[name]
    if parent in heights:
        value = heights[parent] + 1
    else:
        value = fam_def(
            parent) + 1
    heights[name] = value
    return value

people = int(input('Введите количество человек:'))
parents_tree = {}

for i in range(1, people + 1):
    line = input(f'{i} пара:')
    child, parent = line.split()
    parents_tree[child] = parent

all_man = set(parents_tree.keys()) | set(parents_tree.values())

heights = {}

for name in all_man:
    if name not in heights:
        fam_def(name)

print(f'«Высота» каждого члена семьи:\n')
for name in sorted(heights):
    print(f'{name}, {heights[name]}')


#################################################################################################
#Задача 10

def can_make_pal(stri):
    d = {}
    for i in stri:
        if d.get(i) is None:
            d[i] = 1
        else:
            d[i] += 1
    n = len(d)
    e = 0
    for j in d.values():
        if j % 2 == 0:
            e += 1
    return e == n or e == n-1

string = input('Введите строку:')

if can_make_pal(string):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')