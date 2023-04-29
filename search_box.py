import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *

root = tk.Tk()
root.geometry('800x500')
root.title('Search')
root.resizable(False, False)
window_frame = tk.Frame(root, width=800, height=500, bg='#FEFFB7')
window_frame.pack(fill='both', expand=True)

con = None

def connect():
    global con
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mini_project_2023"
        )
    except Exception as e:
        print("Unable to connect to the database.")
        print(e)

def close():
    if con:
        con.close()
        print("Resources Released")

connect()
# create the Treeview widget outside the loop
tree = ttk.Treeview(
    window_frame, column=("id", "Name", "dob", "age", "gender", "address", "email"), 
    show='headings', height=5
)
tree.column("# 1", anchor=CENTER, width=50)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER, width=150)
tree.heading("# 2", text="NAME")
tree.column("# 3", anchor=CENTER, width=100)
tree.heading("# 3", text="DOB")
tree.column("# 4", anchor=CENTER, width=50)
tree.heading("# 4", text="AGE")
tree.column("# 5", anchor=CENTER, width=75)
tree.heading("# 5", text="GENDER")
tree.column("# 6", anchor=CENTER, width=200)
tree.heading("# 6", text="ADDRESS")
tree.column("# 7", anchor=CENTER, width=150)
tree.heading("# 7", text="EMAIL")
tree.pack(side=BOTTOM, fill='both', expand=True, padx=20, pady=20)

def search():
    global con
    try:
        name = search_box.get()
        dob = dob_box.get()
        print("Connection Established Successfully")
        cur = con.cursor()
        savequery = "select * from patients"
        cur.execute(savequery)
        myresult = cur.fetchall()
        status = False

            # clear the old data from the Treeview
        tree.delete(*tree.get_children())

        for x in myresult:
            if name==x[0] or name==x[1] or dob == x[2]:
                status = True
                print(x)
                tree.insert('', 'end', text=x[0], values=(x))

        if status != True:
            showerror(title="Error", message='No Records Found')
    except Exception as e:
        print('An exception occurred')
        print(e)
        if con:
            con.close()
            print("Resources Released")
        connect()


search_label = tk.Label(window_frame, text="Search", font=("Times New Roman", 26), bg="#FEFFB7")
search_label.pack()

search_field = tk.Label(window_frame, text="Name/ID:", font=("Times New Roman", 14), bg="#FEFFB7")
search_field.pack(side=LEFT, padx=20, pady=20)

search_box = tk.Entry(window_frame, font=("Times New Roman", 14), bd=2)
search_box.pack(side=LEFT, padx=10, pady=20)


dob_field = tk.Label(window_frame, text="DOB:", font=("Times New Roman", 14), bg="#FEFFB7")
dob_field.place(x=400, y=67)

dob_box = Entry(window_frame, font=("Times New Roman", 14), width=25)
dob_box.place(x=450, y=67)

search_button = tk.Button(window_frame, text="Search", font=("Times New Roman", 14), command=search)
search_button.place(x=650, y=95)

root.mainloop()
