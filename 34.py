# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

k = 10
while k >= 1:
    if k % 2 == 0:
        bin = 0 
    elif k % 2 == 0.5:
     bin = 0
    else:
        bin = 1
    k = k / 2
    print(bin, end= '')
print(' ')

