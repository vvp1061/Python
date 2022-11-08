# Вариант 10
# 1. В одномерном массиве, состоящем из п целых элементов. Упорядочить элементы массива, стоящие между
# первым элементом массива и последним максимальным элементом массива по невозрастанию.
# 2. Дан массив A размера N.
# Сформировать два новых массива B и C: в массив B записать все положительные элементы массива A, в массив C — все
# отрицательные (сохраняя исходный порядок следования элементов). Вывести вначале размер и содержимое массива B,
# а затем — размер и содержимое массива C.

from random import randint

n = int(input('Введите n: '))

array = []

for i in range(n):
    array.append(randint(-15, 15))
    print(array[i], end=' ')
print('')

array[1:len(array)-1] = sorted(array[1:len(array)-1], reverse=True)

for i in range(n):
    print(array[i], end=' ')


del array

array = []
arrayB = []
arrayC = []

print('\nИсходный массив А:')
for i in range(n):
    array.append(randint(-15, 15))
    print(array[i], end=' ')

for i in range(n):
    if array[i] > 0:
        arrayB.append(array[i])
    elif array[i] < 0:
        arrayC.append(array[i])

print("\nДлина массива B: {}\nМассив B:".format(len(arrayB)))
for i in range(len(arrayB)):
    print(arrayB[i], end=' ')
print("\nДлина массива C: {}\nМассив C:".format(len(arrayC)))
for i in range(len(arrayC)):
    print(arrayC[i], end=' ')
