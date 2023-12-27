from random import randint


n = int(input('Введите n>'))
x = []
for _ in range(n):
    x.append(randint(0, 1))
print(f'Исходные данные {x}')

max_l = 0
cur_l = 0
for v in x:
    if v == 1:
        cur_l += 1
        if cur_l > max_l:
            max_l = cur_l
    else:
        cur_l = 0


print(f'Длина последовательности из 1 = {max_l}')
