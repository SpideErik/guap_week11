from tkinter import *


def print_str():
    global s
    global pos
    print(f'{s[:pos]}[{s[pos]}]{s[pos+1:]}')


def left():
    global s
    global pos
    if pos > 0:
        pos -= 1
    print_str()


def right():
    global s
    global pos
    if pos < len(s)-1:
        pos += 1
    print_str()


s = input('Введите строку>')
pos = 1
left()

root = Tk()
root.title('Задача 4')
Button(text='<-', command=left, font='Arial 24').pack(anchor=W, side=LEFT)
Button(text='->', command=right, font='Arial 24').pack(anchor=E, side=RIGHT)

root.mainloop()
