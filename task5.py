from random import randint


n = int(input('Введите n>'))
x = []
for _ in range(n):
    x.append(randint(0, 1))
print(f'Исходные данные {x}')

max_len = 0
cur_len = 0
for v in x:
    if v == 1:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0

print(f'Максимальная длина последовательности из 1 = {max_len}')
