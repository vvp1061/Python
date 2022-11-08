n, m = int(input()), int(input())
matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * m

for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input())

imax, jmax, maximum = 0, 0, matrix[0][0]

print("Наша матрица:")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            imax = i
            jmax = j
            maximum = matrix[i][j]

print(matrix[imax][jmax], imax, jmax)

print('Сумма положительных элементов в каждой строке')
for i in range(n):
    sump = 0
    for j in range(m):
        if matrix[i][j] > 0:
            sump += matrix[i][j]
    print(sump)

# 3.

print('Введите размер квадратной матрицы')
N = int(input())

matrix1 = [0] * N
for i in range(N):
    matrix1[i] = [0] * N

for i in range(N):
    for j in range(N):
        matrix1[i][j] = int(input())

s1 = 0
for i in range(N):
    s1 += matrix1[i][0]

count = 0
for i in range(N):
    for j in range(N):
        if matrix1[i][j] > s1 and i < j:
            count += 1

print("Наша матрица:")
for i in range(N):
    for j in range(N):
        print(matrix1[i][j], end=" ")
    print()
print('Искомое количество элементов', count)