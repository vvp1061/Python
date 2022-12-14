# Вариант 10
# 1.  Вводится последовательность из N чисел. Найти и вывести те числа, которые являются числами Фибоначчи {f1=1, f2=1, fi= f i-1 + f i-2}.
# 2.  Найти все натуральные числа х, у и z из интервала от 1 до 20, для которых выполняется равенство: x*y^2=z^2.


n = int(input('Введите число N: '))

for i in range(1, n+1):
    print(i, end=' ')
print('')

f1 = 1
f2 = 1

while f2 < n:
    print(f2, end=' ')
    f1, f2 = f2, f1 + f2
print('')
print('_'*16)
print("%3s | %3s | %3s" % ('X', ' Y', 'Z'))
for x in range (1, 21):
    for y in range (1, 20):
        for z in range(1, 20):
            if x*y**2 == z**2:
                print("%3d | %3d | %3d" % (x, y, z))

