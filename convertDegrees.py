from tkinter import *
w = Tk()
w.geometry("500x300")
w.title("Farenheit to Celsius")


def calculate():
    e2.delete(0,END)
    F = float(e1.get())
    C = (F-32)/1.8
    e2.insert(0,str(C))

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
      
fare = Label(w,text = "Farenheit:")
cel = Label(w,text = "Celsius:")
calc = Button(w,text = "Calculate",width = 8,command = calculate)
clear = Button(w,text = "Clear", width = 8, command = clear)
leave = Button(w,text = "Quit", width = 8, command = exit)
e1 = Entry(w, width = 40)
e2 = Entry(w, width = 40)
fare.place(x=20,y=20)
cel.place(x=23,y=50)
e1.place(x=80,y=20)
e2.place(x=80,y=50)
calc.place(x=30,y=100)
clear.place(x=120,y=100)
leave.place(x=210,y=100)
    
w.mainloop()
