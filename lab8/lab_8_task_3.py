# Дано 100 целых чисел от 1 до 50. Определить, сколько среди них чисел совершенных чисел.
# Совершенное число — натуральное число, равное сумме всех своих собственных делителей
# (то есть всех положительных делителей, отличных от самого числа).
# Например, 6 — совершенное число, поскольку 1 + 2 + 3 = 6, а 1, 2 и 3 — делители числа 6.

from random import randint


def perfectNumber(n):
    factors = []
    for j in range(1, n):
        if n % j == 0:
            factors.append(j)
    return sum(factors) == n


numbers = []
perfNumbers = []
for i in range(1, 101):
    numbers.append(randint(1, 50))

print(numbers)
mn = set()
for i in numbers:
    if perfectNumber(i):
        perfNumbers.append(i)
        mn.add(i)
# print(sorted(perfNumbers))
print(sorted(mn))
# print('Совершенных чисел:', len(perfNumbers))
