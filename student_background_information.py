from tkinter import *
import sqlite3
try:
   db=sqlite3.connect('library.db')
   cr=db.cursor()
   cr.execute('create table edit(name text,phone integer,email_id string,gender text,date_of_birth date,course text,batch_year integer,registration_number integer,classX integer,classX_passout integer,classXII integer,classXII _passout integer)')
   db.commit()
except:
    print('Database created successfully')
       

w=Tk()
#Global variable to store data from the form
x=StringVar()#name
y=StringVar()#phone
z=StringVar()#email_id
u=StringVar()#gender
v=StringVar()#date_of_birth
w1=StringVar()#course
q=StringVar()#batch_year
r=StringVar()#registration_number
s=StringVar()#classX
t=StringVar()#classX_passout
m=StringVar()#classXII
n=StringVar()#classXII_passout

w.geometry('1500x1500')
w.config(background='steelblue')
w.title('Student Management System')
img=PhotoImage(file='C:\\Users\\user\\OneDrive\\Documents\\python project\\Tkinter\\icons\\images.png')
w.iconphoto(False, img)

l1=Label(w,text='Student Background Information',font=('times new roman',22),fg='white',bg='black')
l1.pack()

l2=Label(w,text='Name',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l2.place(x=50,y=120)

l3=Label(w,text='Phone',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l3.place(x=50,y=160)

l4=Label(w,text='Email Id',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l4.place(x=50,y=200)

l5=Label(w,text='Gender',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l5.place(x=50,y=240)

l6=Label(w,text='Date of Birth',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l6.place(x=50,y=280)

l7=Label(w,text='Course',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l7.place(x=50,y=320)

l8=Label(w,text='Batch Year',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l8.place(x=50,y=360)

l9=Label(w,text='Registration Number',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l9.place(x=50,y=400)

l10=Label(w,text='Class X%',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l10.place(x=50,y=440)

l11=Label(w,text='Class Passout Year',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l11.place(x=50,y=480)

l12=Label(w,text='Class XII%',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l12.place(x=50,y=520)

l13=Label(w,text='Class XII Passout Year',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l13.place(x=50,y=560)

l14=Label(w,text='Diploma(if any)',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l14.place(x=50,y=600)

l15=Label(w,text='Diploma %(if any)',font=('times new roman',15,'bold'),bg='steelblue',fg='white')
l15.place(x=50,y=640)

#entry box:-
e1=Entry(w,font=('times new roman',20,'bold'),textvar=x)
e1.place(x=270,y=120)

e2=Entry(w,font=('times new roman',20,'bold'),textvar=y)
e2.place(x=270,y=160)

e3=Entry(w,font=('times new roman',20,'bold'),textvar=z)
e3.place(x=270,y=200)

e4=Entry(w,font=('times new roman',20,'bold'),textvar=u)
e4.place(x=270,y=240)

e5=Entry(w,font=('times new roman',20,'bold'),textvar=v)
e5.place(x=270,y=280)

e6=Entry(w,font=('times new roman',20,'bold'),textvar=w1)
e6.place(x=270,y=320)

e7=Entry(w,font=('times new roman',20,'bold'),textvar=q)
e7.place(x=270,y=360)

e8=Entry(w,font=('times new roman',20,'bold'),textvar=r)
e8.place(x=270,y=400)

e9=Entry(w,font=('times new roman',20,'bold'),textvar=s)
e9.place(x=270,y=440)

e10=Entry(w,font=('times new roman',20,'bold'),textvar=t)
e10.place(x=270,y=480)

e11=Entry(w,font=('times new roman',20,'bold'),textvar=m)
e11.place(x=270,y=520)

e12=Entry(w,font=('times new roman',20,'bold'),textvar=n)
e12.place(x=270,y=560)

e13=Entry(w,font=('times new roman',20,'bold'))
e13.place(x=270,y=600)

e14=Entry(w,font=('times new roman',20,'bold'))
e14.place(x=270,y=640)


#clear
def edit():
    x.set('')
    y.set('')
    z.set('')
    u.set('')
    v.set('')
    w1.set('')
    q.set('')
    r.set('')
    s.set('')
    t.set('')
    m.set('')
    n.set('')
b2=Button(w,text='Edit',font=('times new roman',15,'bold'),fg='white',bg='green',command=edit)
b2.place(x=270,y=700)

#update
def update():
    a=x.get()
    b=y.get()
    c=z.get()
    d=u.get()
    e=v.get()
    f=w1.get()
    g=q.get()
    h=r.get()
    i=s.get()
    j=t.get()
    k=m.get()
    l=n.get()
    cr.execute("update from edit set name=? where phone=? where email_id=? where gender=? where date_of_birth=? where course=? where batch_year=? where classX=? where classX_passout=? where classXII=? where classXII_passout=? ",(a,b,c,d,e,f,g,h,i,j,k,l))
    db.commit()    
b3=Button(w,text='Update',font=('times new roman',15,'bold'),fg='white',bg='blue',command=update)
b3.place(x=360,y=700)

w.mainloop()
