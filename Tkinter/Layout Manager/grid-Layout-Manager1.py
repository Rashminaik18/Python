from tkinter import *

win=Tk()

b1=Button(win,text="Button1",bg="grey")
b2=Button(win,text="Button2",bg="grey")
b3=Button(win,text="Button3",bg="grey")
b4=Button(win,text="Button4",bg="grey")
b5=Button(win,text="Button5",bg="grey")
b6=Button(win,text="Button6",bg="grey")
b7=Button(win,text="Button7",bg="grey")
b8=Button(win,text="Button8",bg="grey")
b9=Button(win,text="Button9",bg="grey")
b10=Button(win,text="Button10",bg="grey")
b11=Button(win,text="Button11",bg="grey")
b12=Button(win,text="Button12",bg="grey")



b1.grid(row=0,column=0,padx=10,pady=10,ipadx=10,ipady=10,sticky="nsew",columnspan=2)

b3.grid(row=0,column=2,padx=10,pady=10,ipadx=10,ipady=10,sticky="ew")
b4.grid(row=0,column=3,padx=10,pady=10,ipadx=10,ipady=10,sticky="nsew")

b5.grid(row=1,column=0,padx=10,pady=10,ipadx=10,ipady=10,sticky="nsew",rowspan=2)
b6.grid(row=1,column=1,padx=10,pady=10,ipadx=10,ipady=10,sticky="ew")
b7.grid(row=1,column=2,padx=10,pady=10,ipadx=10,ipady=10,sticky="nsew")
b8.grid(row=1,column=3,padx=10,pady=10,ipadx=10,ipady=10,sticky="nsew")


b10.grid(row=2,column=1,padx=10,pady=10,ipadx=10,ipady=10,sticky="ns")
b11.grid(row=2,column=2,padx=10,pady=10,ipadx=10,ipady=10,sticky="nsew")
b12.grid(row=2,column=3,padx=10,pady=10,ipadx=10,ipady=10,sticky="ns")


win.grid_columnconfigure(2,weight=1);

win.grid_rowconfigure(2,weight=1)




win.mainloop()
