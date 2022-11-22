# Алгоритм сортировки фон Неймана. Упорядочить массив а1, а2,, аn по неубыванию
# с помощью алгоритма сортировки слияниями:
# а) каждая пара соседних элементов сливается в одну группу из двух элементов
# (последняя группа может состоять из одного элемента);
# б) каждая пара соседних двухэлементных групп сливается в одну четырёх- элементную группу и т.д.
# При каждом слиянии новая укрупненная группа сортируется. Использовать функцию сортировки.

from random import randint


def merge_lists(first_list, second_list):
    tmp = []
    i = j = 0
    while i < len(first_list) and j < len(second_list):
        if first_list[i] < second_list[j]:
            tmp.append(first_list[i])
            i += 1
        else:
            tmp.append(second_list[j])
            j += 1
    if i < len(first_list):
        tmp += first_list[i:]
    if j < len(second_list):
        tmp += second_list[j:]
    return tmp


def fon_neyman_sort(arr):
    if len(arr) == 1:
        return arr
    div_place = len(arr) // 2
    left = arr[:div_place]
    right = arr[div_place:]

    left = fon_neyman_sort(left)
    right = fon_neyman_sort(right)

    return merge_lists(left, right)


n = int(input('Введите число элементов массива: '))
array = []
print('Сгенерированный массив: ')
for i in range(n):
    array.append(randint(0, 15))
    print(array[i], end=' ')
print()

print("Отсортированный массив: ")
res = fon_neyman_sort(array)
# print(res)
for i in range(n):
    print(res[i], end=' ')
print()