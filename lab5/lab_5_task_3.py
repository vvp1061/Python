# Вариант 10
#     1. Дана целочисленная матрица A(N, N), заполненная целыми числами.
#     Сформировать одномерный массив, каждый элемент которого равен сумме
#     положительных элементов в соответствующем столбце, кратных 4 или 5.
#     2. Дана целочисленная матрица A(N, N), заполненная целыми числами.
#     Отсортировать по возрастанию чётные элементы матрицы.

from random import randint

A = []
B = []
C = []

N = int(input('Введите N: '))

for i in range(N):
    A.append([0] * N)

print('\nИсходная матрица: ')

for i in range(N):
    for j in range(N):
        A[i][j] = randint(95, 105)
        print("\t%5d" % (A[i][j]), end=' ')
    print()


for j in range(N):
    mySum = 0
    for i in range(N):
        if A[i][j] > 0 and A[i][j] % 4 == 0 and A[i][j] % 5 == 0:
            C.append(A[i][j])
            mySum = sum(C)
    C.clear()
    if mySum != 0:
        B.append(mySum)

print("\nОдномерный массив:\n", B)

del A, B, C, N

print('='*36)

A = []
B = []
N = int(input('Введите N: '))

for i in range(N):
    A.append([0] * N)

print('Исходная матрица: ')

for i in range(N):
    for j in range(N):
        A[i][j] = randint(0, 20)
        print("\t%3d" % (A[i][j]), end=' ')
        if abs(A[i][j]) % 2 == 0:
            B.append(A[i][j])
            B = sorted(B)
    print()

print('Чётные элементы массива:\n', B,'\nОтсортированная матрица:')
k = 0
for i in range(N):
    for j in range(N):
        if abs(A[i][j]) % 2 == 0:
            A[i][j] = B[k]
            k += 1
        print("\t%3d" % (A[i][j]), end=' ')
    print()
