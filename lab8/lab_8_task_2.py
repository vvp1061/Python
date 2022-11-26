# Вариант 3.
# Задача 2
# type letters = set of 'a'..'z';
# Описать процедуру print(А), печатающую в алфавитном порядке все элементы множества А,
# имеющего тип letters.
# Составить, программу, использующую эту процедуру.

def letters():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return sorted(set(alphabet))


print(letters())
