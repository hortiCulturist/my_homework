count_number = int(input('Введите кол-во чисел: '))
number = []


for _ in range(count_number):
    num = int(input('Введите число: '))
    number.append(num)
print(f'Изначальный список: {number}')


swapped = True
while swapped:
    swapped = False
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            number[i], number[i + 1] = number[i + 1], number[i]
            swapped = True

print(f'Отсортированный список:  {number}')