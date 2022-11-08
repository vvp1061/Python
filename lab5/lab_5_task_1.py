# Вариант 10
# 1.Дана матрица A(N, M). Определите общее число ненулевых элементов в матрице
# и сумму индексов нулевых элементов матрицы.
# 2.Дана квадратная матрица A(N, N) целых чисел. Определить номера столбцов матрицы,
# элементы которых образуют невозрастающую последовательность.
# 3.Дана квадратная матрица A(N, N) целых чисел. Вычислить сумму S1 элементов массива,
# расположенных над главной диагональю, cумму S2 элементов массива, расположенных
# над побочной диагональю. Найти НОД(S1, S2).



from random import randint

N = int(input('Введите N: '))
M = int(input('Введите M: '))

A = []

for i in range(N):
    A.append([0]*M)

for i in range(N):
    for j in range(M):
        A[i][j] = randint(-5, 5)
null_indx = 0
zero_counter = 0

for i in range(N):
    for j in range(M):
        if A[i][j] == 0:
            zero_counter += 1
            null_indx += i+1 + j+1
for i in range(len(A)):
    for j in range(len(A[i])):
        print("%3d" % (A[i][j]), end=' ')
    print()
print("\nКоличесиво нулевых символов: {} \nСумма их индексов: {}\n".format(zero_counter,null_indx))

del A, N

N = int(input('Введите N: '))
A = []
TMP = []
for i in range(N):
    A.append([0]*N)

for i in range(N):
    for j in range(N):
        A[i][j] = randint(-5, 5)

for j in range(N):
    for i in range(N-1):
        if A[i][j] >= A[i+1][j]:
            TMP.append(j)
        else:   #ОТМЕНА ПАЦАНЫ ОТМЕНА УДАЛЯЕМСЯ !!!!!!!!
            while j in TMP:
                TMP.pop()
            break

for i in range(len(A)):
    for j in range(len(A[i])):
        print("%3d" % (A[i][j]), end=' ')
    print()

print('\n', set(TMP))

