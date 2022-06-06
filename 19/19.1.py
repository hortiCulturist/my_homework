#################################################################################################
#Задача 1

num = int(input('Введите число:'))
dicts = {}
for i in range(1, num + 1):
    dicts[i] = i ** 2
for j in dicts:
    print(j ,'-', dicts[j] )

#################################################################################################
#Задача 2

student_str = input('Введите данные:')

student_info = student_str.split()
student = dict()

student['Имя '] = student_info[0]
student['Фамилия'] = student_info[1]
student['Город'] = student_info[2]
student['Место учебы'] = student_info[3]
student['Оценки'] = []
for i in student_info[4:]:
    student['Оценки'].append(int(i))

print(student)

#################################################################################################
#Задача 3

phonebook = {}
while True:
    print(f'\nТекущие контакты на телефоне: \n{phonebook}')
    name = str(input('Введите имя:'))
    phone = int(input('Введите номер телефона:'))
    if name is not phonebook:
        phonebook[name] = phone
    elif name in phonebook:
        print('Ошибка: такое имя уже существует.')
