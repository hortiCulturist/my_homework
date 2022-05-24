#################################################################################################
#Задача 1

words = input('Введите строку: ')
symbols = list(words)
counter = 0

for i in symbols:
    if i == ':':
        index = symbols.index(i)
        symbols[index] = ";"
        counter += 1
print('Исправленная строка:')
for n in symbols:
    print(n, end='')

print('\nКол-во замен: ',counter)

#################################################################################################
#Задача 2

lline = input('Введите строку: ')
sym = int(input('Номер символа: '))
sym += 1
symbol = lline[sym-1]
right = lline[sym]
left = lline[sym-2]

if symbol == right and symbol == left:
    print('Есть два таких же символа')
elif symbol == right or symbol == left:
    print('Есть ровно один такой же символ.')
else:
    print('Таких же символов нет.')

print('Символ:',symbol,'\nПравый:',right,'\nЛевый:',left)

#################################################################################################
#Задача 3

words_list = []
counts = [0, 0, 0]

for i in range(3):
    print('Введите', i + 1, 'слово:', end=' ')
    word = input()
    words_list.append(word)

text = input('Слов из текста: ')
while text != 'end':
    for index in range(3):
        if words_list[index] == text:
            counts[index] += 1
    text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте')
for i in range(3):
    print(words_list[i], ':', counts[i])