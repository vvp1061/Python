firstset = {'a', 'b', 'c', 'd', 'e'}
secondset = {'d', 'e', 'f', 'g', 'h', 'i'}
thirdset = {1, 2, 3, 4, 5, 6}
forthset = {5, 6, 7, 8, 9, 10}


print('Объединение')
print(firstset | secondset)

print('Пересечение')
print(firstset & secondset)

print('Входят в A, но не входят в B')
print(thirdset - forthset)

print('Входят в A | B, но не входят в A & B')
print(firstset ^ secondset)

print('Сравнение')
print(True) if thirdset == forthset else print(False)

print('Добавление 777')
print(forthset)
forthset.add(777)
print(forthset)

print('Удаление 777')
forthset.discard(777)
print(forthset)

print('Преобразование строки к множеству')
str = 'hello'
print(set(str))