from tkinter import *
import mysql.connector
import tkinter as tk
from PIL import Image,ImageTk

root=Tk()
root.title("Patient Dashboard")
screen_width = root.winfo_screenwidth()+2
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
bg="#FEFFB7"
font=('times new roman',14)

frame=Frame(root,width=screen_width,height=screen_height,bg=bg)
frame.pack(fill="both")

image_file=Image.open("example.png")
image=ImageTk.PhotoImage(image_file)
image_file=image_file.resize((150,200))
image=ImageTk.PhotoImage(image_file)
image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,padx=10,pady=20)

frame2=Frame(frame,bg=bg)
frame2.grid(row=1,column=2,padx=20,pady=20,sticky='n')

id_label=Label(frame2,text='Patient ID:',font=font,bg=bg)
id_label.grid(row=1,column=2,sticky='ne',padx=5)

name_label=Label(frame2,text="Name:",font=font,bg=bg)
name_label.grid(row=1,column=3,sticky='ne',padx=5)

email_label=Label(frame2,text="Email:",font=font,bg=bg)
email_label.grid(row=1,column=4,sticky='ne',padx=5)

number=Label(frame2,text="Contact Number:",font=font,bg=bg)
number.grid(row=1,column=5,sticky='ne',padx=5)

address=Label(frame2,text="Address:",font=font,bg=bg)
address.grid(row=1,column=6,sticky='ne',padx=5)

city=Label(frame2,text="City:",font=font,bg=bg)
city.grid(row=1,column=7,sticky='ne',padx=5)

test=Label(frame2,text="\n",font=font,bg=bg)
test.grid(row=2,column=2)

dob=Label(frame2,text="Date Of Birth:",font=font,bg=bg)
dob.grid(row=3,column=2,sticky='ne',padx=5)

gender=Label(frame2,text="Gender:",font=font,bg=bg)
gender.grid(row=3,column=3,sticky='ne',padx=5)

weight=Label(frame2,text="Weight:",font=font,bg=bg)
weight.grid(row=3,column=4,sticky='ne',padx=5)

height=Label(frame2,text="Height:",font=font,bg=bg)
height.grid(row=3,column=5,sticky='ne',padx=5)

blg=Label(frame2,text="Blood Group:",font=font,bg=bg)
blg.grid(row=3,column=6,sticky='ne',padx=5)

insu=Label(frame2,text="Insurence ID:",font=font,bg=bg)
insu.grid(row=3,column=7,sticky='ne',padx=5)

alle=Label(frame2,text="Allergies:",font=font,bg=bg)
alle.grid(row=3,column=8,sticky='ne',padx=5)


frame_tab=Frame(root,width=screen_width,height=screen_height-300,bg=bg)
frame_tab.pack()
from tkinter import ttk

notebook=ttk.Notebook(frame_tab,width=screen_width,height=screen_height-300)

tab1=ttk.Frame(notebook)
tab2=ttk.Frame(notebook)
tab3=ttk.Frame(notebook)

notebook.add(tab1,text="Daily Record")
notebook.add(tab2,text="Immunizations")
notebook.add(tab3,text="Screening")

label1=Label(tab1,text="Daily Records section")
label2=Label(tab2,text="Immunizations Section")
label3=Label(tab3,text="Screening Section")

label1.pack()
label2.pack()
label3.pack()



notebook.pack()

root.mainloop()