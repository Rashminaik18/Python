from tkinter import *
from tkinter.messagebox import *

def final(e):
    showinfo('Confirmation box',"Order placed")

win=Tk()


win.geometry("800x500")

win.title("Donut Store Order Window")

frame1=Frame(win,width=400,height=500,bg="#F8F3D9")
frame1.pack(side="left",expand=True,fill=BOTH)
frame1.pack_propagate(False)
frame2=Frame(win,width=400,height=500,bg="#F8F3D9")
frame2.pack(side="right",expand=True,fill=BOTH)
frame2.pack_propagate(False)







l1=Label(frame1,text="Welcome to Donut Affair",font=("Lucida Fax",20),bg="#EBE5C2")
l1.pack(anchor=NW,pady=10,padx=10)

l=Label(frame1,text="Enter your name",font=("Lucida Fax",15))
l.pack(anchor=NW,pady=10,padx=20)

name=Entry(frame1,width=30)
name.pack(anchor=NW,pady=5,padx=25)


l2=Label(frame1,text="Select the order type:",font=("Lucida Fax",15),)
l2.pack(anchor=NW,pady=10,padx=20)

orderType=StringVar()
orderType.set(None)

r1=Radiobutton(frame1,text="Dine-in",variable=orderType,value="Dine-In",font=("Lucida Fax",10))
r2=Radiobutton(frame1,text="Takeaway",variable=orderType,value="Takeaway",font=("Lucida Fax",10))
r3=Radiobutton(frame1,text="Delivery",variable=orderType,value="Delivery",font=("Lucida Fax",10))
r1.pack(anchor=NW,padx=25,pady=5)
r2.pack(anchor=NW,padx=25,pady=5)
r3.pack(anchor=NW,padx=25,pady=5)

flavour=StringVar()
flavour.set(None)

l3=Label(frame1,text="Select the Flavour:",font=("Lucida Fax",15))
l3.pack(anchor=NW,pady=10,padx=25)

o=OptionMenu(frame1,flavour,*("Chocolate Glazed","Vanilla Cream","Strawberry Frosted","Blueberry Bliss", "Biscoff Lava", "Classic Sugar"))
o.configure(font=("Lucida Fax",10))
o.pack(anchor=NW,padx=25,pady=5,ipadx=5,ipady=5)

l4=Label(frame1,text="Select the Toppings:",font=("Lucida Fax",15))
l4.pack(anchor=NW,pady=10,padx=25)

choco=IntVar()
choco.set(None)
nuts=IntVar()
nuts.set(None)
caramel=IntVar()
caramel.set(None)
cream=IntVar()
cream.set(None)
plain=IntVar()
plain.set(None)


c1=Checkbutton(frame1,text="Chocochips",variable=choco)
c2=Checkbutton(frame1,text="Crushed Nuts",variable=nuts)
c3=Checkbutton(frame1,text="Caramel Drizzle" ,variable=caramel)
c4=Checkbutton(frame1,text="Extra Cream",variable=cream)
c5=Checkbutton(frame1,text="No toppings",variable=plain)
c1.pack(anchor=NW,padx=25,pady=5)
c2.pack(anchor=NW,padx=25,pady=5)
c3.pack(anchor=NW,padx=25,pady=5)
c4.pack(anchor=NW,padx=25,pady=5)
c5.pack(anchor=NW,padx=25,pady=5)

l5=Label(frame2,text="Select Quantity",font=("Lucida Fax",15),)
l5.pack(anchor=NW,pady=10,padx=25)


quantity=Scale(frame2,from_=0,to=10,orient=HORIZONTAL)
quantity.pack(anchor=NW,padx=25,pady=5)

l6=Label(frame2,text="Enter Instructions if any:",font=("Lucida Fax",15))
l6.pack(anchor=NW,pady=10,padx=25)

txt=Text(frame2,width=70,height=3)
txt.pack(anchor=NW,pady=10,padx=25)

submit=Button(frame2,text="Place Order",width=20,height=3)
submit.bind('<Button-1>',final)

submit.pack(anchor=CENTER,pady=30)





win.mainloop()

