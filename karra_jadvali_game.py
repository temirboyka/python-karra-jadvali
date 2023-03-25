# karra jadvali o'yini
from tkinter import *
from random import randint
from tkinter import messagebox


w=Tk()
w.title("karra dasturi")
w.geometry("250x270")
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
    
    q = e2.get()
    if q =='':

        messagebox.showwarning("qiymat kiritilmadi!","butun qiymat kiriting!")
    
    else:
        if i*j == int(q):
 
            l3.config(text="topdingiz!")
          

        else:

            l3.config(text="topmadingiz!")
            



l2=Label(w,text="",bg="cyan",fg="blue",font=("Algerian",30))
l2.pack(pady=3)
l3=Label(w,text="",bg="cyan",fg="blue",font=("Algerian",15))
l3.pack(pady=5)
l1=Label(w,text="Javobni kiriting: ",bg="cyan",fg="black",font=("Arial",10))
l1.pack(pady=3)
e2=Entry(w,width=10,font=('Helvetica',20),state="disabled")
e2.pack(pady=2)
b1=Button(w,text="Boshlash",width=9,font=('Algerian',9),height=1,command=Karra)
b1.pack(pady=5)
b2=Button(w,text="Natija",width=9,font=('Algerian',9),height=1, state="disabled",command=Natija)
b2.pack(pady=5)
b3=Button(w,text="Bilmadim",width=9,font=('Algerian',9),height=1,state="disabled",command=Bilmadim)
b3.pack(pady=5)
w.mainloop()
