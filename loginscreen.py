from tkinter import *
import tkinter.messagebox


def note():
    tkinter.messagebox.showinfo('Congrats', 'Successfully Done')


def prt():
    print('Successfully Logged in')


def close():
    ans=tkinter.messagebox.askquestion('Warning',"DO YOU WANT TO QUIT?")
    if ans=='yes':
        tkinter.messagebox.showinfo('Closing',"Click ok to close")
    if ans=='no':
        quit()

root = Tk()
label1 = Label(root, text='Enter username:')
label1.grid(row=0)
label2 = Label(root, text='Password:')
label2.grid(row=1)
entry1 = Entry(root)
entry1.grid(row=0, column=1)
entry2 = Entry(root)
entry2.grid(row=1, column=1)
check = Checkbutton(root, text='Keep me log in')
check.grid(columnspan=2)
button = Button(root, text='Log in', bg='Blue', fg='white', command=prt)
button.grid(row=3, column=1)

mainMenu = Menu(root)
root.configure(menu=mainMenu)
subMenu = Menu(mainMenu)
mainMenu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New', command=note)
subMenu.add_command(label='Open', command=note)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=open)

root.mainloop()
