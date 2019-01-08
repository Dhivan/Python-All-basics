from tkinter import *

root= Tk()
topframe= Frame(root)
topframe.pack()
bottomframe= Frame(root)
bottomframe.pack()
button1 = Button(topframe,text='Button1', fg='blue')
button2 = Button(topframe,text='Button2', fg='blue')
button3 = Button(bottomframe,text='Button3', fg='blue')
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack()
root.mainloop()