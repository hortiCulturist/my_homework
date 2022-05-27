#################################################################################################
#Задача 1

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

zoo.insert(1, 'bear')
zoo.remove('elephant')

print(zoo)
print('Лев сидит в клетке номер', zoo.index('lion'))
print('Обезьяна сидит в клетке номер', zoo.index('monkey'))

#################################################################################################
#Задача 2

amount = int(input('Кол-во сотрудников: '))
money = []
counter = 0

for _ in range(amount):
    x = int(input('Зарплата сотрудника: '))
    counter += 1
    money.append(x)

for n in range(counter):
    for i in money:
        if i == 0:
            money.remove(i)

mx_money = max(money)
mi_money = min(money)

print('\nОсталось сотрудников:', len(money))
print('Зарплаты:', money)
print('Максимальная зп: ', mx_money)
print('Минимальная зп: ', mi_money)
