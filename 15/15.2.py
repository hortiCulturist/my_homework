#################################################################################################
#Задача 1

nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))

    nums_list.append(num)

maximum = nums_list[0]
minimum = nums_list[0]

for i in nums_list:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print('Максимальное число в списке:', maximum)

print('Минимальное число в списке:', minimum)

#################################################################################################
#Задача 2

