#################################################################################################
#Задача 1

nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))

    nums_list.append(num)

maximum = nums_list[0]
minimum = nums_list[0]

for i in nums_list:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print('Максимальное число в списке:', maximum)

print('Минимальное число в списке:', minimum)

#################################################################################################
#Задача 2

num_in_list = int(input('Кол-во чисел в списке: '))
listt = []

summa = 0

for i in range(num_in_list):
    listt.append(int(input('Введите число: ')))

divider = int(input('Введите делитель:'))

for i in range(num_in_list):
    if listt[i] % divider == 0:
        print(f"Индекс числа {listt[i]}: {i}")
        summa += i

print(f"Сумма индексов: {summa}")

#################################################################################################
#Задача 3

from random import randint

num_in_list = int(input('Введите кол-во собак: '))
listt = []

for i in range(num_in_list):
    listt.append(randint(1,50))
print(listt)

max_num = max(listt)
min_num = min(listt)
print('max: ',max_num,'\nmin: ',min_num)

for n in listt:
    if max_num == n:
        in_max = listt.index(n)

    if min_num == n:
        in_min = listt.index(n)


listt[in_max], listt[in_min] = listt[in_min], listt[in_max]
print(listt)