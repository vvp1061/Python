# Вариант 10
# 1. Дана матрица размера M × N (N — чётное число). Поменять местами левую и правую половины матрицы.
# 2. Дана матрица размера M × N. Удалить из нее последнюю из строк, сумма нечётных элементов,
# в которых больше заданного числа P.
# 3. Дана матрица размера M × N. Продублировать строку матрицы, содержащую ее максимальный элемент,
# вставив ее после первой строки.

from random import randint

A = []
M = int(input('Введите M: '))
N = int(input('Введите N: '))
while N % 2 != 0:
    N = int(input('Введите N: '))

for i in range(M):
    A.append([0] * N)

print('\nИсходная матрица: ')

for i in range(M):
    for j in range(N):
        A[i][j] = randint(0, 10)
        print("\t%2d" % (A[i][j]), end=' ')
    print()

print('\nОтзеркаленная матрица: ')

halfN = int(N / 2)
for i in range(M):
    for j in range(halfN):
        A[i][j], A[i][j + halfN] = A[i][j + halfN], A[i][j]

for i in range(M):
    for j in range(N):
        print("\t%2d" % (A[i][j]), end=' ')
    print()

del A, M, N

print('=' * 36)


M = int(input('Введите M: '))
N = int(input('Введите N: '))

while N % 2 != 0:
    N = int(input('Введите N: '))

A = []
for i in range(M):
    A.append([0] * N)

B = []
for i in range(M):
    B.append([0] * N)

print('\nИсходная матрица: ')

for i in range(M):
    for j in range(N):
        A[i][j] = randint(0, 10)
        print("\t%2d" % (A[i][j]), end=' ')
    print()
print()

P = int(input('Введите P: '))

sumTemp = []
minRow = 0

for i in range(M):
    for j in range(N):
        if A[i][j] % 2 != 0:
            sumTemp.append(A[i][j])
    if sum(sumTemp) > P:
        minRow = i
    sumTemp.clear()
del A[minRow]

for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%2d" % (A[i][j]), end=' ')
    print()
print()

del A, M, N

print('=' * 36)

A = []

M = int(input('Введите M: '))
N = int(input('Введите N: '))

for i in range(M):
    A.append([0] * N)

print('\nИсходная матрица: ')

for i in range(M):
    for j in range(N):
        A[i][j] = randint(-100, 100)
        print("\t%3d" % (A[i][j]), end=' ')
    print()

maximum = A[0][0]
maxRow = 0

for i in range(M):
    for j in range(N):
        if maximum < A[i][j]:
            maximum = A[i][j]
            maxRow = i

print('\nМатрица после: ')

A.insert(1, A[maxRow])

for i in range(len(A)):
    for j in range(len(A[i])):
        print("\t%3d" % (A[i][j]), end=' ')
    print()

