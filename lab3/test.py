# """
# Написать программу, которая выводит таблицу значений функции S(x) для х,
# изменяющихся в интервале от x1 до x2 с шагом h.  Переменная N – задает
# количество слагаемых для каждого аргумента х из интервала от х1 до х2 для
# функции S(x). Значение переменной h можно подсчитать по формуле h=(x2 –
# x1)/m, где m – количество точек табуляции переменной  x.
# """
# from math import *
#
# x1 = int(input('Введите x1: '))
# x2 = int(input('Введите x2: '))
# m = int(input('Введите m: '))
# print('S(x)   x    N')
#
# i = x1
# while i <= x2:
#     N = int(input())
#     s = 0
#     for k in range(N+1):
#         s += (-1)**k*i**(2*k+1)/factorial(2*k+1)
#     print('{:.3f} {} {}'.format(s, i, N))
#     i = i + (x2-x1)/m
#
#
'''
Задание 3
Написать программу, которая выводит таблицу значений функции S(x) для х, изменяющихся в интервале от x1 до x2 с шагом h.
Переменная N – задает количество слагаемых для каждого аргумента х из интервала от х1 до х2 для функции S(x).
Значение переменной h можно подсчитать по формуле h=(x2 – x1)/m, где m – количество точек табуляции переменной  x.
вариант 7
'''
import math

x1, x2, m, N = map(float, input('enter x1, x2, m and N: ').split())
h = (x2 - x1) / m
s = [0] * int(m + 1)
x = x1
for i in range(int(m) + 1):
    s[i] = 0
    for k in range(int(N) + 1):
        s[i] += (-1 ** k) * (2 * k ** 2 + 1) / math.factorial(2 * k) * (x ** 2)
    x += h

print("| x    |  S(x)|")
x = x1
for i in range(int(m) + 1):
    print("|{:3.3f}|{:3.3f}|".format(x, s[i]))
    x += h