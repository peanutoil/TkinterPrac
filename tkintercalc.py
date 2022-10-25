from tkinter import *
from tkinter import messagebox
w = Tk()
w.geometry("500x400")
w.title("Calculator")

def add():
    num1 = int(e1.get())
    num2 = int(e2.get())
    e3.insert(0, str(num1+num2))

def subtract():
    num1 = int(e1.get())
    num2 = int(e2.get())
    e3.insert(0, str(num1-num2))

def multiply():
    num1 = int(e1.get())
    num2 = int(e2.get())
    e3.insert(0, str(num1*num2))
    
def divide():
    num1 = int(e1.get())
    num2 = int(e2.get())
    e3.insert(0, str(num1/num2))

l1 = Label(text = "Input Number 1:")
e1 = Entry(w,width = 40)
l1.place(x=5,y=50)
e1.place(x=100,y=50)
l2 = Label(text = "Input Number 2:")
e2 = Entry(w,width = 40)
l2.place(x=5,y=100)
e2.place(x=100,y=100)
b1 = Button(w,text="+",width = 7, command = add)
b1.place(x=40,y=150)
b2 = Button(w,text="-",width = 7, command = subtract)
b2.place(x=140,y=150)
b3 = Button(w,text = "*",width = 7, command = multiply)
b3.place(x=240,y=150)
b4 = Button(w,text = "/",width = 7, command = divide)
b4.place(x=340,y=150)
l3 = Label(text = "Result:")
l3.place(x=50,y=200)
e3 = Entry(w,width = 40)
e3.place(x=100,y=200)

w.mainloop()
