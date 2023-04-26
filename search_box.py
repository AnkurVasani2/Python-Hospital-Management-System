import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

root=tk.Tk()
root.geometry('800x300')
root.title('Search')
root.resizable(False, False)
window_frame=tk.Frame(root, width=800, height=300,bg='#FEFFB7')
window_frame.pack(fill='both', expand=True)  # Set fill and expand options to 'both'


def search():
    try:
        name=search_box.get()
        dob=dob_box.get()
        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mini_project_2023")
        if con:
            print("Connection Established Successfully")
        cur = con.cursor()
        savequery = "select * from patients"
        cur.execute(savequery)
        myresult = cur.fetchall()
        status = False
        for x in myresult:
            if x[0]==name or x[1]==name or dob==x[2]:
                status=True
                print(x)

                def item_selected(event):
                    for select in tree.selection():
                        item=tree.item(select)
                        record=item['values']
                        showinfo(title='Information',message=','.join(record))
                hs=Scrollbar(frame,orient='horizontal')
                hs.pack(side=BOTTOM,fill='x')
                tree = ttk.Treeview(frame, column=("id", "Name", "dob","age","gender","address","email"), show='headings', height=5,xscrollcommand=hs.set)
                tree.column("# 1", anchor=CENTER)
                tree.heading("# 1", text="ID")
                tree.column("# 2", anchor=CENTER)
                tree.heading("# 2", text="NAME")
                tree.column("# 3", anchor=CENTER)
                tree.heading("# 3", text="DOB")
                tree.column("# 4", anchor=CENTER)
                tree.heading("# 4", text="AGE")
                tree.column("# 5", anchor=CENTER)
                tree.heading("# 5", text="GENDER")
                tree.column("# 6", anchor=CENTER)
                tree.heading("# 6", text="ADDRESS")
                tree.column("# 7", anchor=CENTER)
                tree.heading("# 7", text="EMAIL")
                
                # Insert the data in Treeview widget
                tree.insert('', 'end', text="1", values=(x))
                tree.bind('<<TreeviewSelect>>',item_selected)
                hs.config(command=tree.xview)

                tree.pack(fill='x')
        if status!=True:
            showerror(title="Error",message='No Records Found')
    except Exception as e:
        print('An exception occurred')
        print(e)
    finally:
        if con:
            con.close()
            print("Resourses Released")



search_label=tk.Label(window_frame,text="Search",font=("Times New Roman", 26), bg="#FEFFB7")
search_label.pack()

search_field=tk.Label(window_frame,text="Name/ID:",font=("Times New Roman", 14), bg="#FEFFB7",justify='center')
search_field.place(relx=0.1,rely=0.2)

dob_field=tk.Label(window_frame,text="Date Of Birth:",font=("Times New Roman", 14), bg="#FEFFB7",justify='center')
dob_field.place(relx=0.1,rely=0.3)

myfont = ("Times New Roman", 16)

search_box=tk.Entry(window_frame,font=myfont)
search_box.place(relx=0.3,rely=0.2)


dob_box=tk.Entry(window_frame,font=myfont)
dob_box.place(relx=0.3,rely=0.3)

search_btn=tk.Button(window_frame,text="Search", bg="#B93030", fg="white", height=2, width=15,command=search)
search_btn.place(relx=0.6,rely=0.25)

frame_width=800
frame_height=170

frame=tk.Frame(window_frame,width=800,height=170,bg="white")
frame.pack(side='bottom')

open_btn=Button(frame,text='Open')
open_btn.pack(side=BOTTOM,anchor='se',padx=2)

root.mainloop()
