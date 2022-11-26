# Вариант 10
#     1. Дан файл, в котором записан текст. В другой  файл выводятся только те строки,
#     в которых есть слова, начинающиеся с буквы  «А».


def aLetter(str):
    lettersA = 'aAаА'
    if str[0] in lettersA:
        return True
    else:
        return False


fin = open("input_1.txt", "r")
fout = open("output_1.txt", "w")

while True:
    s = fin.readline().split()
    for i in s:
        if aLetter(i):
            fout.write(' '.join(s) + "\n")
    if not s:
        break

fin.close()
fout.close()

