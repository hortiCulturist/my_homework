#################################################################################################
#Задача 1

first = int(input(f'Левая граница: '))
second = int(input(f'Правая граница: '))

qube = [first ** 3 for first in range(first,second + 1)]
print(qube)
square = [first ** 2 for first in range(first,second + 1)]
print(square)

#################################################################################################
#Задача 2

first = input(f'Введите строку: ')
second = input(f'Введите дополнительный символ: ')

qube = [first * 2 for first in first]
print(qube)
square = [qube + second for qube in qube]
print(square)

#################################################################################################
#Задача 3

def get_prise(percent,prise):
    return round(prise * (1 + percent / 100), 2)

month = int(input(f'Введите количество товаров: '))
prises_now = []
for i in range(month):
    prise = float(input(f'Введите цену: '))
    prises_now.append(prise)

prices_first = int(input(f'Повышение на первый год: '))
prices_second = int(input(f'Повышение на второй год: '))

one = [get_prise(prices_first, i)for n_prise in prises_now]
two =  [get_prise(prices_second, i)for n_prise in one]

print(f'Сумма цен за каждый год: {sum(prises_now)} {sum(one)} {sum(two)}')
