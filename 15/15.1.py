#################################################################################################
#Задача 1

numbers = [3,7,5]

while True:
 number = int(input('Новое число: '))
 numbers.append(number)
 print('Текущий список чисел:', numbers)

 for i in numbers:
   print(i ** 2, i ** 3, i ** 4)

 print()

#################################################################################################
#Задача 2

numbers = []

for i in range(100 +1):
    numbers.append(i)

print(numbers)

#################################################################################################
#Задача 3

human_in_office = int(input('Кол-во сотрудников в офисе: '))
ID_list = []
counter = 0

for i in range(human_in_office):
    ID_list.append(int(input('ID сотрудника: ')))

Find_ID = int(input('Какой ID ищем? '))

for i in ID_list:
    if Find_ID == i:
        counter += 1

if counter == 1:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')
