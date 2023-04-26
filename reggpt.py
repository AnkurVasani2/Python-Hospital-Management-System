#registration form patient

from tkinter import *

base = Tk()
base.geometry("500x500")
base.title("Registration Form")
base.configure(bg="#FEFFB7")


# Name label and entry
lb1 = Label(base, text="Enter Name", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb1.place(x=20, y=20)
en1 = Entry(base)
en1.place(x=200, y=20,anchor="w")


lb8 = Label(base, text="Patient ID", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb8.place(x=20, y=60)
en8 = Entry(base)
en8.place(x=200, y=60,anchor="w")


# Email label and entry
lb3 = Label(base, text="Enter Email", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb3.place(x=20, y=100,anchor="w")
en3 = Entry(base)
en3.place(x=200, y=100)

# Contact number label and entry
lb4 = Label(base, text="Contact Number", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb4.place(x=19, y=140,anchor="w")
en4 = Entry(base)
en4.place(x=200, y=140)

# Re-enter password label and entry
lb9 = Label(base, text="Address", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb9.place(x=21, y=180,anchor="w")
en9 = Entry(base)
en9.place(x=200, y=180)


list_of_cntry = ("Mumbai", "Delhi", "Pune", "Banglore")
cv = StringVar()
drplist = OptionMenu(base, cv, *list_of_cntry)
drplist.config(width=15)
cv.set("Mumbai")
lb2 = Label(base, text="Select City", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb2.place(x=20, y=220,anchor="w")
drplist.place(x=200, y=220)


dob_label = Label(base, text="Date of Birth ",width=15, font=("times new roman", 12),bg="#FEFFB7")
dob_label.place(x=20,y=260,anchor="w")
dob_entry = Entry(base)
dob_entry.place(x=200,y=260)


# Gender label and radio buttons
lb5 = Label(base, text="Select Gender", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb5.place(x=20, y=300,anchor="w")
vars = IntVar()
Radiobutton(base, text="Male", padx=5, variable=vars, value=1).place(x=180, y=300)
Radiobutton(base, text="Female", padx=10, variable=vars, value=2).place(x=240, y=300)
Radiobutton(base, text="Others", padx=15, variable=vars, value=3).place(x=310, y=300)

# Weight label and entry
lb6 = Label(base, text="Enter Weight (kg)", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb6.place(x=20, y=340,anchor="w")
en6 = Entry(base)
en6.place(x=200, y=340)

# Weight label and entry
lb = Label(base, text="Enter Height (inches)", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb.place(x=20, y=380,anchor="w")
en6 = Entry(base)
en6.place(x=200, y=380)



# Blood group label and checkboxes
list_of_bg = ("O+", "A+", "B+", "AB+","O-","A-","B-","AB-")
bg = StringVar() 
drplist = OptionMenu(base, bg, *list_of_bg)
drplist.config(width=15)
bg.set("O+")
lb7 = Label(base, text="Select Blood Group", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb7.place(x=20, y=420,anchor="w")
drplist.place(x=200, y=420)


lb10 = Label(base, text="Insurance ID", width=15, font=("times new roman", 12),bg="#FEFFB7")
lb10.place(x=21, y=460,anchor="w")
en10 = Entry(base)
en10.place(x=200, y=460)

lb11=Label(base,text="Allergies",width=15,font=("times new roman",12),bg="#FEFFB7")
lb11.place(x=21, y=500,anchor="w")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10=IntVar()
c1 = Checkbutton(base, text='Asthma',variable=var1, onvalue=1, offvalue=0)
c1.place(x=200,y=500)
c2 = Checkbutton(base, text='Diabetic',variable=var2, onvalue=1, offvalue=0)
c2.place(x=350,y=500)
c3 = Checkbutton(base, text='Vision Disorder',variable=var3, onvalue=1, offvalue=0)
c3.place(x=200,y=540)
c4 = Checkbutton(base, text='Migraine',variable=var4, onvalue=1, offvalue=0)
c4.place(x=350,y=540)
c5 = Checkbutton(base, text='Acute acidity',variable=var5, onvalue=1, offvalue=0)
c5.place(x=200,y=580)
c6 = Checkbutton(base, text='Respiratory problem',variable=var6, onvalue=1, offvalue=0)
c6.place(x=350,y=580)
c7 = Checkbutton(base, text='Dental problem',variable=var7, onvalue=1, offvalue=0)
c7.place(x=200,y=620)
c8 = Checkbutton(base, text='Cardiac disorder',variable=var8, onvalue=1, offvalue=0)
c8.place(x=350,y=620)
c9 = Checkbutton(base, text='Orthopaedic disorder',variable=var9, onvalue=1, offvalue=0)
c9.place(x=200,y=660)
c10 = Checkbutton(base, text='Blood pressure',variable=var10, onvalue=1, offvalue=0)
c10.place(x=350,y=660)


# Register button
Button(base, text="Register", width=15).place(x=200, y=750)

base.mainloop()
