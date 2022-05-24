num_in_list = int(input('Кол-во чисел в списке: '))
listt = []

summa = 0

for i in range(num_in_list):
    listt.append(int(input('Введите число: ')))

divider = int(input('Введите делитель:'))

for i in range(num_in_list):
    if listt[i] % divider == 0:
        print(f"Индекс числа {listt[i]}: {i}")
        summa += i

print(f"Сумма индексов: {summa}")
