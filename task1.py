def greeting(name):
    print(f'Hello {name}!')


def bye(name):
    print(f'Goodbye {name}!')


name = input('Enter your name>').title()
greeting(name)
bye(name)
