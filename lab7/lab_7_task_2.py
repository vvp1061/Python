# #Вариант 10
# 2. Дана последовательность, содержащая от 1 до 30 слов, в каждом из которых от 1 до 5 строчных латинских букв;
# между соседними словами запятая, за последним словом точка. Напечатать:
# а) все слова, которые встречаются в последовательности по одному разу;
# б) все слова в алфавитном порядке. (Разбить предложение на массив слов).

myStr = ' yzabc, rsty, vwx, def, ghi, jklm, nopq.'
myStr = myStr.replace('.', '').strip()
print(sorted(set(list(myStr.split(', ')))))
