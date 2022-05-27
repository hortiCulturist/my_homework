#################################################################################################
#Задача 1

main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

main.extend(first_company)
main.extend(second_company)
main.extend(third_company)

x = main.count(0)

print('Общий список задач:', main)
print('Кол-во невыполненных задач:', x)

#################################################################################################
#Задача 2

first_massage = input('Первое сообщение:')
second_massage = input('Первое сообщение:')
counter1 = 0
counter2 = 0

for i in first_massage:
    if i == '!' or i == '?':
        counter1 += 1

for i in second_massage:
    if i == '!' or i == '?':
        counter2 += 1

if counter1 > counter2:
    print(first_massage + second_massage)
if counter2 > counter1:
    print(second_massage + first_massage)