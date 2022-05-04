from tkinter import *
from tkinter import messagebox
import mysql.connector
import pyttsx3 as sx

sound = sx.init()
voices = sound.getProperty("voices")
sound.setProperty("voice", voices[1].id)
sound.setProperty("rate",150)
sound.setProperty("volume",3.0)

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

cur = db.cursor() 

try:
    cur.execute("create database login")
    cur.execute("use login")
    cur.execute("create table log_det (name varchar(30),phone int(11) primary key,username varchar(30),passwd varchar(30))")

except:
    cur.execute("use login")
#----------------XXXXXXXXXXXXXXXXXXXXXX-------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def chatpage():
    w2.destroy()

def login_check():
    usn=lu.get()
    psn=lp.get()

    global text

    try:
        cur.execute("select * from log_det where username='%s'"%(usn))
    except:
        messagebox.showerror("Try Again","Check Username and Password")
        lpu.delete(0,END)
        lpp.delete(0,END)
        
    data = cur.fetchall()

    try:
        if(usn==data[0][2] and psn==data[0][3]):
            text = "Welcome, " + data[0][0]
            print(text)
            chatpage()
        else:
            messagebox.showerror("Try Again","Check Username and Password")
            lpu.delete(0,END)
            lpp.delete(0,END)
    except:
        messagebox.showerror("Try Again","Check Username and Password")
        lpu.delete(0,END)
        lpp.delete(0,END)

def login():
    w.destroy()
    global w2,lu,lp,lpu,lpp
    w2=Tk()
    w2.title("Chat Bot")
    w2.geometry("925x500+300+200")
    w2.config(bg="White")
    w2.resizable(False,False)
    img=PhotoImage(file="E:\\python_codes\\app project\\chatbot.png")
    Label(w2,image=img,bg="white").place(x=50,y=100)

    f2=Frame(w2,width=350,height=340,bg="#e9f0ea")
    f2.place(x=450,y=60)

    Label(f2,text="Sign-In",font=("bold",20)).place(x=120,y=20)

    lu=StringVar()
    lpu=Entry(f2,textvariable=lu,width=23,border=1,font=("bold",15))
    lpu.place(x=50,y=120)
    lpu.insert(0,"Username")

    lp=StringVar()
    lpp=Entry(f2,textvariable=lp,width=23,border=1,font=("bold",15),show="*")
    lpp.place(x=50,y=190)
    lpp.insert(0,"Password")

    Button(f2,text="Log-in",width=10,font=("bold",15),bg="#5fb375",fg="white",command=login_check).place(x=120,y=240)

    w2.mainloop()


def sign_complete():
    global n1,ph1
    n1=n.get()
    ph1=ph.get()
    un1=un.get()
    psd1=psd.get()

    try:
        cur.execute("insert into log_det values ('%s',%d,'%s','%s')" % (n1,ph1,un1,psd1))
        db.commit()
        messagebox.showinfo("Account","Account Created")
        w.destroy()
        login()
    except:
        messagebox.showerror("Try Again","Mobile Number already Registered")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0,END)
        e4.delete(0,END)


def sign_up():

    global w,n,ph,un,psd,e1,e2,e3,e4,img
    w=Tk()
    w.title("Chat Bot")
    w.geometry("925x500+300+200")
    w.config(bg="White")
    w.resizable(False,False)
    img=PhotoImage(file='chatbot.png')
    Label(w,image=img,bg="white").place(x=50,y=100)

    f=Frame(w,width=350,height=390,bg="#e9f0ea")
    f.place(x=450,y=40)

    Label(f,text="Sign-Up",font=("bold",20)).place(x=120,y=20)

    n=StringVar()
    e1=Entry(f,textvariable=n,width=23,border=1,font=("bold",15))
    e1.place(x=50,y=100)
    e1.insert(0,"Name")

    #Frame(f,width=295,height=2,bg="grey").place(x=35,y=140)

    ph=IntVar()
    e2=Entry(f,textvariable=ph,width=23,border=1,font=("bold",15))
    e2.place(x=50,y=150)
    e2.insert(0,"Mobile Number ")

    un=StringVar()
    e3=Entry(f,textvariable=un,width=23,border=1,font=("bold",15))
    e3.place(x=50,y=200)
    e3.insert(0,"Username")

    psd=StringVar()
    e4=Entry(f,textvariable=psd,width=23,border=1,font=("bold",15),show="*")
    e4.place(x=50,y=250)
    e4.insert(0,"Password")

    try: 
        Button(f,text="Submit",width=10,font=("bold",15),bg="#5fb375",fg="white",command=sign_complete).place(x=120,y=290)
    except:
        messagebox.showinfo("Account","Fill all the details")

    
    Button(f,text="Log-in",width=10,font=("bold",15),bg="#5fb375",fg="white",command=login).place(x=120,y=340)

    w.mainloop()

sign_up()
