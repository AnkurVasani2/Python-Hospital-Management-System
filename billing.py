import tkinter as tk
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hospital"
)

class HospitalBillInvoice:
    def __init__(self, master):
        self.master = master
        master.title("Hospital Bill Invoice")

        # Set background color
        master.config(bg='#FEFFB7')

        # Create labels and entry widgets for user input
        self.label1 = tk.Label(master, text="Room Charge:", bg='#FEFFB7')
        self.label1.grid(row=0, column=0)
        self.entry1 = tk.Entry(master)
        self.entry1.grid(row=0, column=1)

        self.label2 = tk.Label(master, text="Doctor's Fee:", bg='#FEFFB7')
        self.label2.grid(row=1, column=0)
        self.entry2 = tk.Entry(master)
        self.entry2.grid(row=1, column=1)

        self.label3 = tk.Label(master, text="Medication Charges:", bg='#FEFFB7')
        self.label3.grid(row=2, column=0)
        self.entry3 = tk.Entry(master)
        self.entry3.grid(row=2, column=1)

        # Create a button to calculate the total bill
        self.button = tk.Button(master, text="Calculate", command=self.calculate_bill, bg='#E6E6FA')
        self.button.grid(row=3, column=1)

        # Create a label to display the total bill
        self.label4 = tk.Label(master, text="Total Bill:", bg='#FEFFB7')
        self.label4.grid(row=4, column=0)
        self.total_bill = tk.Label(master, text="", bg='#FEFFB7')
        self.total_bill.grid(row=4, column=1)

    def calculate_bill(self):
        # Get user input values
        room_charge = float(self.entry1.get())
        lab_fees = float(self.entry2.get())
        med_charges = float(self.entry3.get())

        # Calculate total bill
        total = room_charge + lab_fees + med_charges

        # Display total bill
        self.total_bill.configure(text="₹{:.2f}".format(total))

root = tk.Tk()
my_gui = HospitalBillInvoice(root)
root.mainloop()
