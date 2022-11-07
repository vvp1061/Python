# Вариант 10
# 1. Дано натуральное число:
# •    сколько раз первая цифра встречается в данном числе;
# •    верно ли, что данное число начинается на А, а заканчивается на В (цифры А и В вводятся с клавиатуры).
# 2.   Найти все четырёхзначные числа, в которых ровно две одинаковых цифры.
# 3.   Найти количество различных цифр данного натурального числа.


number = int(input('Число: '))
number = str(number)

len_num = len(number)
first_number = (number[0])
last_number = (number[len_num-1])

A = int(input('Введите число А: '))
B = int(input('Введите число B: '))


if A == int(first_number) and B == int(last_number):
    print('Верно')
else:
    print('Неверно')

count = 0
for i in number:
    if i == first_number:
        count += 1

print("Число %s встречается %d раз(а)" % (first_number, count))

print('Количество различных цифр данного натурального числа:', len(set(number)))
# в set попадают только уникальные элементы, следовательно один элемент - повторяющийся
for i in range(1000, 10000):
    if len(set(str(i))) == 3:
        print(i, end=' ')



