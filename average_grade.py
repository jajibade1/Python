import tkinter
from tkinter import *

root=Tk()
root.title("grade calculator")
root.geometry("500x500")

def Calculate():
    IT101=int(it101entry.get())
    IT102=int(it102entry.get())
    IT103=int(it103entry.get())
    total=(IT101+IT102+IT103)
    Label(text=f"{total}",font="arial 15 bold").place(x=250,y=170)

    average=int(total/3)
    Label(text=f"{average}",font="arial 15 bold").place(x=250,y=210)

    if (average>70):
        grade="Distinction"
    elif (average>50):
        grade="Merit"
    elif (average<45):
        grade="Fail"

    Label(text=f"{grade}",font="arial 15 bold").place(x=250,y=250)

#Subject
sub1=Label(root,text="IT101:", font="arial 10")
sub2=Label(root,text="IT102:", font="arial 10")
sub3=Label(root,text="IT103:", font="arial 10")
total=Label(root,text="Total:", font="arial 10")
avg=Label(root,text="Average:", font="arial 10")
grade=Label(root,text="Grade:", font="arial 10")

sub1.place(x=50,y=20)
sub2.place(x=50,y=70)
sub3.place(x=50,y=120)
total.place(x=50,y=170)
avg.place(x=50,y=210)
grade.place(x=50,y=250)

IT101value=StringVar()
IT102value=StringVar()
IT103value=StringVar()

it101entry=Entry(root,textvariable=IT101value, font="arial 15", width=15)
it102entry=Entry(root,textvariable=IT102value, font="arial 15", width=15)
it103entry=Entry(root,textvariable=IT103value, font="arial 15", width=15)

it101entry.place(x=250,y=20)
it102entry.place(x=250,y=70)
it103entry.place(x=250,y=120)

Button(text="Calculate",font="arial 15", bg="white",bd=10,command=Calculate).place(x=50,y=300)
Button(text="Exit",font="arial 15", bg="white",bd=10,width=10,command=lambda:exit()).place(x=250,y=300)

root.mainloop()
