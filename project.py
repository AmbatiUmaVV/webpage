from tkinter import *
import tkinter.messagebox as MessageBox
import random
top=Tk()
top.geometry("600x300")
top.title("Employment Recruitment System")
def validate():
 name1=t_name.get()
 password1=t_pwd.get()
 if name1=="python" and password1=="project":
    MessageBox.showinfo(name1,"Login Successful")
 else:
    MessageBox.showinfo(name1,"Login Failed")
def registration():
 MessageBox.showinfo("Registration complete")
def validate1():
 MessageBox.showinfo("Login Successful")
 
def forget():
 f1.pack_forget()
 f3=Frame(top,bg="DodgerBlue",height=600,width=1200)
 f3.pack()
 L=Label(f3,text="Enter the Mobile Number or Email to login",fg="white",bg="DodgerBlue",font=("bold",16))
 L.place(x=300,y=100)
 
 m=Label(f3,text="Mobile number :",font=("bold",13),bg="DodgerBlue")
 m.place(x=100,y=200)
 
 E1=Entry()
 E1.place(x=400,y=200)
 
 otp=Label(f3,text="Enter otp :",font=("bold",13),bg="DodgerBlue")
 otp.place(x=100,y=300)
 
 E2=Entry()
 E2.place(x=400,y=300)
 
 c=Label(f3,text="Captcha :",bg="DodgerBlue",font=("bold",13))
 c.place(x=250,y=400)
 
 E3=Entry()
 E3.place(x=550,y=400)
 
 c1=Label(f3,text=random.randint(100000,999999),bg="red")
 c1.place(x=550,y=400)
 
 Or=Label(f3,text="or",font=("bold",18),bg="DodgerBlue",fg="green")
 Or.place(x=420,y=250)
 
 e=Label(f3,text="Email :",font=("bold",13),bg="DodgerBlue")
 e.place(x=500,y=200)
 
 E3=Entry()
 E3.place(x=800,y=200)
 
 otp1=Label(f3,text="Enter otp :",font=("bold",13),bg="DodgerBlue")
 otp1.place(x=500,y=300)
 
 E4=Entry()
 E4.place(x=800,y=300)
 
 login1=Button(f3,text="Login",command=validate1)
 login1.place(x=420,y=500)
 
def register():
 f1.pack_forget()
 f2=Frame(top,height=600,width=1200,bg="DodgerBlue")
 f2.pack()
 l=Label(f2,text="New Registration",fg="white",font=("bold",15),bg="GREEN")
 l.place(x=530,y=30)
 fullname=Label(f2,text="FullName :",fg="white",bg="orange",font=("bold",13))
 fullname.place(x=500,y=60)
 entry_fullname=Entry(f2)
 entry_fullname.place(x=700,y=60)
 
 username=Label(f2,text="UserName :",fg="white",bg="DodgerBlue",font=("bold",13))
 username.place(x=500,y=90)
 entry_username=Entry(f2)
 entry_username.place(x=700,y=90)
 
 pwd=Label(f2,text="Password :",fg="white",bg="DodgerBlue",font=("bold",13))
 pwd.place(x=500,y=120)
 entry_pwd=Entry(f2)
 entry_pwd.place(x=700,y=120)
 cpwd=Label(f2,text="ConfirmPassword :",fg="white",bg="DodgerBlue",font=("bold",13))
 cpwd.place(x=500,y=150)
 entry_cpwd=Entry(f2)
 entry_cpwd.place(x=700,y=150)
 emailid=Label(f2,text="Email-id :",fg="white",bg="DodgerBlue",font=("bold",13))
 emailid.place(x=500,y=180)
 entry_emailid=Entry(f2)
 entry_emailid.place(x=700,y=180)
 
 gender = Label(f2,text="Gender :",fg="white",bg="DodgerBlue",font=("bold",13))
 gender.place(x=500,y=240)
 v=IntVar()
 rb1=Radiobutton(f2,text="Male",variable=v,value=1)
 rb1.place(x=700,y=240)
 rb2=Radiobutton(f2,text="Female",variable=v,value=2)
 rb2.place(x=750,y=240)
 rb3=Radiobutton(f2,text="Transgender",variable=v,value=3)
 rb3.place(x=810,y=240)
 country=Label(f2,text="Country :",fg="white",bg="DodgerBlue",font=("bold",13))
 country.place(x=500,y=270)
 
list_of_country=["Afghanistan","Albania","Algeria","Andorra","Angola","Argentina",
"Australia","Austria","Bahamas","Bangladesh","Belgium","Bhutan","Bolivia",
"Brazil","Canada","Chile","Colombia","Denmark","Egypt","France",
 
"Germany","Hungary","Iceland","India","Indinesia","Iran","Italy","Japan",
 
"Kenya","Kuwait","Liberia","Libya","Malaysia","Mexico","Nepal",
 
"NewZealand","Peru","Russia","Singapore","Spain","Srilanka","Switzerland",
 "Turkey","Uk","Us","Zambia"]
c=StringVar()
f2=Frame(top,height=600,width=1200,bg="Pink")
f2.pack()
droplist=OptionMenu(f2,c,*list_of_country)
droplist.config(width=15)
c.set("Select Country")
droplist.place(x=700,y=270)
language = Label(f2,text="Languages known :",fg="white",bg="DodgerBlue",font=("bold",13))
language.place(x=500,y=300)
v1 = IntVar()
c1 = Checkbutton(f2,text="English",variable=v1,font=("bold",13))
v2 = IntVar()
c2 = Checkbutton(f2,text="Hindi",variable=v2,font=("bold",13))
v3 = IntVar()
c3 = Checkbutton(f2,text="Telugu",variable=v3,font=("bold",13))
v4 = IntVar()
c4 = Checkbutton(f2,text="German",variable=v4,font=("bold",13))
c1.place(x=700,y=300)
c2.place(x=700,y=330)
c3.place(x=700,y=360)
c4.place(x=700,y=390)
submit = Button(f2,text="Submit",command=registration)
submit.place(x=600,y=450)
f1=Frame(top)
f1.pack()
top.configure(bg="orange")
title = Label(top,text="Login Form",fg="white",bg="#003e53",font=("bold,15"))
title.place(x=700,y=30)
name=Label(top,text="UserName",fg="white",bg="#003e53",font=("bold",13))
name.place(x=600,y=90)
password=Label(top,text="Password",fg="white",bg="#003e53",font=("bold",13))
password.place(x=600,y=120)
t_name=Entry()
t_name.place(x=700,y=90)
t_pwd=Entry()
t_pwd.place(x=700,y=120)
Login = Button(top,text = "Login",command = validate)
Login.place(x=700,y=150)
signup = Button(top,text = "Signup",command = register)
signup.place(x=600,y=180)
forgetpw = Button(top,text="ForgetPassword",command=forget)
forgetpw.place(x=750,y=180)
top.mainloop()