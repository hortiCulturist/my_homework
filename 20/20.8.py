#################################################################################################
#Задача 1

def func(dict):
    lst = []
    string = ''
    for i in dict:
        print(i)
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for _ in string:
        cnt += 1
    return lst, cnt

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


pairs = [(i, students[i]['age']) for i in students]
# for i in students:
#     pairs += (i, students[i]['age'])


my_lst = func(students)[0]
surname_size = func(students)[1]
print(f'Список пар "ID студента — возраст": {pairs}')
print(f'Полный список интересов всех студентов: {my_lst}')
print(f'Общая длина всех фамилий студентов: {surname_size}')

#################################################################################################
#Задача 2

#################################################################################################
#Задача 3

def slicer(j, i):
    if i not in j:
        return ()
    if j.count(i) == 1:
        return j[j.index(i):]
    return j[j.index(i):j.index(i, j.index(i) + 1) + 1]


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))

#################################################################################################
#Задача 4

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
new_players_tuple = list(i_key + i_value for i_key, i_value in players.items())

print(f"Результат работы программы: \n{new_players_tuple}")


#[('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]

#################################################################################################
#Задача 5

family = {
    'Сидоров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10,
    'Петров Виктор': 15,
    'Петрова Дарья': 16
}

search = input('Кого ищем? ').lower()
result = []
for i in family:
    if search in i.split()[0].lower():
        result.append(i+' '+str(family[i]))

if not result:
    print('Поиск не дал результатов')
else:
    for j in result:
        print(j)

#################################################################################################
#Задача 6