#################################################################################################
#Задача 1

words = [input(f'Введите слово номер { i+1 } :') for i in range(3)]
text = input('Введите текст:')

for word in words:
    print(f'слово { word } встречается в тексте { text.count(word) } раз')

#################################################################################################
#Задача 2

text = input('Введите текст:').split()
print(' '.join(text))

#################################################################################################
#Задача 3

while True:
    congratulation = input("Введите шаблон поздравнелия где имя это {user}, возраст это {age}:")
    if '{user}' in congratulation and '{age}' in congratulation:
        break
    print('Ошибка')

names = input('Введите имя и фамилию через запятую:').split(', ')
ages = input('Введите возраст через пробел: ')
age = [int(i) for i in ages.split()]

for j in range(len(names)):
    print(congratulation.format(user=names[j], age=age[j]))
