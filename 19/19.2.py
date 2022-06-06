#################################################################################################
#Задача 1

small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
big_storage.update(small_storage)
print("<База данных успешно обновлена>")
while True:
    product = (input('Введите товар:'))
    search = big_storage.get(product)
    if product in big_storage:
        print(f'Цена товара: {search}')
    else:
        print('Ошибка, такого товара нет.')

#################################################################################################
#Задача 2

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
all_summ = 0
min_summ = " "
for i in incomes:
    all_summ += incomes[i]
    min_summ = (min(incomes, key=incomes.get))
dell = incomes.pop(min_summ)
print(f'Общий доход за год составил {all_summ} рублей')
print(f'Самый маленький доход у {min_summ}. Он составляет {dell} рублей')
print(f'Итоговый словарь: {incomes}')

#################################################################################################
#Задача 3

def histogram(str):
    dictionary = dict()
    for sim in str:
        if sim in dictionary:
            dictionary[sim] += 1
        else:
            dictionary[sim] = 1
    return dictionary


text = input('Введите текст:').lower()
hist = histogram(text)

for i in sorted(hist.keys()):
    print(f'{i} - {hist[i]}')

print(f'Максимальное значение: {max(hist.values())}')


