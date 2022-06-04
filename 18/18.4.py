#################################################################################################
#Задача 1

alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()

message = input('Введите сообщение: ').lower()
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

#################################################################################################
#Задача 2

path_to_file = input('Путь к файлу:').upper()
disk = input('На каком диске должен лежать файл:').upper()
extension = input('Требуемое расширение файла:').upper()


if path_to_file.startswith(disk) and path_to_file.endswith(extension):
    print('Путь корректен!')
else:
    print('Путь не корректен!')

#################################################################################################
#Задача 3

text = input('Введите строку:')
End = ''
counter_s = 0
counter_b = 0

for i in text:
    if i.islower() == True:
        counter_s += 1
    if i.isupper() == True:
        counter_b += 1
if counter_s > counter_b:
    End = text.lower()
if counter_s < counter_b:
    End = text.upper()

print(End)





