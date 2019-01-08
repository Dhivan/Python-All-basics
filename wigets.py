from tkinter import *

root = Tk()
one = Label(root, text='Hi', fg='red', bg='green')
one.pack(fill=Y)
two = Label(root, text='Hello', fg='green', bg='yellow')
two.pack(fill=X)
three = Label(root, text='welcome', fg='blue', bg='black')
three.pack(fill=Y)

root.mainloop()