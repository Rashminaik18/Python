from tkinter import *
from tkinter.messagebox import *

def on_click(e):
    showinfo('message box','''Why dont scientists trust atoms?
Because they make up everything.''')


# def onEnter(e):
#     showinfo('message box',"Entered the button")


# def onLeave(e):
#     showinfo('message box',"Left the button")

# def onRelease(e):
#     showinfo('message box',"Mouse button is released")

# def onScroll(e):
#     showinfo('message box',"Scrolled over")




win=Tk()
win.geometry("800x400")

b=Button(win,text="Click here",bg="pink",bd="5",width=40,height=5)
b.pack()
b.bind('<Button>',on_click)


win.mainloop()