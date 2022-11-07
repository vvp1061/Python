# Вариант 10
# 1. В одномерном массиве, состоящем из п целых элементов, найти номер последней пары подряд идущих
# элементов массива, произведение которых нечетно, а сумма положительна.
# 2. В одномерном массиве, состоящем из п
# целых чисел удалить элементы, последняя цифра которых кратна 3.
# 3. В одномерный массив, состоящий из п целых чисел
# вставить новый элемент перед всеми нечётными числами стоящими на чётных местах.

import random

n = int(input('Введите n: '))

array = []
index_of_pair = 0
for i in range(n):
    array.append(random.randint(-15, 15))
    print(array[i], end=' ')
print('')

# for i in range(n):
#     array.append(int(input('Введите эл-т массива: ')))
array.reverse()
for i in range(n - 1):
    if (array[i] * array[i + 1]) % 2 != 0 and (array[i] + array[i + 1]) > 0:
        index_of_pair = len(array) - 1 - i
        print('Номер последней пары:', index_of_pair)
        break

if index_of_pair == 0:
    print('Нет таких пар')
del array
# 2
array = []

n = int(input('Введите n: '))

for i in range(n):
    array.append(random.randint(-15, 15))
    print(array[i], end=' ')
print('')

i = n - 1
while i >= 0:
    if (abs(array[i]) % 10) % 3 == 0:
        del array[i]
    i -= 1

print('Массив после удаления:')
for i in range(len(array)):
    print(array[i], end=' ')
