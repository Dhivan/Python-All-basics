from tkinter import *
root = Tk()

def printname():
    print('Welcome')

frame = Frame(root,width=300, height=300)
frame.pack()
button1=Button(root,text='click here', command=printname)
button1.pack()
root.mainloop()
