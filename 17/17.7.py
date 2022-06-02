#################################################################################################
#Задача 1

exceptions = "аоиеёэыуюя"

text = input("Введите текст: ")
letters = [c for c in text if c in exceptions]
print("Список гласных букв:", letters)
print("Длина списка:", len(letters))

#################################################################################################
#Задача 2

or_list = [i % 5 if i % 2 else 1 for i in range(int(input('введите число')))]

print(or_list)

#################################################################################################
#Задача 3

import random

first_list = [round(random.uniform(5,10),2) for _ in range(20)]
second_list = [round(random.uniform(5,10),2) for _ in range(20)]
winer_list = []

for i in range(20):
    if first_list[i] > second_list[i]:
        winer_list.append(first_list[i])
    else:
        winer_list.append(second_list[i])

print(f'Первая команда: {first_list}')
print(f'Вторая команда: {second_list}')
print(f'Победители: {winer_list}')

#################################################################################################
#Задача 4

alphabet = 'abcdefg'

alphabet1 = alphabet[:]
alphabet2 = alphabet[:]
alphabet3 = alphabet[:]
alphabet4 = alphabet[:]
alphabet5 = alphabet[:]
alphabet6 = alphabet[:]
alphabet7 = alphabet[:]
alphabet8 = alphabet[:]
alphabet9 = alphabet[:]
alphabet10 = alphabet[:]

print(f'1: {alphabet1}')
print(f'2: {alphabet2[::-1]}')
print(f'3: {alphabet3[::2]}')
print(f'4: {alphabet4[1:7:2]}')
print(f'5: {alphabet5[:1]}')
print(f'6: {alphabet6[7:5:-1]}')
print(f'7: {alphabet7[3:4]}')
print(f'8: {alphabet8[4:]}')
print(f'9: {alphabet9[3:5]}')
print(f'10:{alphabet10[4:2:-1]}')

#################################################################################################
#Задача 5

H = input('Введите строку: ')

a = H[:H.find('h')]
b = H[H.find('h'):H.rfind('h') + 1]
c = b[::-1]

print(f'Развёрнутая последовательность между первым и последним h: {c}')

#################################################################################################
#Задача 6

import random

numbers = int(input('Количество чисел в списке: '))

num_list = [random.randint(0,2) for _ in range(numbers)]
listt = []
zero = 0

for i in num_list:
    if i == 0:
        num_list.append(i)
        num_list.remove(i)

for i in num_list:
    if i == 0:
        zero += 1

for i in range(zero):
    num_list.remove(0)

print(num_list)

#################################################################################################
#Задача 7

a = 12
b = 4

listt =[[i_num + i for i_num in range(0, a, 4)]for i in range(1, b + 1)]

print(listt)

#################################################################################################
#Задача 8!!!!!!

#################################################################################################
#Задача 9

listt = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

flat_list = [layer3 for layer1 in listt for layer2 in layer1 for layer3 in layer2]
print(flat_list)

#################################################################################################
#Задача 10

alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг:'))
cipher = ''

for i in message:
    place = alfavit.find(i)
    new_place = place + shift
    if i in alfavit:
        cipher += alfavit[new_place]  # Задаем значения в итог
    else:
        cipher += i
print (cipher)


