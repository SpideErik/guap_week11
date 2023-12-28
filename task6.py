from random import randint, sample


def get_words():
    words = []
    for i in input('Введите слова>').split():
        words.append(i.lower())
    return words


def print_prompt(words, idx):
    word = words[idx]
    na = word.count('а')
    no = word.count('о')
    print(f'Количество букв а: {na}, количество букв о: {no}')
    print(f'Две буквы из слова слева', sample(words[idx-1], 2))
    if len(word) < len(words[idx+1]):
        print('Слово справа длиннее')
    else:
        print('Слово справа короче')


def print_words(words):
    for i, v in enumerate(words, 1):
        print(f'{i}:{v}', end=' ')
    print()


words = get_words()
idx_word = randint(1, len(words) - 2)
print_prompt(words, idx)
print_words(words)
n = int(input('Введите номер слова>')) - 1
if idx_word == n:
    print('Угадал')
else:
    print('Не угадал')
