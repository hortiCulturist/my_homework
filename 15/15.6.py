#################################################################################################
#Задача 1

number = int(input('Введите число: '))
odd_numbers = []
for i in range(1,number):
    if i % 2 != 0:
        odd_numbers.append(i)

print('Список из нечётных чисел от одного до N:', odd_numbers)

#################################################################################################
#Задача 2

gamers = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []
x = 0
y = 0
for i in range(len(gamers)):
    if i % 2 == 0:
        first_day.append(gamers[i])

print('Первый день:',first_day)

#################################################################################################
#Задача 3

from random import randint

amount = int(input('Количество клеток: '))
efficiency = []
not_suitable = []


for i in range(amount):
    efficiency.append(randint(1,amount))
print(efficiency)

for i in range(len(efficiency)):
    if i < efficiency[i]:
        not_suitable.append(efficiency[i])
print('Неподходящие значения: ',not_suitable)

#################################################################################################
#Задача 4

amount = int(input('Количество видеокарт: '))
video_card_list = []

for n in range(amount):
    video_card_list.append(int(input('Модель видеокарты: ')))

max_card = max(video_card_list)
print(max_card)


while max_card in video_card_list:
    video_card_list.remove(max_card)

print(video_card_list)

#################################################################################################
#Задача 5

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite_films = []
count_film = int(input('Сколько фильмов хотите добавить? '))


for n in range(count_film):
    add_film = str(input('Введите название фильма:'))
    if add_film in films:
        favorite_films.append(add_film)
    else:
        print(f'Ошибка: фильма {add_film} у нас нет :(')


print('Ваш список любимых фильмов: ')
print('\n'.join(favorite_films))


#################################################################################################
#Задача 6
word = str(input('Введите слово: '))
list_word = list(word)
unique_word = 0

for i in list_word:
    counter = 0
    for n in list_word:
        if n == i:
            counter += 1
    if counter == 1:
        unique_word += 1

print(f'Количество уникальных букв: {unique_word}')

#################################################################################################
#Задача 7

containers_num = int(input('Количество контейнеров: '))
containers = []
new_tov = int(input('Новый ящик: '))
counter = 0

for _ in range(containers_num):
    new_container = int(input('Введите вес нового контейнера: '))
    containers.append(new_container)

while counter < len(containers) and containers[counter] >= new_tov:
    counter += 1

print('Номер, который получит новый контейнер:', counter + 1)

#################################################################################################
#Задача 8

all_element = int(input('Сколько элементов в списке: '))
lists = []

for i in range(all_element):
    element = int(input('Введите значение элемента: '))
    lists.append(element)

shift = int(input('Сдвиг: '))
print(f'Было: {lists}')

for n in range(shift):
    index = 0
    save = lists[index - 1]
for i in range(len(lists) - 1):
    lists[index - 1] = lists[index - 2]
    index -= 1
lists[0] = save
print(f'Стало: {lists}')

#################################################################################################
#Задача 9

word = str(input('Введите слово: '))
x = word[::-1]
if word == x:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

#################################################################################################
#Задача 10

count_number = int(input('Введите кол-во чисел: '))
number = []


for _ in range(count_number):
    num = int(input('Введите число: '))
    number.append(num)
print(f'Изначальный список: {number}')


swapped = True
while swapped:
    swapped = False
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            number[i], number[i + 1] = number[i + 1], number[i]
            swapped = True

print(f'Отсортированный список:  {number}')