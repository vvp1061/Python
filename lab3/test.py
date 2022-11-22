import copy

a = str(input('Vvedite stroku: '))
b = copy.copy(a)
b = b.replace('A', 'B')
c = ''
for i in range(len(b)):
    if a[i] == b[i]:
        if b[i] == 'b':
            c += 'a'
        if b[i] == 'B':
            c += 'A'
    else:
        c += b[i]

print(c)
