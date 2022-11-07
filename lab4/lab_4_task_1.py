# Вариант 10
# В одномерном массиве, состоящем из п целых элементов, определить:
#     • сумму индексов максимальных элементов массива;
#     • произведение элементов массива, в числовой записи которых есть 1;
#     • номера двух элементов массива, сумма которых минимальна.

import random

n = int(input('Введите n: '))

array = []
tmp_array = []
out_array = []

for i in range(n):
    array.append(random.randint(0, 15))
    print(array[i], end=' ')
print('')


# for i in range(n):
#     array.append(int(input('Введите эл-т массива: ')))

min_element = min(array)
max_element = max(array)

tmp_array = array.copy()
tmp_array.remove(min_element)
sec_min_element = min(tmp_array)
count = 0
mult = 1


for i in range(n):
    if array[i] == max_element:
        # max_element = array[i]
        count += i
        # Если find ничего не нашёл, он возвращает -1
    if (str(array[i])).find('1') != -1:
        mult *= array[i]
    elif (str(array[i])).find('1') == 1:
        print('Нет элементов, в которых содержится 1')

    if array[i] == min_element or array[i] == sec_min_element:
        out_array.append(i)

print("Сумма индексов максимальных элементов массива: {}\nПроизведение элементов массива, в числовой записи которых "
      "есть 1: {}".format(count, mult))
print('Для получения минимальной суммы потребуются элементы с индексами:', out_array)
