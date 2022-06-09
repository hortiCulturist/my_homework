#################################################################################################
#Задача 1

simbol = {'.', ',', ';', ':', '!', '?'}
counter = 0
text = input(f'Введите текст: ')

for i in text:
    if i in simbol:
        counter += 1

print(f'Количество знаков пунктуации:', counter)

#################################################################################################
#Задача 2

import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

un_nums1 = set(nums_1)
print(f'1-е множество:{un_nums1}')

un_nums2 = set(nums_2)
print(f'1-е множество:{un_nums2}')

mininmum1 = min(un_nums1)
un_nums1.discard(mininmum1)
print(f'Минимальный элемент 1-го множества:{mininmum1}')

mininmum2 = min(un_nums2)
un_nums2.discard(mininmum2)
print(f'Минимальный элемент 2-го множества:{mininmum2}')

rand1 = random.randint(100, 200)
un_nums1.add(rand1)
print(f'Случайное число для 1-го множества:{rand1}')

rand2 = random.randint(100, 200)
un_nums1.add(rand2)
print(f'Случайное число для 2-го множества:{rand2}')

all_nums = un_nums1.union(un_nums2)     #Вывести все элементы множеств (объединение).
print(f'Объединение множеств:{all_nums}')

inter = un_nums1.intersection(un_nums2)     #Вывести только общие элементы (пересечение).
print(f'Пересечение множеств:{inter}')

dif = un_nums2.difference(un_nums1)     #Вывести элементы, входящие в nums_2, но не входящие в nums_1
print(f'Элементы, входящие в nums_2, но не входящие в nums_1:{dif}')

#################################################################################################
#Задача 3

text = input('Введите текст: ')

uniq_numbers_list = [int(symbols) for symbols in set(text) if '0' <= symbols <= '9']

print(uniq_numbers_list)

