"""
Вариант 1
1. Дана целочисленная матрица A(N, N), заполненная целыми
числами. Все ее элементы, кратные трем, записать в одномерный
массив, а остальные в другой.
2. Дана целочисленная матрица A(N, N), заполненная целыми
числами. Отсортировать по возрастанию элементы матрицы, от
первого элемента до первого минимального элемента матрицы.
"""
import random
n = int(input())

matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * n

arr1 = []
arr2 = []
for i in range(n):
    for j in range(n):
        matrix[i][j] = random.randint(0,100)
        if matrix[i][j] % 3 == 0:
            arr1.append(matrix[i][j])
        else:
            arr2.append(matrix[i][j])

print('Ответ на первую задачу: ')
print(arr1)
print(arr2)

print("Наша матрица:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

# 2.

arr3 = []
minimum = matrix[0][0]
imin = 0
jmin = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] < minimum:
            minimum = matrix[i][j]
            imin = i
            jmin = j  # Нашли минимальный элемент матрицы

for i in range(imin + 1):
    for j in range(jmin + 1):
        arr3.append(matrix[i][j])
arr3.sort()

k = 0

for i in range(imin + 1):
    for j in range(jmin + 1):
        matrix[i][j] = arr3[k]
        k += 1

# Вывод массива
print('Ответ на вторую задачу: ')
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()