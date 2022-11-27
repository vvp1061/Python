# Вариант 10
# Дан список стран и языков на которых говорят в этой стране в формате <Название Страны>:<язык1><язык2><язык3>...  в файле. 
# На ввод задается N - длина списка и список языков. Для каждого языка укажите, в каких странах на нем говорят.

def get_key(listCountry, language):
    for value in listCountry:
        if language == value:
            return language


fin = open("input_2.txt", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")

N = int(input('Сколько языков? '))

country = {}
allLang = set()

while True:
    s = fin.readline()
    s = s.replace("<", "")
    s = s.replace(">", " ")
    s = s.replace(":", " ")
    s = s.strip()
    if not s:
        break

    string_from_file = s.split()
    country[string_from_file[0]] = []

    for i in string_from_file[1:]:
        country[string_from_file[0]].append(i)
        allLang.add(i)

allLang = sorted(allLang)

for j in allLang:
    if N > 0:
        fout.write(j + ":\t")
        for key in country:
            if get_key(country[key], j) is not None:
                fout.write(key + " ")
        fout.write("\n")
    N -= 1

fin.close()
fout.close()
