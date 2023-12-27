from random import randint


def buble_sort(x):
    for i in range(len(x)-1, 0, -1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]


lst = []
for i in range(15):
    lst.append(randint(0, 100))
print(f'Исходные данные {lst}')
buble_sort(lst)
print(f'Отсортированные данные {lst}')
