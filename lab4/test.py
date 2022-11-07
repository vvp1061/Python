# # # Вариант 10
# # # В одномерном массиве, состоящем из п целых элементов, определить:
# # #     • сумму индексов максимальных элементов массива;
# # #     • произведение элементов массива, в числовой записи которых есть 1;
# # #     • номера двух элементов массива, сумма которых минимальна.
# #
# # import random
# #
# # n = int(input('Введите n: '))
# #
# # array = []
# # tmp_array = []
# # out_array = []
# #
# # for i in range(n):
# #     array.append(random.randint(0, 15))
# #     print(array[i], end=' ')
# # print('')
# #
# #
# # # for i in range(n):
# # #     array.append(int(input('Введите эл-т массива: ')))
# #
# # min_element = min(array)
# # max_element = max(array)
# #
# # tmp_array = array.copy()
# # tmp_array.remove(min_element)
# # sec_min_element = min(tmp_array)
# # count = 0
# # mult = 1
# #
# #
# # for i in range(n):
# #     if array[i] == max_element:
# #         # max_element = array[i]
# #         count += i
# #         # Если find ничего не нашёл, он возвращает -1
# #     if (str(array[i])).find('1') != -1:
# #         mult *= array[i]
# #     elif (str(array[i])).find('1') == 1:
# #         print('Нет элементов, в которых содержится 1')
# #
# #     if array[i] == min_element or array[i] == sec_min_element:
# #         out_array.append(i)
# #
# # print("Сумма индексов максимальных элементов массива: {}\nПроизведение элементов массива, в числовой записи которых "
# #       "есть 1: {}".format(count, mult))
# # print('Для получения минимальной суммы потребуются элементы с индексами:', out_array)
# def print_iterator(it): for x in it: print(x, end=' ') print('\n') # reversed string r = reversed('abc') print(type(r)) print(r) print_iterator(r) # reversed list r = reversed([1, 2, 3]) print_iterator(r) # reversed tuple r = reversed((1, 2, 3)) print_iterator(r) # reversed bytes r = reversed(bytes('abc', 'utf-8')) print_iterator(r) # reversed bytearray r = reversed(bytearray('abc', 'utf-8')) print_iterator(r)

"""
Вариант 1
В одномерном массиве, состоящем из п целых элементов, найти
     первый нечетный элемент массива, который делится на 5.
В одномерном массиве, состоящем из п целых элементов
     удалить элементы, которые при делении на 3 дают остаток 2.
В одномерный массив, состоящий из п целых чисел
     вставить новый элемент перед первым элементом и после последнего элемента.
"""

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

i = 0
while i < n and not (arr[i] % 2 != 0 and arr[i] % 5 == 0):
    i += 1
if i == n:
    print('такого элемента нет')
else:
    print('первый нечетный элемент массива, который делится на 5 -', arr[i])

# удалить элементы, которые при делении на 3 дают остаток 2.

delarr = []  # массив индексов по которым в arr надо удалить элементы
for i in range(n):
    if arr[i] % 3 == 2:
        delarr.append(i)
for i in range(len(delarr)):
    del arr[delarr[i]]
print(*arr)

# В одномерный массив, состоящий из п целых чисел
#     вставить новый элемент перед первым элементом и после последнего элемента.

arr1 = []
for i in range(n):
    arr1.append(int(input()))

value = int(input())

arr1.insert(0, value)
arr1.insert(len(arr1), value)
print(*arr1)