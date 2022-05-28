#################################################################################################
#Задача 1

a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

maximum = max(a)


a = a + b
print('Кол-во цифр 5 при первом объединении:', (a.count(5)))
for i in a:
    if i == maximum:
        a.remove(maximum)

a = a + c
print('Кол-во цифр 3 при втором объединении:', (a.count(3)))


print(a)

#################################################################################################
#Задача 2

size_list = []

for i in range(160,176 + 1,2):
    size_list.append(i)

for i in range(162,180 + 1,3):
    size_list.append(i)

size_list.sort()

print(f'Отсортированный список учеников: {size_list}')

#################################################################################################
#Задача 3

shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

request_product = input('Введите название детали:')
product = 0
product_list = []
prise = 0

for i in shop:
    for j in i:
        if j == request_product:
            product += 1
            for f in i:
                product_list += i[1],[0]
                break

for m in (product_list[::2]):
    prise += m

print(f'\nКол-во деталей — {product}')
print(f'Общая стоимость — {prise}')

#################################################################################################
#Задача 4

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
counter_gu = 0
for i in range(len(guests)):
    counter_gu += 1


while True:
    print(f'Сейчас на вечеринке {counter_gu} человек: {guests}')
    choicer = str(input('Гость пришёл или ушёл?:'))
    if choicer == 'пришел' or choicer == 'Пришел':
        name_guest = str(input('Имя гостя: '))
        if counter_gu <= 6:
            guests.append(name_guest)
            counter_gu += 1
            print(f'Привет, {name_guest}!\n')

        if counter_gu == 7:
            counter_gu -= 1
            print(f'Прости, {name_guest}, но мест нет.\n')
    elif choicer == 'ушел' or choicer == 'Ушел':
        name_guest = str(input('Имя гостя: '))
        for i in guests:
            if name_guest == i:
                guests.remove(i)
                counter_gu -= 1
        print(f'Пока, {name_guest}!\n')

    elif choicer == 'пора спать' or choicer == 'Пора спать':
        print(f'Вечеринка закончилась, все легли спать.')
        break
    else:
        print(f'Ошибка ввода, напишите "пришел" гость или "ушел".\n')

#################################################################################################
#Задача 5

violator_songs = [['World in My Eyes', 4.86],
                  ['Sweetest Perfection', 4.43],
                  ['Personal Jesus', 4.56],
                  ['Halo', 4.90],
                  ['Waiting for the Night', 6.07],
                  ['Enjoy the Silence', 4.20],
                  ['Policy of Truth', 4.76],
                  ['Blue Dress', 4.29],
                  ['Clean', 5.83]]

all_list = []
flag = True
k = int(input('Сколько песен выбрать? '))

for i in range(1, k + 1):
    s = input('\nВведите название ' + str(i) + ' песни: ')
    flag = True
    for j in violator_songs:
        a = []
        a.extend(j)
        for l in a:
            if s == l:
                all_list += [s]
                flag = False
    if flag:
        print('\nОшибка. Такой песни в плейлисте нет!')
        break
    if i == k:
        summ = 0
        for i in violator_songs:
            if i[0] in all_list:
                summ += i[1]
        print('\nОбщее время звучания песен:', float(round(summ, 2)))

#################################################################################################
#Задача 6