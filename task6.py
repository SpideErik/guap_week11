from random import randint, sample

words = []


def get_words():
    global words
    words = []
    for i in input('Введите слова>').split():
        words.append(i.lower())


def print_prompt():
    word = words[idx_word]
    na = word.count('а')
    no = word.count('о')
    print(f'Количество букв а: {na}, количество букв о: {no}')
    print(f'Две буквы из слова слева', sample(words[idx_word-1], 2))
    if len(word) < len(words[idx_word+1]):
        print('Слово справа длиннее')
    else:
        print('Слово справа короче')


def print_words():
    for i, v in enumerate(words, 1):
        print(f'{i}:{v}', end=' ')
    print()


get_words()
idx_word = randint(1, len(words) - 2)
print_prompt()
print_words()
n = int(input('Введите номер слова>')) - 1
if idx_word == n:
    print('Угадал')
else:
    print('Не угадал')
