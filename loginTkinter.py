from tkinter import *
from tkinter import messagebox
w = Tk()
w.geometry("300x100")
w.title("Login")

corruser = "NomNickNom"
corrword = "poopie#357"

def check():
    if e1.get() == corruser and e2.get() == corrword:
        messagebox.showinfo("Correct","Access Granted")
    elif e1.get() == corruser and e2.get!= corrword:
        messagebox.showinfo("Wrong","Incorrect Password; Access Denied")
    else:
        messagebox.showinfo("Incorrect","Access Denied")

user = Label(w,text="Username")
word = Label(w,text = "Password")
e1 = Entry(w,width = 40)
e2 = Entry(w,width = 40,show="*")
login = Button(w,text="Login",command = check)

user.place(x=20,y=20)
word.place(x=20,y=50)
e1.place(x=100,y=20)
e2.place(x=100,y=50)
login.place(x=250,y=70)
