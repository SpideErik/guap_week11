from tkinter import *


def print_str(s, pos):
    print(f'{s[:pos]}[{s[pos]}]{s[pos+1:]}')


def left():
    global s
    global pos
    if pos > 0:
        pos -= 1
    print_str(s, pos)


def right():
    global s
    global pos
    if pos < len(s)-1:
        pos += 1
    print_str(s, pos)


s = input('Введите строку>')
pos = 0
print_str(s, pos)

root = Tk()
root.title('Задача 4')
Button(text='<-', command=left, font='Arial 24').pack(anchor=W, side=LEFT, padx=20, pady=20)
Button(text='->', command=right, font='Arial 24').pack(anchor=E, side=RIGHT, padx=10, pady=10)

root.mainloop()
