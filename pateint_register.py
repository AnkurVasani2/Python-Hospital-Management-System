#registration form patient
from tkinter import *
base = Tk()
screen_height = base.winfo_screenheight()-300
base.geometry(f"900x{screen_height}")
base.title("Patient Register")
base.configure(bg="#FEFFB7")

font=font=("times new roman",15)
bg="#FEFFB7"
patient=Label(base,text="Patient Register",font=("times new roman",30),bg="#FEFFB7")
patient.place(relx=0.5,rely=0.05,anchor="center")

frame=Frame(base,width=600,height=screen_height-100,bg=bg)
frame.pack(fill="both",padx=0,pady=70)
# frame.place(relx=0.2,rely=0.5)

name=Label(frame,text="Enter Name:",font=font,bg=bg)
name.grid(row=2,column=1,padx=2,pady=5,sticky='e')

name_entry=Entry(frame,font=font)
name_entry.grid(row=2,column=2,padx=2,pady=5,sticky='w')


Id=Label(frame,text="Enter ID:",font=font,bg=bg)
Id.grid(row=3,column=1,padx=2,pady=5,sticky='e')

id_entry=Entry(frame,font=font)
id_entry.grid(row=3,column=2,padx=2,pady=5,sticky='w')


email=Label(frame,text="Enter Email:",font=font,bg=bg)
email.grid(row=4,column=1,padx=2,pady=5,sticky='e')

email_entry=Entry(frame,font=font)
email_entry.grid(row=4,column=2,padx=2,pady=5,sticky='w')

number=Label(frame,text="Contact Number:",font=font,bg=bg)
number.grid(row=5,column=1,padx=3,pady=5,sticky='e')

number_entry=Entry(frame,font=font)
number_entry.grid(row=5,column=2,padx=2,pady=5,sticky='w')

address=Label(frame,text="Address:",font=font,bg=bg)
address.grid(row=6,column=1,padx=2,pady=5,sticky='e')

address_entry=Entry(frame,font=font)
address_entry.grid(row=6,column=2,padx=2,pady=5,sticky='w')

list_of_cntry = ("Mumbai", "Delhi", "Pune", "Banglore")
cv = StringVar()
drplist = OptionMenu(frame, cv, *list_of_cntry)
drplist.config(width=15)
cv.set("Mumbai")
city = Label(frame, text="Select City:",font=font,bg="#FEFFB7")
city.grid(row=7,column=1,padx=2,pady=5,sticky='e')
drplist.grid(row=7,column=2,padx=2,pady=5)

dob=Label(frame,text="Date of Birth:",font=font,bg=bg)
dob.grid(row=8,column=1,padx=2,pady=5,sticky='e')

from tkcalendar import DateEntry

dob_entry = DateEntry(frame, width=15, background='darkblue',foreground='white', borderwidth=2)
dob_entry.grid(row=8,column=2,padx=2,pady=5,sticky='w')

gender = Label(frame, text="Select Gender", font=font,bg=bg)
gender.grid(row=9,column=1,padx=2,pady=5,sticky='e')
list_of_gntry = ("Male", "Female", "Others")
gv = StringVar()
droplist = OptionMenu(frame, gv, *list_of_gntry)
droplist.config(width=15)
gv.set("Male")
droplist.grid(row=9,column=2,padx=2,pady=5)

weight=Label(frame,text="Weight:",font=font,bg=bg)
weight.grid(row=2,column=4,padx=2,pady=5,sticky='e')

weight_entry=Entry(frame,font=font)
weight_entry.grid(row=2,column=5,padx=2,pady=5,sticky='w')

height=Label(frame,text="Height:",font=font,bg=bg)
height.grid(row=3,column=4,padx=2,pady=5,sticky='e')

height_entry=Entry(frame,font=font)
height_entry.grid(row=3,column=5,padx=2,pady=5,sticky='w')

list_of_bg = ("O+", "A+", "B+", "AB+","O-","A-","B-","AB-")
bog = StringVar() 
drplist = OptionMenu(frame, bog, *list_of_bg)
drplist.config(width=15)
bog.set("O+")
blg = Label(frame, text="Select Blood Group", font=font,bg=bg)
blg.grid(row=4,column=4,padx=2,pady=5,sticky='e')
drplist.grid(row=4,column=5,padx=2,pady=5,sticky='w')


insurence=Label(frame,text="Insurence ID:",font=font,bg=bg)
insurence.grid(row=5,column=4,padx=2,pady=5,sticky='e')

insurence_entry=Entry(frame,font=font)
insurence_entry.grid(row=5,column=5,padx=2,pady=5,sticky='w')


allergies=Label(frame,text="Allergies:",font=font,bg=bg)
allergies.grid(row=6,column=4,padx=2,pady=5,sticky='e')
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
c1 = Checkbutton(frame, text='Dust mites',variable=var1, onvalue=1, offvalue=0)
c1.grid(row=6,column=5,padx=2,pady=5,sticky='w')
c2 = Checkbutton(frame, text='Pollen',variable=var2, onvalue=1, offvalue=0)
c2.grid(row=6,column=6,padx=2,pady=5,sticky='w')
c3 = Checkbutton(frame, text='Insect Stings',variable=var3, onvalue=1, offvalue=0)
c3.grid(row=6,column=7,padx=2,pady=5,sticky='w')
c4 = Checkbutton(frame, text='Mold',variable=var4, onvalue=1, offvalue=0)
c4.grid(row=7,column=5,padx=2,pady=5,sticky='w')
c5 = Checkbutton(frame, text='Food',variable=var5, onvalue=1, offvalue=0)
c5.grid(row=7,column=6,padx=2,pady=5,sticky='w')
c6 = Checkbutton(frame, text='Medications',variable=var6, onvalue=1, offvalue=0)
c6.grid(row=7,column=7,padx=2,pady=5,sticky='w')
c7 = Checkbutton(frame, text='Chemicals',variable=var7, onvalue=1, offvalue=0)
c7.grid(row=8,column=5,padx=2,pady=5,sticky='w')
c8 = Checkbutton(frame, text='Pets',variable=var8, onvalue=1, offvalue=0)
c8.grid(row=8,column=6,padx=2,pady=5,sticky='w')
c9 = Checkbutton(frame, text='Latex',variable=var9, onvalue=1, offvalue=0)
c9.grid(row=8,column=7,padx=2,pady=5,sticky='w')

def register():
 pass

register=Button(frame, text="Register", width=15,command=register,bg="#B93030", fg="white", height=2).grid(row=9,column=5)

base.mainloop()