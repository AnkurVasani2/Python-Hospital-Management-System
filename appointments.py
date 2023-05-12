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
cur=con.cursor()
bg="#FEFFB7"
def fetch():
    try:
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
                entry4.config(text=i[11],font=font,bg=bg)
                dob_entry.config(text=i[6],font=font,bg=bg)
    except Exception as e:
        print("Exception Occured")
        print(e)

# Create the GUI window
font=('times new roman',14)
root = tk.Tk()
root.title("Patient Appointment")
root.config(bg='#FEFFB7')
root.geometry("900x300")

apt=tk.Label(root,text="Appointment",font=('times new roman',30),bg="#FEFFB7")
apt.grid(row=1, column=0,columnspan=6,rowspan=2, padx=5, pady=5, sticky="n")

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

from tkcalendar import *

label5 = tk.Label(root, text="Patient DOB:", font=font, bg='#FEFFB7')
label5.grid(row=4, column=4, padx=5, pady=5, sticky="e")
dob_entry = tk.Label(root)
dob_entry.grid(row=4,column=5,padx=2,pady=5,sticky='w')

admission=tk.Label(root,text="Appointment Date:",font=font,bg="#FEFFB7")
admission.grid(row=5,column=0,padx=2,pady=5,sticky='e')
admission_date= DateEntry(root,date_pattern='dd/mm/yy', width=16, background='darkblue',foreground='white', borderwidth=2)
admission_date.grid(row=5,column=1,padx=2,pady=5,sticky='w')

preferred_time_label = tk.Label(root, text="Preferred Time:", font=font, bg="#FEFFB7")
preferred_time_label.grid(row=5, column=2, padx=5, pady=5, sticky="e")

def validate_time(input):
    # Ensure that input is in the correct format
    if input == "":
        return True
    try:
        time = time.strptime(input, "%I:%M %p")
        return True
    except ValueError:
        return False

time_var = tk.StringVar()
time_entry = tk.Entry(root, textvariable=time_var, validate="key", validatecommand=(root.register(validate_time), '%P'))
time_entry.grid(row=5,column=3,padx=5,pady=5,sticky="e")

def calculate_available_doctors(time_entry):
  #Calculates all the doctors available in a time slot, depending on the preferred time of the patient.
  global cur
  # Get the list of all doctors.
  cur.execute('SELECT name FROM doctor')
  doctors = cur.fetchall()

  # Get the list of all appointments that are scheduled in the preferred time slot.
  cur.execute('SELECT id FROM doctor WHERE start_shift<= ? AND end_shift >= ?', (time_entry, time_entry))
  appointment_ids = cur.fetchall()

  # Create a list of doctors who are available in the time slot.
  available_doctors = []
  for doctor in doctors:
    if doctor[0] not in appointment_ids:
      available_doctors.append(doctor[0])    
  return available_doctors

# Set the menubutton's menu to the custom menu
fetch_button = tk.Button(root, text="FETCH", font=font, bg='#FF5733',command=fetch)
fetch_button.grid(row=7, column=2, pady=20)

avail_button=tk.Button(root,text="DOCTOR",font=font,bg="#FF5733",command=calculate_available_doctors(time_entry))
avail_button.grid(row=7, column=3, pady=20)

# Create a label to display the total bill
bill_label = tk.Label(root, text="Total Bill: Rs.", font=font, bg='#FEFFB7')
bill_label.grid(row=7, column=1)

root.mainloop()