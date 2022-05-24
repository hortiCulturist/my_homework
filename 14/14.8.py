#Задача 2

print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))
k = 0


x_diff = x1 - x2
y_diff = y1 - y2

if x_diff == 0 or y_diff == 0:
    x_diff = x_diff
    y_diff = y_diff
else:
    k = y_diff / x_diff

b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)

#################################################################################################
#Задача 3

number = int(input('Введите число: '))
suma = 0

def number_summ(number):
    summ = 0
    while number > 0:
       digit = number % 10
       summ += digit
       number = number // 10
    return suma
    print('\nСумма цифр:', summ)


def count_number(number):
    x = 0
    co_num = number
    while co_num > 0:
        x += 1
        co_num //= 10
    return x
    print('Кол-во цифр в числе:', x)


def diff_number(number_summ, count_number):
    diff = number_summ(number) - count_number(number)
    print('\nСумма цифр:', number_summ(number))
    print('Кол-во цифр в числе:', count_number(number))
    print('Разность суммы и кол-ва цифр:', diff)

diff_number(number_summ, count_number)

#################################################################################################
#Задача 4

number_1 = float(input('Введите первое число:'))
number_2 = float(input('Введите второе число:'))


def number_reverse(number):
    x = int(number_1)
    n = 0

    while x > 0:
        digit = x % 10
        x = x // 10
        n = n * 10
        n = n + digit
    return n

def number_rev_after(number):
    y = ''
    for i in reversed(str(number_1)):
        if i == '.':
            break
        y += i
        y = float('0.' + y)
        return y

def number_summ(number_1, number_2):
    num1 = number_reverse(number_1) + number_rev_after(number_1)
    num2 = number_reverse(number_2) + number_rev_after(number_2)

    number_summ = num1 + num2

    print('Первое число наоборот: ', num1)
    print('Второе число наоборот: ', num2)
    print('Их сумма: ',number_summ)

number_summ(number_1, number_2)

#################################################################################################
#Задача 5

def get_gcd(a):
    gcd = 1
    for i in range(1, a + 1):
        if a % i == 0:
            gcd = i
        if gcd > 1:
            break
    return gcd


number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', get_gcd(number))

#################################################################################################
#Задача 7

year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))


def counter(year1, year2,):
    print('Годы от ',year1,' до ',year2,' с тремя одинаковыми цифрами:')
    for i in range(year1, year2 +1,):
        x1 = i // 1000
        x2 = i // 100
        x2 -= x1 * 10
        x3 = i % 100
        x3 -= x3 % 10
        x3 = x3 / 10
        x3 = int(x3)
        x4 = i % 10
        #print(x1,x2,x3,x4)
        if x2 == x3 and x4 == x2 and x4 == x3:
            year = x1 * 1000 + x2 * 100 + x3 * 10 + x4 * 1
            print(year)
        if x1 == x3 and x4 == x1 and x4 == x3:
            year = x1 * 1000 + x2 * 100 + x3 * 10 + x4 * 1
            print(year)


counter(year1, year2)
