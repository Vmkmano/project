import sqlite3
from tkinter import *

con=sqlite3.connect(r"gui.db")

cur=con.cursor()






def reg():
    name_info=name.get()
    age_info=age.get()
    city_info=city.get()
    phone_number_info=phone_number.get()
    gender_info=gender.get()
    total_info=totalfee.get()

    cur.execute("insert into EMOPLYEE values('{}','{}','{}','{}','{}','{}')".format(name_info,age_info,city_info,phone_number_info,gender_info,total_info)) 

    con.commit()
    con.close()

    # file=open(name_info +".txt","w")
    # file.write(name_info+"\n")
    # file.write(age_info+"\n")
    # file.write(city_info+"\n")
    # file.write(phone_number_info+"\n")
    # file.write(gender_info+"\n")
    # file.write(total_info+"\n")
    # file.close
    lab=Label(text="succeuss...!",font=("Arial 10"),fg="green")
    lab.place(x=230,y=470)

#creating gui
root=Tk()
root.geometry("500x500")
root.resizable(False,False)
#creating label
Label(root,text="College Profile Entery",font="arial 22").pack(pady=22)
Label(text="Name",font="arial 15").place(x=40,y=130)
Label(text="Age",font="arial 15").place(x=40,y=170)
Label(text="City",font="arial 15").place(x=40,y=210)
Label(text="Phone Number",font="arial 15").place(x=40,y=250)
Label(text="Gender",font="arial 15").place(x=40,y=290)
Label(text="Totalfees",font="arial 15").place(x=40,y=330)

#stroing value
name=StringVar()
age=StringVar()
city=StringVar()
phone_number=StringVar()
gender=StringVar()
totalfee=StringVar()

#createing entry box

Name_entry=Entry(root,textvariable=name,width=20,bd=2,font=20).place(x=200,y=130)
age_entry=Entry(root,textvariable=age,width=20,bd=2,font=20).place(x=200,y=170)
city_entry=Entry(root,textvariable=city,width=20,bd=2,font=20).place(x=200,y=210)
phone_number_entry=Entry(root,textvariable=phone_number,width=20,bd=2,font=20).place(x=200,y=250)
gender_entry=Entry(root,textvariable=gender,width=20,bd=2,font=20).place(x=200,y=290)
totalfee_entry=Entry(root,textvariable=totalfee,width=20,bd=2,font=20).place(x=200,y=330)
#creating check box

check=IntVar
checkbox=Checkbutton(text="remember me",variable=check,font="Arial 15").place(x=200,y=380)
#button
but1=Button(text="Enter",width=10,height=2,font="Arial 10",command=lambda:reg()).place(x=230,y=420)


root.mainloop()