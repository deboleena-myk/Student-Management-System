from tkinter import *
import sqlite3
try:
   db=sqlite3.connect('library.db')
   cr=db.cursor()
   cr.execute('create table login(name text,phone integer)')
   db.commit()
except:
    print('Database created successfully')
       

w=Tk()
#Global variable to store data from the form
x=StringVar()#name
y=StringVar()#phone
w.geometry('1000x1000')
w.config(background='steelblue')
w.title('Student Management System')
img=PhotoImage(file='C:\\Users\\user\\OneDrive\\Documents\\python project\\Tkinter\\icons\\images.png')
w.iconphoto(False, img)

l1=Label(w,text='Registration Form',font=('times new roman',25),fg='white',bg='black')
l1.pack()
l1=Label(w,text='Login Here..',font=('times new roman',25,'bold','italic'),fg='white',bg='orange')
l1.place(x=200,y=60)

l2=Label(w,text='Email',font=('times new roman',22,'bold'),bg='steelblue',fg='white')
l2.place(x=50,y=120)

l3=Label(w,text='Password',font=('times new roman',22,'bold'),bg='steelblue',fg='white')
l3.place(x=50,y=160)

#entry box:-
e1=Entry(w,font=('times new roman',22,'bold'),textvar=x)
e1.place(x=200,y=120)

e2=Entry(w,font=('times new roman',22,'bold'),textvar=y)
e2.place(x=200,y=160)

#button
def submit():
    a=x.get()
    b=y.get()
    cr.execute("insert into login(email id, password)values(?,?)",(a,b))
    db.commit()

    
b1=Button(w,text='Login',font=('times new roman',15,'bold'),fg='white',bg='red',command=submit)
b1.place(x=150,y=270)

#clear
def clear():
    x.set('')
    y.set('')


b2=Button(w,text='Clear',font=('times new roman',15,'bold'),fg='white',bg='green',command=clear)
b2.place(x=220,y=270)

w.mainloop()
