import tkinter as tk
import mysql.connector
import tkinter.ttk as ttk
from datetime import datetime
import tkinter.messagebox as mb
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mini_project_2023"
)

bg="#FEFFB7"
def fetch():
    try:
        cur=con.cursor()
        sql="select * from patient"
        cur.execute(sql)
        status = False
        name=entry0.get()
        myresult=cur.fetchall()
        for x in myresult:
            if x[0] == name:
                status = True
                break
        if status:
            cur.execute('select * from patient where name=%s',(name,))
            myresults=cur.fetchall()
            for i in myresults:
                entry1.config(text=i[14],font=font,bg=bg)
                entry2.config(text=i[2],font=font,bg=bg)
                entry3.config(text=i[3],font=font,bg=bg)
                entry4.config(text=i[15],font=font,bg=bg)
                dob_entry.config(text=i[6],font=font,bg=bg)
    except Exception as e:
        print("Exception Occured")
        print(e)

# Create the GUI window
font=('times new roman',14)
root = tk.Tk()
root.title("Hospital Bill Invoice")
root.config(bg='#FEFFB7')
root.geometry("900x300")

bill=tk.Label(root,text="Bill",font=('times new roman',30),bg="#FEFFB7")
bill.grid(row=1, column=0,columnspan=6,rowspan=2, padx=5, pady=5, sticky="n")

# Create labels and entry widgets for user input
label0 = tk.Label(root, text="Patient Name:", font=font, bg='#FEFFB7')
label0.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry0 = tk.Entry(root)
entry0.grid(row=3, column=1)

label1 = tk.Label(root, text="Patient ID:", font=font, bg='#FEFFB7')
label1.grid(row=3, column=2, padx=5, pady=5, sticky="e")
entry1 = tk.Label(root)
entry1.grid(row=3, column=3)

label2 = tk.Label(root, text="Patient Email:", font=font, bg='#FEFFB7')
label2.grid(row=3, column=4, padx=5, pady=5, sticky="e")
entry2 = tk.Label(root)
entry2.grid(row=3, column=5)

label3 = tk.Label(root, text="Contact Number:", font=font, bg='#FEFFB7')
label3.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry3 = tk.Label(root)
entry3.grid(row=4, column=1)

label4 = tk.Label(root, text="Insurance ID:", font=font, bg='#FEFFB7')
label4.grid(row=4, column=2, padx=5, pady=5, sticky="e")
entry4 = tk.Label(root)
entry4.grid(row=4, column=3)

from tkcalendar import DateEntry

label5 = tk.Label(root, text="Patient DOB:", font=font, bg='#FEFFB7')
label5.grid(row=4, column=4, padx=5, pady=5, sticky="e")
dob_entry = tk.Label(root)
dob_entry.grid(row=4,column=5,padx=2,pady=5,sticky='w')

admission=tk.Label(root,text="Admission Date:",font=font,bg="#FEFFB7")
admission.grid(row=5,column=0,padx=2,pady=5,sticky='e')
admission_date= DateEntry(root,date_pattern='dd/mm/yy', width=16, background='darkblue',foreground='white', borderwidth=2)
admission_date.grid(row=5,column=1,padx=2,pady=5,sticky='w')

discharge=tk.Label(root,text="Discharge Date:",font=font,bg="#FEFFB7")
discharge.grid(row=5, column=2, padx=5, pady=5, sticky="e")
discharge_date= DateEntry(root,date_pattern='dd/mm/yy', width=16, background='darkblue',foreground='white', borderwidth=2)
discharge_date.grid(row=5,column=3,padx=2,pady=5,sticky='w')

label6 = tk.Label(root, text="Room Charge:", font=font, bg='#FEFFB7')
label6.grid(row=5, column=4, padx=5, pady=5, sticky="e")
entry6 = tk.Label(root)
entry6.grid(row=5, column=5)

label7 = tk.Label(root, text="Doctor's Fee:", font=font, bg='#FEFFB7')
label7.grid(row=6, column=0, padx=5, pady=5, sticky="e")
entry7 = tk.Label(root)
entry7.grid(row=6, column=1)

def calculate():
    start = datetime.strptime(admission_date.get(), '%d/%m/%y')
    end = datetime.strptime(discharge_date.get(), '%d/%m/%y')
    days = abs((end - start).days)
    entry6.config(text=days*50,font=font,bg=bg)
    entry7.config(text=days*100,font=font,bg=bg)

def file_bill():
    cur=con.cursor()
    sql='insert into bill (p_id,name,email,contact,insurance,dob,admission,discharge,total) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    p_id=entry1.cget("text")
    name=entry0.get()
    email=entry2.cget("text")
    contact=entry3.cget("text")
    insurance=entry4.cget("text")
    dob=dob_entry.cget("text")
    admission=datetime.strptime(admission_date.get(), '%d/%m/%y')
    discharge=datetime.strptime(discharge_date.get(), '%d/%m/%y')
    total=bill_label.cget("text")
    val=(p_id,name,email,contact,insurance,dob,admission,discharge,total)
    cur.execute(sql,val)
    con.commit()
    mb.showinfo(title="Successful!",message='Record Inserted Successfully')

def update_text(var_dict, dose_dict, menubutton, bill_label):
    selected_items = [item for item, var in var_dict.items() if var.get()]
    total_bill = 0
    room_charges=float(entry6.cget("text"))
    doctor_charges=float(entry7.cget("text"))
    if selected_items:
        for item in selected_items:
            dose = dose_dict[item].get()
            if int(dose) > 0:
                total_bill += int(dose) * prices[item]
                total_bill+=room_charges+doctor_charges
        menubutton.config(text=", ".join("{} x {}".format(item, dose_dict[item].get()) for item in selected_items))
    else:
        menubutton.config(text="Select Medicines")
    bill_label.config(text="Total Bill: Rs.{:.2f}".format(total_bill))

medicines = ["Paracetamol", "Ibuprofen", "Aspirin", "Codeine"]
prices = {"Paracetamol": 450, "Ibuprofen": 750, "Aspirin": 475, "Codeine": 800}
var_dict = {}
dose_dict = {}

label8 = tk.Label(root, text="Medicine Charge:", font=font, bg='#FEFFB7')
label8.grid(row=6, column=2, padx=5, pady=5, sticky="e")
menubutton = tk.Menubutton(root, text="Select Medicines", indicatoron=True, borderwidth=1, relief="solid")
menubutton.grid(row=6,column=3,padx=5,pady=5,sticky='w')

# Create a custom menu
menu = tk.Menu(menubutton, tearoff=False)

# Add the checkboxes and doses to the menu
for item in medicines:
    var = tk.BooleanVar(value=False)
    var_dict[item] = var
    dose_var = tk.StringVar(value="0")
    dose_dict[item] = dose_var
    menu.add_checkbutton(label=item, variable=var, onvalue=True, offvalue=False)
    menu.add_command(label=f"Enter dose for {item}", command=lambda x=item: root.after(1, get_dose(x, dose_dict)))

def get_dose(item, dose_dict):
    top = tk.Toplevel(root)
    top.title(f"Enter dose for {item}")
    entry = tk.Entry(top, width=10, textvariable=dose_dict[item])
    entry.pack(padx=10, pady=10)
    button = tk.Button(top, text="OK", command=top.destroy)
    button.pack(pady=10)

# Add a separator and a "Clear" option to the menu
menu.add_separator()
menu.add_command(label="Clear", command=lambda: clear_menu(var_dict, dose_dict, menubutton, bill_label))

# Set the menubutton's menu to the custom menu
menubutton.config(menu=menu)

menu.config(postcommand=lambda: update_text(var_dict, dose_dict, menubutton, bill_label))

# Define a function to clear the menu and reset the bill
def clear_menu(var_dict, dose_dict, menubutton, bill_label):
    for var in var_dict.values():
        var.set(False)
    for dose_var in dose_dict.values():
        dose_var.set("0")
    menubutton.config(text="Select Medicines")
    bill_label.config(text="Total Bill: Rs.0.00")
# Create a function to calculate the total bill and display it
# Create a button to calculate the total bill

fetch_button = tk.Button(root, text="FETCH", font=font, bg='#FF5733',command=fetch)
fetch_button.grid(row=7, column=2, pady=20)


calculate_button=tk.Button(root,text="CALCULATE",font=font,bg="#FF5733",command=calculate)
calculate_button.grid(row=7, column=3, pady=20)


file_button = tk.Button(root, text="FILE", font=font, bg='#FF5733',command=file_bill)
file_button.grid(row=7, column=4, pady=20)

# Create a label to display the total bill
bill_label = tk.Label(root, text="Total Bill: Rs.", font=font, bg='#FEFFB7')
bill_label.grid(row=7, column=1)

root.mainloop()
