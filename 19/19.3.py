#################################################################################################
#Задача 1

family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },

        {
            "name": "Bob",
            "age": 8
        }
    ]
}

print(family_member['children'][1]["name"])




#################################################################################################
#Задача 2

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

team1 = [

    player['name']
    for player in players_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'

]

print(f'Задание 1: {team1}')


team2 = [

    player['name']
    for player in players_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'

]

print(f'Задание 2: {team2}')


team3 = [

    player['name']
    for player in players_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'

]

print(f'Задание 3: {team3}')