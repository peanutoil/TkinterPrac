#broken code
from tkinter import *
from tkinter import messagebox
w = Tk()
w.geometry("300x220")
w.resizable(width = False, height = False)
w.title("Food Price Calculator")

variable = IntVar()
key1=IntVar()
key1.set(2)
key2=IntVar()
key2.set(3)
key3=IntVar()
key3.set(4)
    
def calc():
    variable = IntVar()
    key1=IntVar()
    key1.set(2)
    key2=IntVar()
    key2.set(3)
    key3=IntVar()
    key3.set(4)
    cmd1=lamd
    r1 = Checkbutton(w,text = "Rice",cmd = cmd1)
    r2 = Checkbutton(w,text = "Chocolate",variable = key2)
    r3 = Checkbutton(w,text = "Mango",variable=key3)
    amount = e1.get()
    print(variable)
    if variable == 2:
        price = amount*2
    elif variable == 4:
        price = amount*1
    elif variable == 4:
        price = amount*0.5
    else:
        messagebox.showinfo("Error","Invalid input; Please try again")
    
l1 = Label(w,text = "Please select ONE item")
r1 = Checkbutton(w,text = "Rice",variable = key1)
r2 = Checkbutton(w,text = "Chocolate",variable = key2)
r3 = Checkbutton(w,text = "Mango",variable=key3)
l2 = Label(w,text = "Total Price:")
e1 = Entry(w,width = 20)
e2 = Entry(w,width = 20)
b1 = Button(w,text = "Calculate",command = calc)
l5 = Label(w,text = "Enter Quantity:")
photo1 = PhotoImage(file = "rice.png")
photo2 = PhotoImage(file = "choco.png")
photo3 = PhotoImage(file = "mango.png")
p1 = Label(w,image = photo1)
p2 = Label(w,image = photo2)
p3 = Label(w,image = photo3)
##get value of checkbutton?

l1.place(x=100,y=5)
r1.place(x=5,y=35)
r2.place(x=5,y=65)
r3.place(x=5,y=95)
l5.place(x=5,y=140)
e1.place(x=95,y=140)
b1.place(x=15,y=180)
e2.place(x=95,y=180)
p1.place(x=65,y=25)
p2.place(x=90,y=55)
p3.place(x=75,y=93)

w.mainloop()
