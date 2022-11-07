# Вариант 10
# Написать программу не используя условный оператор.
# На экран вывести TRUE или FALSE
# 10) точка с координатами (x,y) принадлежит внутренней области
# треугольника с вершинами A(0,5), B(5,0) и C(1,0);


Ax = 0
Ay = 5

Bx = 5
By = 0

Cx = 1
Cy = 0

Dx = float(input('Введите координату x: '))
Dy = float(input('Введите координату y: '))

kAB = (Ay - By) / (Ax - Bx)
AB = By - kAB * Bx

kAC = (Ay - Cy) / (Ax - Cx)
AC = Cy - kAC * Cx

kBC = (By - Cy) / (Bx - Cx)
BC = By - kBC * Cx

print((Dy > (kAC * Dx + AC)) and (Dy > (kBC * Dx + BC)) and (Dy < (kAB * Dx + AB)))


