# Вариант 10
# Определить, является ли шестизначное число "счастливым" (сумма первых трех цифр равна сумме последних трех цифр).

six_digit_number = 0
while len(str(six_digit_number)) != 6:
    six_digit_number = input('Введите шестизначное число ')
six_digit_number = str(six_digit_number)

if int(six_digit_number[0])+int(six_digit_number[1])+int(six_digit_number[2]) == int(six_digit_number[3]) + int(six_digit_number[4]) + int(six_digit_number[5]):
    print('Число счастливое')
else:
    print('Число несчастливое')
