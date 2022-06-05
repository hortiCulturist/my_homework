#################################################################################################
#Задача 1

menu = input('Доступное меню через ";" :').split(';')
print(f'На данный момент в меню есть :{", ".join(menu)}')

#################################################################################################
#Задача 2

word = input('Введите строку:').split()
maximum = (word[0])

for i in range(1, len(word)):
    if len(word[i]) > len(maximum):maximum = word[i]

print(f'Самое длинное слово: {maximum}')
print(f'Длина этого слова: {len(maximum)}')

#################################################################################################
#Задача 3

file = input('Название файла:')

if file.startswith(('@', '№', '$', '%', '^', '&', '*', '(', ')')):
    print('Ошибка: название начинается на один из специальных символов.')
elif not file.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')

#################################################################################################
#Задача 4

word = input('Введите строку:').split(' ')
cap_word = []

for i in word:
    cap_word.append(i.capitalize())
    words = " ".join(cap_word)
print(words)

#################################################################################################
#Задача 5

while True:
    password = input('Придумайте пароль:')
    if len(password) < 8 and password.islower() == False and password.isdigit() == False:
        print('Это надёжный пароль!')
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

#################################################################################################
#Задача 6

def compression(text):
   counter = 1
   compressed = []

   for symbol in range(len(text)):
      if text[symbol] == text[symbol + 1: symbol + 2]:
         counter += 1
         continue
      compressed.append(text[symbol] + str(counter))
      counter = 1

   return compressed


plain_text = input('Введите строку:')
print('Закодированная строка: {}'.format(''.join(compression(plain_text))))

#################################################################################################
#Задача 7

ip = input('Введите строку IP: ').split('.')

if len(ip) < 4:
   print('Адрес - это четыре числа, разделенные точками')
else:
   count_number = 0
for i in ip:

   if i.isdigit():
      if int(i) <= 255:
         count_number += 1
         continue
      else:
         print(i, 'превышает 255')
   else:
      print(i, 'не целое число')
      break

if count_number == 4:
   print("IP-адрес корректен")

#################################################################################################
#Задача 8

str_1 = input('Первая строка: ')
str_2 = input('Вторая строка: ')

if str_1 == str_2:
    print('Строки одинаковые')
else:
    if len(str_1) != len(str_2):
        print('Строки имеют разную длинну')
    else:
        shift = 1
        flag = False
        for _ in range(len(str_1) - 1):
            str_2 = str_2[-1] + str_2[:-1]
            if str_1 == str_2:
                print(f'Первая строка получается из второй со сдвигом {shift}.')
                flag = True
                break
            else:
                shift += 1
        if not flag:
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

#################################################################################################
#Задача 9

massege = input('Сообщение:').split()
listt = []
for i in massege:
    listt.append(i[::-1])
    endd = " ".join(listt)
print(endd)

#################################################################################################
#Задача 10

