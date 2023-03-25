# karra jadvali o'yini (har bir karra savoliga to'g'ri javob pul bilan taqdirlanadi)
from tkinter import *
from random import randint
from tkinter import messagebox


w=Tk()
w.title("karra jadvalini o'rgatuvchi dastur")
w.geometry("500x350")
#w.resizable(False,False)
#w.overrideredirect(1)
#w.iconbitmap('1.ico')
w.config(background="cyan")

def Karra():
    global i,j
    k = randint(2,10)
    i=k
    j=randint(1,10)
    l2.config(text=f"{i}*{j}=")
    e2.delete(0,'end')
    e2["state"]="normal"
    b2["state"]="normal"
    b3["state"]="normal"

def Bilmadim():
    l2.config(text=f"{i}*{j}={i*j}")
    e2.delete(0,'end')




def Natija():
    q = int(e2.get())
    if q=='':

        messagebox.showwarning("xato!","butun qiymat kiriting!")
    else:
        if i*j == q:
            l3.config(text="barakalla to'g'ri topdingiz!")

        else:
            l3.config(text="iltimos to'g'ri topishga harakat qiling!")



l=Label(w,text="Karra jadvalini o'rgatuvchi dastur",bg="cyan",fg="red",font=("Algeian",20))
l.pack()
l2=Label(w,text="",bg="cyan",fg="blue",font=("Algerian",50))
l2.pack(pady=16)
l3=Label(w,text="",bg="cyan",fg="blue",font=("Algerian",15))
l3.pack(pady=50)
l1=Label(w,text="Javobni kiriting: ",bg="cyan",fg="black",font=("Arial",13))
l1.place(x=2,y=150)
e2=Entry(w,width=15,font=('Helvetica',24),state="disabled")
e2.place(x=130,y=150)
b1=Button(w,text="Boshlash",width=10,font=('Algerian',15),height=3,command=Karra)
b1.place(x=25,y=250)
b2=Button(w,text="Natija",width=10,font=('Algerian',15),height=3, state="disabled",command=Natija)
b2.place(x=190,y=250)
b3=Button(w,text="Bilmadim",font=('Algerian',15),width=10,height=3,state="disabled",command=Bilmadim)
b3.place(x=350,y=250)
w.mainloop()
