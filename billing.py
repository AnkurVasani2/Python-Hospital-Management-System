import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hospital"
)

# Create the GUI window

root = tk.Tk()
root.title("Hospital Bill Invoice")
root.config(bg='#FEFFB7')
root.geometry("800x600+100+100")

# Create labels and entry widgets for user input
label0 = tk.Label(root, text="Patient Name:", font=('Times New Roman', 12), bg='#FEFFB7')
label0.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry0 = tk.Entry(root)
entry0.grid(row=0, column=1)

label1 = tk.Label(root, text="Patient ID:", font=('Times New Roman', 12), bg='#FEFFB7')
label1.grid(row=0, column=2, padx=5, pady=5, sticky="w")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=3)

label2 = tk.Label(root, text="Patient Email:", font=('Times New Roman', 12), bg='#FEFFB7')
label2.grid(row=0, column=4, padx=5, pady=5, sticky="w")
entry2 = tk.Entry(root)
entry2.grid(row=0, column=5)

label3 = tk.Label(root, text="Contact Number:", font=('Times New Roman', 12), bg='#FEFFB7')
label3.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry3 = tk.Entry(root)
entry3.grid(row=1, column=1)

label4 = tk.Label(root, text="Insurance ID:", font=('Times New Roman', 12), bg='#FEFFB7')
label4.grid(row=1, column=2, padx=5, pady=5, sticky="w")
entry4 = tk.Entry(root)
entry4.grid(row=1, column=3)

label5 = tk.Label(root, text="Patient Age:", font=('Times New Roman', 12), bg='#FEFFB7')
label5.grid(row=1, column=4, padx=5, pady=5, sticky="w")
entry5 = tk.Entry(root)
entry5.grid(row=1, column=5)

label6 = tk.Label(root, text="Room Charge:", font=('Times New Roman', 12), bg='#FEFFB7')
label6.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry6 = tk.Entry(root)
entry6.grid(row=2, column=1)

label7 = tk.Label(root, text="Doctor's Fee:", font=('Times New Roman', 12), bg='#FEFFB7')
label7.grid(row=2, column=2, padx=5, pady=5, sticky="w")
entry7 = tk.Entry(root)
entry7.grid(row=2, column=3)

label8 = tk.Label(root, text="Medication Charges:", font=('Times New Roman', 12), bg='#FEFFB7')
label8.grid(row=2, column=4, padx=5, pady=5, sticky="w")
entry8 = tk.Entry(root)
entry8.grid(row=2, column=5)

# Create a button to calculate the total bill
def calculate_bill():
    # Get user input values
    patient_name = entry0.get()
    patient_id = entry1.get()
    patient_email = entry2.get()
    contact_number = entry3.get()
    insurance_id = entry4.get()
    patient_age = entry5.get()
    room_charge = float(entry6.get())
    doctor_fee = float(entry7.get())
    medication_charges = float(entry8.get())

    total = room_charge + lab_fees + med_charges

    # Display total bill
    total_bill.configure(text="₹{:.2f}".format(total))

button = tk.Button(root, text="Calculate", command=calculate_bill, bg='#E6E6FA')
button.grid(row=10, column=1)


# Create a label to display the total bill
label9 = tk.Label(root, text="Total Bill:", bg='#FEFFB7')
label9.grid(row=11, column=0, padx=10)

total_bill = tk.Label(root, text="", bg='#FEFFB7')
total_bill.grid(row=11, column=1)

root.mainloop()
