def get_key(listCountry, language):
    for value in listCountry:
        if language == value:
            return language


fin = open("input.txt", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")

N = int(input('Сколько стран выводить? '))
M = input('Какие языки проверить? ')
M = M.split()

country = {}
allLang = set()

while True:
    s = fin.readline()
    if not s:
        break

    string_from_file = s.split()
    country[string_from_file[0]] = []

    for i in string_from_file[1:]:
        country[string_from_file[0]].append(i)
        allLang.add(i)

for j in M:
    if j in allLang:
        fout.write(j + ":\t")
        N_tmp = N
        for key in country:
            if get_key(country[key], j) is not None and N_tmp > 0:
                fout.write(key + " ")
                N_tmp -= 1
        fout.write("\n")

fin.close()
fout.close()
