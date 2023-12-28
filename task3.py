def find_names(words):
    names = []
    for i in words:
        if i[0].isupper():
            names.append(i)
    return names


words = input('Введите список>').split()
names = find_names(words)
print(f'Найдены имена: {names}')
