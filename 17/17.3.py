#################################################################################################
#Задача 1

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))

even_list = [i for i in range(a,b) if i % 2 != 0]

print(even_list)

#################################################################################################
#Задача 2

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

new_prices = [(i if i > 0 else 0) for i in original_prices]

print(new_prices)

#################################################################################################
#Задача 3

import random

first_sqad = [random.randint(50, 80) for _ in range(10)]
second_sqad = [random.randint(30, 60) for _ in range(10)]
sqad = [(f'погиб' if first_sqad[i] + second_sqad[i] > 100 else f'выжил')for i in range(10)]

print(first_sqad)
print(second_sqad)
print(sqad)