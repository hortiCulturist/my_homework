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

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(zip(num_list[::2], num_list[1::2]))

print(f"Новый список: { result } ")

#################################################################################################
#Задача 7

def tpl_sort(num_list):
    num_list = tuple(sorted(num_list))
    return num_list

numbers = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(numbers))

#################################################################################################
#Задача 8

def add_contact(con):
    name_sur = tuple(input('\nВведите имя и фамилию нового контакта (через пробел):').split(' '))
    number = input('Введите номер телефона:')
    if name_sur in con:
        print('\nТакой человек уже есть в контактах.')
    else:
        con[name_sur] = number
    print(f'Текущий словарь контактов: {con}\n')

def find(con):
    surname_find = input('\nВведите фамилию для поиска:')
    for i in con:
        if surname_find in i:
            name = [j for j in i]
            phone_number = con[i]
            print(' '.join(name), phone_number)


contact = dict()
while True:
    choise = int(input('Введите номер действия: \n1. Добавить контакт \n2. Найти человека \n'))
    if choise == 1:
        add_contact(contact)
    elif choise == 2:
        find(contact)
    else:
        print('Не корректный ввод! Повторите ввод\n')

#################################################################################################
#Задача 9

def score_key(a):
    return a[1][0] * 100000000 - a[1][1]

score_table = {}
number_rows = int(input('Общее количество строк протокола: '))
print('Введите результат - имя участника (через пробел)')
for time in range(number_rows):
    ball, name = input('{0} запись:'.format(time + 1)).split()
    ball = int(ball)
    if name in score_table:
        if ball > score_table[name][0]:
            score_table[name][0] = ball
            score_table[name][1] = time
    else:
        score_table[name] = [ball, time]
scores = list(score_table.items())

scores.sort(key=score_key, reverse=True)
print('\nИтоги соревнований: ')
for winner_index in 0, 1, 2:
    print(f'{winner_index + 1} место {scores[winner_index][0]}', end=' ')
    print(f'({scores[winner_index][1][0]})', sep='')

#################################################################################################
#Задача 10

def ziper(symbol, number):
    counter = 0
    x = tuple()
    y = list(symbol)
    for i in number:
        x = (y[counter], i)
        counter += 1
        print(x)

str = input('Строка:')
tup_num = tuple((10, 20, 30, 40))

ziper(str, tup_num)