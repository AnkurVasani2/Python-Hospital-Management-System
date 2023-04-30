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

# Create labels and entry widgets for user input
label0 = tk.Label(root, text="Patient Name:", bg='#FEFFB7')
label0.grid(row=0, column=0)
entry0 = tk.Entry(root)
entry0.grid(row=0, column=1)

label00 = tk.Label(root, text="Patient ID:", bg='#FEFFB7')
label00.grid(row=1, column=0)
entry00 = tk.Entry(root)
entry00.grid(row=1, column=1)

label1 = tk.Label(root, text="Room Charge:", bg='#FEFFB7')
label1.grid(row=2, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=2, column=1)

label2 = tk.Label(root, text="Doctor's Fee:", bg='#FEFFB7')
label2.grid(row=3, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=3, column=1)

label3 = tk.Label(root, text="Medication Charges:", bg='#FEFFB7')
label3.grid(row=4, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=4, column=1)

# Create a button to calculate the total bill
def calculate_bill():
    # Get user input values
    patient_name = entry0.get()
    patient_id = entry00.get()
    room_charge = float(entry1.get())
    lab_fees = float(entry2.get())
    med_charges = float(entry3.get())

    # Calculate total bill
    total = room_charge + lab_fees + med_charges

    # Display total bill
    total_bill.configure(text="₹{:.2f}".format(total))

button = tk.Button(root, text="Calculate", command=calculate_bill, bg='#E6E6FA')
button.grid(row=5, column=1)

# Create a label to display the total bill
label4 = tk.Label(root, text="Total Bill:", bg='#FEFFB7')
label4.grid(row=6, column=0)
total_bill = tk.Label(root, text="", bg='#FEFFB7')
total_bill.grid(row=6, column=1)

root.mainloop()
