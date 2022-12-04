# Вариант 3.
# Задача 2
# type letters = set of 'a'..'z';
# Описать процедуру print(А), печатающую в алфавитном порядке все элементы множества А,
# имеющего тип letters.
# Составить, программу, использующую эту процедуру.

# def letters():
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     return sorted(set(alphabet))
#
#
# print(letters())

def letters(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = sorted(set(list(alphabet)))
    str = set(list(str))
    outset = set()
    for i in str:
        if i in alphabet:
            outset.add(i)
    print(len(outset))
    return sorted(outset)

s = input('Введите строку: ')
print(letters(s))
