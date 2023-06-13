from tkinter import *
from tkinter import font
from tkinter import messagebox as mb

def startup():
    b1 = 0
    b2 = 0

    root_initial = Tk()
    root_initial.title('Tic-Tac-Toe')
    root_initial.geometry('600x600')

    myfont = font.Font(size= 50)
    myfont2 = font.Font(size=20)

    def Button_x():
        nonlocal b1
        b1 = 1
        root_initial.destroy()

    def Button_y():
        nonlocal b2
        b2 = 1
        root_initial.destroy()


    title = Label(root_initial , text= 'What would player 1 like to use?', font = myfont2)
    title.place(x = 160 , y = 190)
    oR = Label(root_initial , text= 'or', font = myfont2)
    oR.place(x = 289 , y = 241)
    button_x = Button(root_initial, text= 'X', font=myfont, command= lambda : Button_x() )
    button_x.place(x = 195 , y = 225)
    button_y = Button(root_initial, text= 'O', font=myfont, command= lambda : Button_y())
    button_y.place(x = 335 , y = 225)

    root_initial.mainloop()
    print(b1,b2)
    return (b1,b2)

a = startup()

if(a[0] == 1 or a[1] == 1):
    

    initial = 'X' if a[0] == 1 else 'O'

    root = Tk()
    root.title('Tic-Tac-Toe')
    myfont = font.Font(size= 50)
    button_lists = []
    button_states = [i for i in range(9)]

    def diagonal_check():
        if button_states[0] == button_states[4] == button_states[8]:
            return True
        elif button_states[2] == button_states[4] == button_states[6]:
            return True
        else:
            return False

    def horizontal_check():
        if button_states[0] == button_states[1] == button_states[2]:
            return True
        elif button_states[3] == button_states[4] == button_states[5]:
            return True
        elif button_states[6] == button_states[7] == button_states[8]:
            return True
        else:
            return False
        
    def vertical_check():
        if button_states[0] == button_states[3] == button_states[6]:
            return True
        elif button_states[1] == button_states[4] == button_states[7]:
            return True
        elif button_states[2] == button_states[5] == button_states[8]:
            return True
        else:
            return False

    def win():
         if vertical_check() or horizontal_check() or diagonal_check() :
                  winner = 'X' if button_states.count('X') > button_states.count('O') else 'O'
                  popup = Tk()
                  popup.geometry('100x100')
                  label = Label(popup, text= f"{winner} has won")
                  label.pack()
                  print('you win', 'X' if button_states.count('X') > button_states.count('O') else 'O')
         elif (button_states.count('X') + button_states.count('O')) == 9:
                  popup = Tk()
                  popup.geometry('100x100')
                  label = Label(popup, text= "Draw") 
                  label.pack()

    def button_update(n, ls,m):
        button_lists[n]['text'] = m[len(ls)]
        button_states[n] = m[len(ls)]
        button_lists[n].config(command = lambda : print("hi"))


    def button_pr(z ,ls = [], ):
        m = [initial , 'O' if initial == 'X' else 'X']
        if button_states.count(0) <= 5:
            if len(ls) == 0:
                button_update(z,ls,m)
                ls.append(0)
                print(button_states)
                win()
        
            elif len(ls) > 0:
                button_update(z,ls,m)
                ls.pop()
                win()
                
            
        else: 
            if len(ls) == 0:
                button_update(z,ls,m)
                ls.append(0)
                print(button_states)
            elif len(ls) > 0:
                button_update(z,ls,m)
                ls.pop()
                print(button_states)
        

            
            


    def game_generation():
        
        button = Button(root , width = 3, height = 2, command = lambda : button_pr(0), font = ('helvetica',100))
        button.grid(row= 1 , column= 0)
        button_lists.append(button)

        button1 = Button(root , width = 3, height = 2, command = lambda : button_pr(1), font = ('helvetica',100))
        button1.grid(row= 1 , column= 1)
        button_lists.append(button1)

        button2 = Button(root , width = 3, height = 2, command = lambda : button_pr(2), font = ('helvetica',100))
        button2.grid(row= 1 , column= 2)
        button_lists.append(button2)

        button3 = Button(root , width = 3, height = 2, command = lambda : button_pr(3), font = ('helvetica',100))
        button3.grid(row= 2 , column= 0)
        button_lists.append(button3)

        button4 = Button(root , width = 3, height = 2, command = lambda : button_pr(4), font = ('helvetica',100))
        button4.grid(row= 2 , column= 1)
        button_lists.append(button4)

        button5 = Button(root , width = 3, height = 2, command = lambda : button_pr(5), font = ('helvetica',100))
        button5.grid(row= 2 , column= 2)
        button_lists.append(button5)

        button6 = Button(root , width = 3, height = 2, command = lambda : button_pr(6), font = ('helvetica',100))
        button6.grid(row= 3 , column= 0)
        button_lists.append(button6)

        button7 = Button(root , width = 3, height = 2, command = lambda : button_pr(7), font = ('helvetica',100))
        button7.grid(row= 3 , column= 1)
        button_lists.append(button7)

        button8 = Button(root , width = 3, height = 2, command = lambda : button_pr(8), font = ('helvetica',100))
        button8.grid(row= 3 , column= 2)
        button_lists.append(button8)
        

    game_generation()

        
    
    root.mainloop()


