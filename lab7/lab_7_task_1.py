# Вариант №10
# 1. Строка содержит произвольный русский текст. Удалить из текста все гласные буквы.
# Заменить пробел запятой. Выполнить двумя способами:
# а) рассматривая строку как массив символов;
# б) используя процедуры и функции для обработки строк.

letters = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
myString = list(input('Введите строку: '))
finalString = ''

def myFinalString(letters, myString, finalString):
    for i in range(len(myString)):
        if myString[i] not in letters:
            if len(finalString) != 0 and myString[i] == ' ' and finalString[-1] == ' ':
                pass
            else:
                finalString += myString[i]
    del myString

    finalString = list(finalString)
    if len(finalString) > 0:
        if finalString[0] == ' ':
            del finalString[0]
        elif finalString[len(finalString) - 1] == ' ':
            ln = len(finalString) - 1
            del finalString[ln]
    finalString = ''.join(finalString)

    myString = ''
    for i in range(len(finalString)):
        if finalString[i] == ' ':
            myString += ','
        else:
            myString += finalString[i]
    print(myString)

myFinalString(letters, myString, finalString)

print('='*36)

myString2 = list(input('Введите строку: '))
ln = len(myString2) - 1
while ln >= 0:
    if myString2[ln] in letters:
        del myString2[ln]
    ln -= 1
myString2 = ''.join(myString2)
myString2 = myString2.strip()
while "  " in myString2:
    myString2 = myString2.replace("  ", ",")
print(myString2)

