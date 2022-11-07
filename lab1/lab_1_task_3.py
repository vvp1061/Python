# Вариант 10
# Запишите логическое выражение, которое принимает значение "TRUE" тогда
# и только тогда, когда точка с координатами (x, y) принадлежит
# заштрихованной области и FALSE  в противном случае.


import math

x = float(input('Введите x: '))
y = float(input('Введите y: '))

circleUp = math.sqrt(math.fabs(4 - x ** 2))

circleDown = -math.sqrt(math.fabs(4 - x ** 2))

if ((2 - x) <= y <= circleUp) or (x <= 0 < y <= (2 + x)) or (
        circleDown <= y <= (-x - 2)) or (x >= 0 >= y >= (x - 2)):
    print('TRUE')
else:
    print('FALSE')

