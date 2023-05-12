import tkinter as tk
import mysql.connector
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
root = tk.Tk()
root.title("Patients")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
bg = "#FEFFB7"
font = ("times new roman",14)
win_frame = tk.Frame(root, width=screen_width, height=screen_height, bg=bg)
win_frame.pack(fill='both',expand='true')

test=tk.Label(win_frame,text="\n",bg=bg)
test.grid(row=1,column=1)

def back():
    pass

back_label=tk.Button(win_frame,text="<- Go Back To Dashboard",bg=bg,font=font,command=back)
back_label.grid(row=2,column=1,padx=10)

patients_label = tk.Label(win_frame, text="Patients", bg=bg, font=("times new roman", 36))
patients_label.place(relx=0.5, rely=0.05, anchor='center')

frame = tk.Frame(win_frame, width=screen_width-8,height=screen_height-200, bg='white', bd=4)
frame.place(relx=0.5, rely=0.15, relwidth=0.95, relheight=0.85, anchor='n')


tree = ttk.Treeview(
    frame, column=("id", "Name", "dob", "age", "gender", "address", "email"), 
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
# tree.bind('<Double-1>', on_item_selected)
tree.pack(side=BOTTOM, fill='both', expand=True, padx=20, pady=20)
con=None
con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mini_project_2023"
        )
try:
    print("Connection Established Successfully")
    cur = con.cursor()
    savequery = "select patient_code,name,dob,age,gender,address,email from patient"
    cur.execute(savequery)
    myresult = cur.fetchall()
    status = False

        # clear the old data from the Treeview
    tree.delete(*tree.get_children())

    for x in myresult:
        if x:
            status = True
            tree.insert('', 'end', text=x[0], values=(x))

    if status != True:
        mb.showerror(title="Error", message='No Records Found')
except Exception as e:
    print('An exception occurred')
    print(e)
    if con:
        con.close()
        print("Resources Released")
root.mainloop()
