# Вариант 10
# Написать программу, которая выводит таблицу значений функции S(x) для х, изменяющихся в интервале от x1
# до x2 с шагом h. Переменная N – задаёт количество слагаемых для каждого аргумента х из интервала от х1 до х2 для
# функции S(x). Значение переменной h можно подсчитать по формуле h=(x2 – x1)/m, где m – количество точек табуляции
# переменной  x.

x1 = int(input('Введите x1: '))
x2 = int(input('Введите x2: '))
m = int(input('Введите m: '))
n = int(input('Введите n: '))
h = (x2 - x1) / m
print('Длина шага = ', h)


while x1 <= x2:
    Sx = 0
    for k in range(1, n + 1):
        Sx += ((-1) ** (k + 1)) * ((x1 ** (2 * k)) / (2 * k * (2 * k - 1)))
        # print('k =' , k)
    print("%3d | %3.3f" % (x1, Sx))
    x1 += h


