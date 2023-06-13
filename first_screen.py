from tkinter import *
from tkinter import font

root = Tk()
root.title('Tic-Tac-Toe')
root.geometry('600x600')

myfont = font.Font(size= 50)
myfont2 = font.Font(size=20)

global b2
global b1
b1 = 0; b2 = 0

def Button_x(x):
    b1 = 1
    root.destroy()

def Button_y(y):
    b2 = 1
    root.destroy()


title = Label(root , text= 'What would player 1 like to use?', font = myfont2)
title.place(x = 160 , y = 190)
oR = Label(root , text= 'or', font = myfont2)
oR.place(x = 289 , y = 241)
button_x = Button(root, text= 'X', font=myfont, command= lambda : Button_x(0) )
button_x.place(x = 195 , y = 225)
button_y = Button(root, text= 'O', font=myfont, command= lambda : Button_y(0))
button_y.place(x = 335 , y = 225)

root.mainloop()

    