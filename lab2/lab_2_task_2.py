# Вариант 10
# Даны координаты точки. А (x, y). Определить,  в какой четверти лежит данная точка.

x, y = map(float, input('Введите x и y: ').split())

if x > 0 and y > 0:
    print('Точка в первой четверти')
elif x < 0 < y:
    print('Точка во второй четверти')
elif x < 0 and y < 0:
    print('Точка в третьей четверти')
elif y < 0 < x:
    print('Точка в четвёртой четверти')
else:
    print('Точка в центре системы координат (0, 0)')