from tkinter import *

win=Tk()
win.geometry("600x400")
l=Label(win,text="Good morning",bg="red",width="20")
l.place(relx=0.2,rely=0.2,relwidth=0.2,relheight=0.1)
b=Button(win,text="Click on me!!",bg="pink")
b.place(relx=0.4,rely=0.4,relwidth=0.3,relheight=0.2)

win.mainloop()
