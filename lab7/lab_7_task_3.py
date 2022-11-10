# #Вариант 10
# 3. Дана строка, содержащая текст и арифметические выражения вида а Ä в,
# где  Ä – один из знаков +,–,*,/. Выписать все арифметические выражения и вычислить их значения.

myStr = '2*15 sum 6+7 division 30/0 and subtraction 80-40 30/2'
Digits = '0123456789'
Signs = '+-*/'

myStr = list(myStr.split())
for word in myStr:
    f1 = ''
    f2 = ''
    Signa = ''
    fnd = -1
    for i in range(len(word)):
        if (word.find('*') != -1) or (word.find('/') != -1) or (word.find('+')) != -1 or (word.find('-') != -1):
            fnd = max(word.find('*'), word.find('/'), word.find('+'), word.find('-'))
            f1 = word[0:fnd]
            f2 = word[fnd+1:len(word)]
            Signa = word[fnd]
    if Signa == '+':
        print("{}+{}={}".format(int(f1), int(f2), int(f1) + int(f2)))
    elif Signa == '-':
        print("{}-{}={}".format(int(f1), int(f2), int(f1) - int(f2)))
    elif Signa == '*':
        print("{}*{}={}".format(int(f1), int(f2), int(f1) * int(f2)))
    try:
        if Signa == '/' and f2 != 0:
            print("{}/{}={}".format(int(f1), int(f2), int(f1) / int(f2)))
    except ZeroDivisionError:
            print('Деление на 0 невозможно')
