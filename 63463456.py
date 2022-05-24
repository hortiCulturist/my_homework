import math


def reverserB(x):
    number = 0
    while x - math.trunc(x) > 0:
        temp_x = math.trunc(x * 10)
        t = temp_x % 10
        x = round(x, 5) * 10
        number += t
        number /= 10
    return number


def reverserB2(x):
    x = math.trunc(x)
    number = 0
    while x > 0.99:
        number *= 10
        t = x % 10
        x = x / 10
        x = math.trunc(x)
        number += t
    return (number)


x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))

print('Первое число наоборот: ', reverserB(x) + reverserB2(x))
print('Второе число наоборот: ', reverserB(y) + reverserB2(y))

print('Сумма: ', reverserB(x) + reverserB2(x) + reverserB(y) + reverserB2(y))